"""
Commande pour créer les données initiales de ThiamStreetwear.
Usage: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from apps.store.models import Category, Size, Color


class Command(BaseCommand):
    help = 'Crée les catégories, tailles et couleurs initiales'

    def handle(self, *args, **kwargs):
        self.stdout.write('Création des données initiales ThiamStreetwear...')

        # ===== CATÉGORIES PARENTES =====
        cats_data = [
            {'name': 'Chaussures', 'order': 1},
            {'name': 'Vêtements Homme', 'order': 2},
            {'name': 'Vêtements Femme', 'order': 3},
            {'name': 'Accessoires', 'order': 4},
            {'name': 'Nouveautés', 'order': 5},
            {'name': 'Soldes', 'order': 6},
        ]
        parents = {}
        for data in cats_data:
            cat, created = Category.objects.get_or_create(
                name=data['name'],
                defaults={'order': data['order'], 'parent': None}
            )
            parents[data['name']] = cat
            status = 'créé' if created else 'existe déjà'
            self.stdout.write(f'  ✓ Catégorie "{data["name"]}" — {status}')

        # ===== SOUS-CATÉGORIES =====
        subcats = [
            ('Chaussures', [
                ('Sneakers', 1), ('Baskets', 2), ('Boots', 3), ('Sandales', 4)
            ]),
            ('Vêtements Homme', [
                ('T-shirts Homme', 1), ('Hoodies', 2), ('Pantalons', 3),
                ('Vestes Homme', 4), ('Shorts', 5)
            ]),
            ('Vêtements Femme', [
                ('Robes', 1), ('Tops', 2), ('Leggings', 3), ('Vestes Femme', 4)
            ]),
            ('Accessoires', [
                ('Casquettes', 1), ('Sacs', 2), ('Ceintures', 3), ('Chaussettes', 4)
            ]),
        ]
        for parent_name, subs in subcats:
            parent = parents.get(parent_name)
            if parent:
                for name, order in subs:
                    sub, created = Category.objects.get_or_create(
                        name=name,
                        defaults={'parent': parent, 'order': order}
                    )
                    if created:
                        self.stdout.write(f'    → Sous-catégorie "{name}" créée')

        # ===== TAILLES =====
        tailles = [
            ('XS', 1), ('S', 2), ('M', 3), ('L', 4), ('XL', 5), ('XXL', 6),
            ('36', 10), ('37', 11), ('38', 12), ('39', 13), ('40', 14),
            ('41', 15), ('42', 16), ('43', 17), ('44', 18), ('45', 19),
            ('TU', 20),  # Taille unique
        ]
        for name, order in tailles:
            Size.objects.get_or_create(name=name, defaults={'order': order})
        self.stdout.write(f'  ✓ {len(tailles)} tailles créées')

        # ===== COULEURS =====
        couleurs = [
            ('Noir', '#000000'), ('Blanc', '#FFFFFF'), ('Gris', '#808080'),
            ('Rouge', '#FF0000'), ('Bleu', '#0000FF'), ('Bleu Marine', '#001F5B'),
            ('Vert', '#008000'), ('Kaki', '#8B7355'), ('Beige', '#F5DEB3'),
            ('Marron', '#8B4513'), ('Orange', '#FFA500'), ('Jaune', '#FFD700'),
            ('Rose', '#FF69B4'), ('Violet', '#800080'), ('Bordeaux', '#800020'),
        ]
        for name, hex_code in couleurs:
            Color.objects.get_or_create(name=name, defaults={'hex_code': hex_code})
        self.stdout.write(f'  ✓ {len(couleurs)} couleurs créées')

        self.stdout.write(self.style.SUCCESS('\n✅ Données initiales créées avec succès !'))
        self.stdout.write('\nProchaines étapes :')
        self.stdout.write('  1. Aller sur /admin/ pour ajouter des produits')
        self.stdout.write('  2. Ajouter des images dans media/products/')
        self.stdout.write('  3. Créer un superutilisateur : python manage.py createsuperuser')
