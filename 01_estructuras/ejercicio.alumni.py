def resumir_ventas(ventas):
    productos = set()
    unidades = 0
    por_producto = {}
    
    for producto, cantidad in ventas:
        productos.add(producto)
        unidades += cantidad
        por_producto[producto] = por_producto.get(producto, 0) + cantidad
        
    return {
        "productos": productos,
        "unidades": unidades,
        "por_producto": por_producto
    }


# Ejemplo:
ventas = [("cafe", 2), ("te", 1), ("cafe", 3)]
print(resumir_ventas(ventas))

# Otro ejemplo: lista con diferentes productos y cantidades variadas
ventas_2 = [("pan", 4), ("leche", 2), ("pan", 1), ("huevos", 12)]

print(resumir_ventas(ventas_2))