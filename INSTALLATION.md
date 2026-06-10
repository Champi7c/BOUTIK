# Bright Looks — Guide d'Installation

## Prérequis
- Python 3.10+
- MySQL / phpMyAdmin (port 3308)
- pip

---

## 1. Installation des dépendances

```bash
cd /Library/AKOA/BOUTIK
pip install -r requirements.txt
```

> Si mysqlclient pose problème sur Mac : `brew install pkg-config mysql`

---

## 2. Base de données MySQL

Créez la base via phpMyAdmin ou MySQL :

```sql
CREATE DATABASE boutik CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Vérifiez que MySQL tourne sur le **port 3308**.

---

## 3. Configuration

Les paramètres sont dans `config/settings.py` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'boutik',
        'USER': 'root',
        'PASSWORD': '',      # ← Mettez votre mot de passe MySQL ici
        'HOST': '127.0.0.1',
        'PORT': '3308',
    }
}
```

---

## 4. Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Données initiales (catégories, tailles, couleurs)

```bash
python manage.py seed_data
```

---

## 6. Créer un superutilisateur (admin)

```bash
python manage.py createsuperuser
```

---

## 7. Collecter les fichiers statiques

```bash
python manage.py collectstatic
```

---

## 8. Lancer le serveur

```bash
python manage.py runserver
```

Puis ouvrir : **http://127.0.0.1:8000/**

---

## URLs du site

| URL | Description |
|-----|-------------|
| `/` | Page d'accueil |
| `/produits/` | Catalogue |
| `/categorie/<slug>/` | Catégorie |
| `/produit/<slug>/` | Fiche produit |
| `/panier/` | Panier |
| `/commande/` | Checkout |
| `/compte/` | Profil client |
| `/compte/connexion/` | Connexion |
| `/compte/inscription/` | Inscription |
| `/contact/` | Contact |
| `/a-propos/` | À propos |
| `/dashboard/` | Dashboard admin |
| `/admin/` | Django Admin |

---

## Ajouter des produits

1. Aller sur `/admin/`
2. Se connecter avec le superutilisateur
3. **Store → Produits → Ajouter un produit**
4. Remplir : nom, catégorie, prix, stock, image

---

## Structure des dossiers d'images

Placez vos images dans :
```
media/
  products/    ← images produits
  categories/  ← images catégories
  banners/     ← bannières accueil
  avatars/     ← photos profils
static/
  images/
    hero-bg.jpg        ← image hero
    placeholder.jpg    ← image par défaut
    wave-logo.png      ← logo Wave
    orange-money-logo.png  ← logo Orange Money
```

---

## Contact / Support

- **Tél :** 77 212 43 19
- **Email :** thiambusiness44@gmail.com
- **WhatsApp :** wa.me/221772124319
