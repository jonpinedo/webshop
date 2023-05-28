import os
from django.core.files import File
from itemApp.models import Item

prendas = [
    {"nombre": "Camiseta básica", "precio": 15.99, "imagen": "camiseta_basica.jpg"},
    {"nombre": "Pantalones vaqueros", "precio": 39.99, "imagen": "pantalon_vaquero.jpg"},
    {"nombre": "Vestido de fiesta", "precio": 89.99, "imagen": "vestido_fiesta.jpg"},
    {"nombre": "Jersey de lana", "precio": 49.99, "imagen": "jersey_lana.jpg"},
    {"nombre": "Falda plisada", "precio": 29.99, "imagen": "falda_plisada.jpg"},
    {"nombre": "Camiseta tirantes", "precio": 15.99, "imagen": "camiseta_tirantes.jpg"},
    {"nombre": "Pantalones de lino", "precio": 39.99, "imagen": "pantalon_lino.jpg"},
    {"nombre": "Vestido de gala", "precio": 89.99, "imagen": "vestido_gala.jpeg"},
    {"nombre": "Sudadera con capucha", "precio": 49.99, "imagen": "sudadera_capucha.jpg"},
    {"nombre": "Falda vaquera", "precio": 29.99, "imagen": "falda_vaquera.jpg"},
    # Agrega más prendas según tus necesidades
]

for i, prenda_data in enumerate(prendas, start=1):
    imagen_path = os.path.join("itemApp", "static", "images", "items", prenda_data["imagen"])
    with open(imagen_path, "rb") as f:
        prenda = Item(
            item_id=i,
            item_name=prenda_data["nombre"],
            item_price=prenda_data["precio"],
            item_image=File(f, name=prenda_data["imagen"])
        )
        prenda.save()
