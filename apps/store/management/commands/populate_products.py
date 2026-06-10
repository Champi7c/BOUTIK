"""
Commande : python manage.py populate_products
Remplit toutes les catégories vides avec des produits en réutilisant
les images déjà présentes dans /img/.
"""
import os, shutil, random
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.store.models import Category, Product, Size, Color

SRC = '/Library/AKOA/BOUTIK/img'
DEST = os.path.join(settings.MEDIA_ROOT, 'products')

def cp(src_name, dest_name=None):
    """Copie une image source vers media/products/ et retourne le chemin relatif."""
    dest_name = dest_name or src_name
    src  = os.path.join(SRC, src_name)
    dst  = os.path.join(DEST, dest_name)
    if os.path.exists(src) and not os.path.exists(dst):
        shutil.copy2(src, dst)
    return f'products/{dest_name}'

def cat(name):
    return Category.objects.get(name=name)

def sizes(*names):
    return list(Size.objects.filter(name__in=names))

def colors(*names):
    return list(Color.objects.filter(name__in=names))

class Command(BaseCommand):
    help = 'Remplit toutes les catégories avec des produits'

    def handle(self, *args, **options):
        os.makedirs(DEST, exist_ok=True)

        PRODUITS = [
            # ── BASKETS ──────────────────────────────────────────────────────
            dict(name='Jordan Street Low', category=cat('Baskets'), price=42000,
                 discount_price=35000, image=cp(' -2.jpg','basket1.jpg'),
                 sizes=sizes('38','39','40','41','42','43'), colors=colors('Noir','Blanc'),
                 is_new=True, is_featured=True, stock=15, sales_count=22),
            dict(name='Air Force One Classic', category=cat('Baskets'), price=38000,
                 image=cp(' -3.jpg','basket2.jpg'),
                 sizes=sizes('39','40','41','42','43','44'), colors=colors('Blanc','Noir'),
                 is_new=False, is_featured=True, stock=20, sales_count=41),
            dict(name='Street Runner Pro', category=cat('Baskets'), price=29500,
                 image=cp(' -4.jpg','basket3.jpg'),
                 sizes=sizes('38','39','40','41','42'), colors=colors('Gris','Noir'),
                 is_new=True, stock=10, sales_count=8),
            dict(name='Classic Low Top', category=cat('Baskets'), price=25000,
                 image=cp('-15.jpg','basket4.jpg'),
                 sizes=sizes('39','40','41','42','43'), colors=colors('Blanc','Bleu'),
                 is_new=False, stock=18, sales_count=15),

            # ── BOOTS ────────────────────────────────────────────────────────
            dict(name='Urban Boots Dakar', category=cat('Boots'), price=55000,
                 image=cp('shoes.jpg','boot1.jpg'),
                 sizes=sizes('39','40','41','42','43','44'), colors=colors('Noir','Marron'),
                 is_new=True, is_featured=True, stock=8, sales_count=12),
            dict(name='Desert Boot Sable', category=cat('Boots'), price=48000,
                 discount_price=40000, image=cp(' -10.jpg','boot2.jpg'),
                 sizes=sizes('40','41','42','43'), colors=colors('Beige','Marron'),
                 is_new=False, stock=12, sales_count=6),
            dict(name='Chelsea Boot Noir', category=cat('Boots'), price=52000,
                 image=cp(' -15.jpg','boot3.jpg'),
                 sizes=sizes('39','40','41','42','43','44'), colors=colors('Noir'),
                 is_new=True, stock=6, sales_count=9),

            # ── SANDALES ─────────────────────────────────────────────────────
            dict(name='Slides Street Noir', category=cat('Sandales'), price=12000,
                 image=cp(' -3.jpg','sandal1.jpg'),
                 sizes=sizes('38','39','40','41','42','43','44'), colors=colors('Noir','Blanc'),
                 is_new=True, stock=30, sales_count=45),
            dict(name='Claquettes Logo TSW', category=cat('Sandales'), price=9500,
                 discount_price=7500, image=cp(' -4.jpg','sandal2.jpg'),
                 sizes=sizes('38','39','40','41','42','43'), colors=colors('Noir','Gris'),
                 is_new=False, is_featured=True, stock=25, sales_count=38),
            dict(name='Sandales Sport Dakar', category=cat('Sandales'), price=15000,
                 image=cp(' -2.jpg','sandal3.jpg'),
                 sizes=sizes('39','40','41','42'), colors=colors('Bleu','Noir'),
                 is_new=True, stock=14, sales_count=7),

            # ── HOODIES ──────────────────────────────────────────────────────
            dict(name='Hoodie TSW Oversize', category=cat('Hoodies'), price=28000,
                 image=cp('shirt6.jpg','hoodie1.jpg'),
                 sizes=sizes('S','M','L','XL','XXL'), colors=colors('Noir','Gris'),
                 is_new=True, is_featured=True, stock=20, sales_count=33),
            dict(name='Sweat Zippé Urban', category=cat('Hoodies'), price=32000,
                 discount_price=26000, image=cp('shirt7.jpg','hoodie2.jpg'),
                 sizes=sizes('S','M','L','XL'), colors=colors('Noir','Bleu Marine'),
                 is_new=False, stock=15, sales_count=18),
            dict(name='Hoodie Brodé Gold', category=cat('Hoodies'), price=35000,
                 image=cp('shirt8.jpg','hoodie3.jpg'),
                 sizes=sizes('M','L','XL','XXL'), colors=colors('Noir'),
                 is_new=True, stock=10, sales_count=11),
            dict(name='Pull Streetwear Logo', category=cat('Hoodies'), price=24000,
                 image=cp('shirt9.jpg','hoodie4.jpg'),
                 sizes=sizes('S','M','L','XL'), colors=colors('Gris','Beige'),
                 is_new=False, stock=22, sales_count=14),
            dict(name='Sweat Capuche Oversize', category=cat('Hoodies'), price=30000,
                 image=cp('shirt10.jpg','hoodie5.jpg'),
                 sizes=sizes('S','M','L','XL','XXL'), colors=colors('Kaki','Noir'),
                 is_new=True, stock=8, sales_count=5),

            # ── VESTES HOMME ─────────────────────────────────────────────────
            dict(name='Veste Coach Noir', category=cat('Vestes Homme'), price=45000,
                 image=cp('shirt11.jpg','veste_h1.jpg'),
                 sizes=sizes('S','M','L','XL'), colors=colors('Noir'),
                 is_new=True, is_featured=True, stock=12, sales_count=17),
            dict(name='Bomber Urban TSW', category=cat('Vestes Homme'), price=52000,
                 discount_price=44000, image=cp('shirt12.jpg','veste_h2.jpg'),
                 sizes=sizes('M','L','XL','XXL'), colors=colors('Noir','Kaki'),
                 is_new=False, stock=8, sales_count=24),
            dict(name='Veste Denim Streetwear', category=cat('Vestes Homme'), price=38000,
                 image=cp('shirt13.jpg','veste_h3.jpg'),
                 sizes=sizes('S','M','L','XL'), colors=colors('Bleu','Noir'),
                 is_new=True, stock=10, sales_count=9),
            dict(name='Jacket Militaire Kaki', category=cat('Vestes Homme'), price=48000,
                 image=cp('shirt14.jpg','veste_h4.jpg'),
                 sizes=sizes('M','L','XL'), colors=colors('Kaki','Vert'),
                 is_new=False, stock=6, sales_count=13),

            # ── SHORTS ───────────────────────────────────────────────────────
            dict(name='Short Cargo Noir', category=cat('Shorts'), price=16500,
                 image=cp('pants2.jpg','short1.jpg'),
                 sizes=sizes('S','M','L','XL'), colors=colors('Noir','Kaki'),
                 is_new=True, is_featured=True, stock=25, sales_count=29),
            dict(name='Short Sport TSW', category=cat('Shorts'), price=12000,
                 discount_price=9500, image=cp('pants3.jpg','short2.jpg'),
                 sizes=sizes('S','M','L','XL','XXL'), colors=colors('Noir','Gris','Bleu'),
                 is_new=False, stock=30, sales_count=42),
            dict(name='Bermuda Streetwear', category=cat('Shorts'), price=14000,
                 image=cp('pants4.jpg','short3.jpg'),
                 sizes=sizes('M','L','XL'), colors=colors('Beige','Kaki'),
                 is_new=True, stock=18, sales_count=11),
            dict(name='Short Jogging Urban', category=cat('Shorts'), price=11000,
                 image=cp('pants5.jpg','short4.jpg'),
                 sizes=sizes('S','M','L','XL','XXL'), colors=colors('Noir','Rouge'),
                 is_new=False, stock=22, sales_count=16),

            # ── ROBES ────────────────────────────────────────────────────────
            dict(name='Robe Streetwear Femme', category=cat('Robes'), price=22000,
                 image=cp('shirt1.jpg','robe1.jpg'),
                 sizes=sizes('XS','S','M','L'), colors=colors('Noir','Blanc'),
                 is_new=True, is_featured=True, stock=14, sales_count=19),
            dict(name='Robe Mini Urban', category=cat('Robes'), price=18500,
                 discount_price=15000, image=cp('shirt2.jpg','robe2.jpg'),
                 sizes=sizes('XS','S','M','L'), colors=colors('Noir','Rouge'),
                 is_new=False, stock=10, sales_count=23),
            dict(name='Robe Longue Sport Chic', category=cat('Robes'), price=26000,
                 image=cp('shirt3.jpg','robe3.jpg'),
                 sizes=sizes('S','M','L','XL'), colors=colors('Gris','Blanc'),
                 is_new=True, stock=8, sales_count=7),

            # ── TOPS FEMME ───────────────────────────────────────────────────
            dict(name='Crop Top TSW Gold', category=cat('Tops'), price=9500,
                 image=cp('shirt4.jpg','top1.jpg'),
                 sizes=sizes('XS','S','M','L'), colors=colors('Noir','Blanc'),
                 is_new=True, is_featured=True, stock=20, sales_count=35),
            dict(name='Top Oversize Femme', category=cat('Tops'), price=13000,
                 image=cp('shirt5.jpg','top2.jpg'),
                 sizes=sizes('XS','S','M','L','XL'), colors=colors('Noir','Gris','Beige'),
                 is_new=False, stock=18, sales_count=27),
            dict(name='Brassière Sport Urbaine', category=cat('Tops'), price=11000,
                 discount_price=8500, image=cp('shirt15.jpg','top3.jpg'),
                 sizes=sizes('XS','S','M','L'), colors=colors('Noir','Rose'),
                 is_new=True, stock=15, sales_count=21),
            dict(name='Top Crop Brodé', category=cat('Tops'), price=14500,
                 image=cp('shirt16.jpg','top4.jpg'),
                 sizes=sizes('XS','S','M'), colors=colors('Blanc','Beige'),
                 is_new=True, stock=12, sales_count=9),

            # ── LEGGINGS ─────────────────────────────────────────────────────
            dict(name='Legging Sport Noir', category=cat('Leggings'), price=14000,
                 image=cp('pants6.jpg','legging1.jpg'),
                 sizes=sizes('XS','S','M','L','XL'), colors=colors('Noir'),
                 is_new=True, is_featured=True, stock=20, sales_count=31),
            dict(name='Legging Streetwear', category=cat('Leggings'), price=16500,
                 image=cp('pants7.jpg','legging2.jpg'),
                 sizes=sizes('XS','S','M','L'), colors=colors('Noir','Gris','Rouge'),
                 is_new=False, stock=15, sales_count=18),
            dict(name='Legging Taille Haute', category=cat('Leggings'), price=18000,
                 discount_price=14000, image=cp('pants8.jpg','legging3.jpg'),
                 sizes=sizes('XS','S','M','L','XL'), colors=colors('Noir','Bordeaux'),
                 is_new=True, stock=12, sales_count=14),
            dict(name='Legging Sport Urban', category=cat('Leggings'), price=12500,
                 image=cp('pants9.jpg','legging4.jpg'),
                 sizes=sizes('XS','S','M','L'), colors=colors('Noir','Violet'),
                 is_new=False, stock=18, sales_count=9),

            # ── VESTES FEMME ─────────────────────────────────────────────────
            dict(name='Bomber Femme Rose', category=cat('Vestes Femme'), price=42000,
                 image=cp('shirt15.jpg','veste_f1.jpg'),
                 sizes=sizes('XS','S','M','L'), colors=colors('Rose','Noir'),
                 is_new=True, is_featured=True, stock=8, sales_count=14),
            dict(name='Veste Denim Femme', category=cat('Vestes Femme'), price=36000,
                 discount_price=30000, image=cp('shirt16.jpg','veste_f2.jpg'),
                 sizes=sizes('XS','S','M','L'), colors=colors('Bleu','Noir'),
                 is_new=False, stock=10, sales_count=11),
            dict(name='Crop Jacket TSW', category=cat('Vestes Femme'), price=38000,
                 image=cp('shirt17.jpg','veste_f3.jpg'),
                 sizes=sizes('XS','S','M','L'), colors=colors('Noir','Bordeaux'),
                 is_new=True, stock=6, sales_count=8),

            # ── SACS ─────────────────────────────────────────────────────────
            dict(name='Sac à Dos Urban TSW', category=cat('Sacs'), price=25000,
                 image=cp('beanie.jpg','sac1.jpg'),
                 sizes=sizes('TU',), colors=colors('Noir','Gris'),
                 is_new=True, is_featured=True, stock=15, sales_count=22),
            dict(name='Tote Bag Streetwear', category=cat('Sacs'), price=8500,
                 image=cp('beanie2.jpg','sac2.jpg'),
                 sizes=sizes('TU',), colors=colors('Noir','Blanc','Beige'),
                 is_new=False, stock=30, sales_count=47),
            dict(name='Sacoche Waist Bag', category=cat('Sacs'), price=18000,
                 discount_price=14000, image=cp('beanie3.jpg','sac3.jpg'),
                 sizes=sizes('TU',), colors=colors('Noir','Kaki'),
                 is_new=True, stock=20, sales_count=19),
        ]

        created = 0
        skipped = 0
        for p in PRODUITS:
            szs   = p.pop('sizes', [])
            clrs  = p.pop('colors', [])
            slug  = p['name'].lower().replace(' ', '-').replace("'", '').replace('é','e').replace('è','e').replace('ê','e').replace('à','a').replace('ç','c')

            # Évite les doublons
            if Product.objects.filter(name=p['name']).exists():
                skipped += 1
                continue

            prod = Product.objects.create(
                slug=slug,
                description=f"{p['name']} — Collection Bright Looks. Style urbain authentique pour les rues de Dakar.",
                is_active=True,
                **p
            )
            prod.sizes.set(szs)
            prod.colors.set(clrs)
            created += 1

        self.stdout.write(self.style.SUCCESS(
            f'✅ {created} produits créés, {skipped} ignorés (déjà existants).'
        ))
