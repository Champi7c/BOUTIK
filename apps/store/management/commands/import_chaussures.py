"""
Management command : importe tous les produits du dossier produits_chaussures/
dans la categorie Sneakers et copie les images dans media/products/.

Usage : python manage.py import_chaussures
"""

import os
import shutil
from pathlib import Path

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from apps.store.models import Category, Product, Size


DOSSIER_SOURCE = Path(__file__).resolve().parents[4] / 'produits_chaussures'
MEDIA_PRODUCTS = Path(__file__).resolve().parents[4] / 'media' / 'products'

# Tailles sneakers par defaut
TAILLES_SNEAKERS = ['39', '40', '41', '42', '43', '44', '45']

# Prix par defaut (FCFA)
PRIX_DEFAUT = 25000


class Command(BaseCommand):
    help = 'Importe les chaussures depuis produits_chaussures/ dans la BDD'

    def handle(self, *args, **options):
        MEDIA_PRODUCTS.mkdir(parents=True, exist_ok=True)

        # --- Categorie parente : Chaussures ---
        parent, _ = Category.objects.get_or_create(
            slug='chaussures',
            defaults={'name': 'Chaussures', 'order': 1}
        )

        # --- Sous-categorie : Sneakers (slug = 'sneakers') ---
        sneakers_cat, created = Category.objects.get_or_create(
            slug='sneakers',
            defaults={
                'name': 'Sneakers',
                'parent': parent,
                'order': 1,
            }
        )
        if not created:
            sneakers_cat.parent = parent
            sneakers_cat.save()
        self.stdout.write(self.style.SUCCESS(f'Categorie : {sneakers_cat.name} (slug={sneakers_cat.slug})'))

        # --- Tailles ---
        tailles = []
        for t in TAILLES_SNEAKERS:
            size, _ = Size.objects.get_or_create(name=t, defaults={'order': int(t)})
            tailles.append(size)

        # --- Parcours des dossiers ---
        dossiers = sorted(
            [d for d in DOSSIER_SOURCE.iterdir() if d.is_dir() and d.name.startswith('CHAUSSURES')],
            key=lambda d: int(''.join(filter(str.isdigit, d.name)) or 0)
        )

        imported = 0
        skipped  = 0

        for dossier in dossiers:
            num = ''.join(filter(str.isdigit, dossier.name))
            nom = f'Sneakers N\u00b0{num}'

            # Eviter les doublons
            if Product.objects.filter(name=nom).exists():
                self.stdout.write(f'  [SKIP] {nom} existe deja')
                skipped += 1
                continue

            # Photos triees par nom
            photos = sorted([
                f for f in dossier.iterdir()
                if f.suffix.lower() in ('.jpg', '.jpeg', '.png', '.webp')
            ])

            if not photos:
                self.stdout.write(self.style.WARNING(f'  [WARN] {dossier.name} : aucune photo'))
                continue

            # Copie des images dans media/products/
            images_db = []
            for photo in photos[:3]:  # max 3 (image, image2, image3)
                dest_name = f'sneakers_{num}_{photo.name}'
                dest_path = MEDIA_PRODUCTS / dest_name
                shutil.copy2(photo, dest_path)
                images_db.append(f'products/{dest_name}')

            # Creation du produit
            product = Product(
                name=nom,
                category=sneakers_cat,
                description=(
                    f'Sneakers de qualite premium, reference {dossier.name}. '
                    f'Disponible en plusieurs tailles. Livraison sur Dakar.'
                ),
                price=PRIX_DEFAUT,
                stock=10,
                image=images_db[0],
                is_new=True,
                is_featured=(int(num) <= 5),
                is_active=True,
            )
            if len(images_db) >= 2:
                product.image2 = images_db[1]
            if len(images_db) >= 3:
                product.image3 = images_db[2]

            product.save()
            product.sizes.set(tailles)

            imported += 1
            self.stdout.write(
                self.style.SUCCESS(f'  [OK] {nom} — {len(images_db)} photo(s)')
            )

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(
            f'Termine : {imported} produits importes, {skipped} deja existants.'
        ))
        self.stdout.write(
            f'Acces : http://127.0.0.1:8000/categorie/sneakers/'
        )
