"""
Importe les données de boutik.sql (MySQL) vers la base SQLite Django.
Lance avec : python import_mysql_to_sqlite.py
"""
import os
import re
import sqlite3
import sys

SQL_FILE = os.path.join(os.path.dirname(__file__), 'boutik.sql')
DB_FILE  = os.path.join(os.path.dirname(__file__), 'db.sqlite3')

# Tables gérées par les migrations Django — on ne les ré-importe pas
SKIP_TABLES = {
    'django_content_type',
    'auth_permission',
    'django_migrations',
    'django_session',         # sessions expirées, inutiles
    'socialaccount_socialaccount',
    'socialaccount_socialapp',
    'socialaccount_socialtoken',
    'account_emailaddress',
    'account_emailconfirmation',
}

# Ordre d'insertion pour respecter les clés étrangères
INSERT_ORDER = [
    'auth_user',
    'accounts_profile',
    'store_category',
    'store_color',
    'store_size',
    'store_banner',
    'store_product',
    'store_product_colors',
    'store_product_sizes',
    'store_productreview',
    'store_wishlist',
    'orders_cart',
    'orders_cartitem',
    'orders_orderitem',
    'orders_order',
    'orders_order_items',
    'payments_payment',
    'auth_group',
    'auth_group_permissions',
    'auth_user_groups',
    'auth_user_user_permissions',
    'django_admin_log',
]


def remove_backticks(sql: str) -> str:
    # Retire les backticks MySQL et quote les mots réservés SQLite
    sql = sql.replace('`order`', '"order"')
    sql = sql.replace('`key`', '"key"')
    sql = sql.replace('`', '')
    # MySQL escape \' -> SQLite escape ''
    sql = sql.replace("\\'", "''")
    return sql


def extract_inserts(sql_text: str) -> dict[str, list[str]]:
    """Extrait les INSERT par table depuis le dump MySQL."""
    inserts: dict[str, list[str]] = {}

    # Chaque INSERT peut s'étaler sur plusieurs lignes ; on les reconstitue
    # en cherchant les blocs INSERT INTO `table` (...) VALUES ... ;
    pattern = re.compile(
        r"INSERT INTO `(\w+)` \([^)]+\) VALUES\s*(.*?);",
        re.DOTALL,
    )
    for m in pattern.finditer(sql_text):
        table = m.group(1)
        if table in SKIP_TABLES:
            continue
        stmt = remove_backticks(m.group(0)).rstrip(';') + ';'
        inserts.setdefault(table, []).append(stmt)

    return inserts


def run():
    print(f"Lecture de {SQL_FILE}...")
    with open(SQL_FILE, encoding='utf-8') as f:
        sql_text = f.read()

    inserts = extract_inserts(sql_text)
    print(f"Tables trouvées : {list(inserts.keys())}")

    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = OFF")
    cur = conn.cursor()

    errors = []

    def do_table(table):
        stmts = inserts.get(table, [])
        if not stmts:
            return
        print(f"  >> {table} ({len(stmts)} INSERT)...", end=' ')
        ok = 0
        for stmt in stmts:
            try:
                cur.executescript(stmt)
                ok += 1
            except sqlite3.Error as e:
                errors.append((table, str(e)[:120]))
        print(f"OK ({ok}/{len(stmts)})")

    # Vider les tables dans l'ordre inverse pour éviter les contraintes FK
    print("\nSuppression des données existantes...")
    for table in reversed(INSERT_ORDER):
        try:
            cur.execute(f"DELETE FROM {table}")
        except sqlite3.Error:
            pass

    print("\nInsertion des données...")
    for table in INSERT_ORDER:
        do_table(table)

    # Tables non listées dans INSERT_ORDER mais présentes dans le dump
    remaining = [t for t in inserts if t not in INSERT_ORDER]
    for table in remaining:
        do_table(table)

    conn.commit()
    conn.execute("PRAGMA foreign_keys = ON")
    conn.close()

    if errors:
        print(f"\n{len(errors)} erreur(s) :")
        for tbl, err in errors:
            print(f"  [{tbl}] {err}")
    else:
        print("\nImportation terminée sans erreur.")


if __name__ == '__main__':
    run()
