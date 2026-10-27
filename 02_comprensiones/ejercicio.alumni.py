def preparar_catalogo(productos):
    # Comprensión de lista para los nombres con precio <= 20
    disponibles = [p["nombre"] for p in productos if p["precio"] <= 20]
    
    # Comprensión de diccionario para asociar nombre -> precio
    precios = {p["nombre"]: p["precio"] for p in productos}
    
    # Comprensión de set para obtener las categorías únicas
    categorias = {p["categoria"] for p in productos}
    
    return {
        "disponibles": disponibles,
        "precios": precios,
        "categorias": categorias
    }


# Ejemplo de uso original:
productos = [
    {"nombre": "cafe", "precio": 10, "categoria": "bebida"},
    {"nombre": "torta", "precio": 25, "categoria": "postre"},
    {"nombre": "te", "precio": 8, "categoria": "bebida"},
]
print(preparar_catalogo(productos))

# TODO: añade otro ejemplo con print y su resultado esperado en un comentario.
# Otro ejemplo: catálogo con diferentes precios y categorías variadas
productos_2 = [
    {"nombre": "agua", "precio": 5, "categoria": "bebida"},
    {"nombre": "sandwich", "precio": 18, "categoria": "comida"},
    {"nombre": "helado", "precio": 22, "categoria": "postre"}
]
# Resultado esperado: {"disponibles": ["agua", "sandwich"], "precios": {"agua": 5, "sandwich": 18, "helado": 22}, "categorias": {"bebida", "comida", "postre"}}
print(preparar_catalogo(productos_2))