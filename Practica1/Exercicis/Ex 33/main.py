def aplicarDescuento(diccionario_compra, iva):
    def calcularDescuento(precio, descuento):
        return precio - (precio * descuento / 100)

    def aplicarIva(descuento, iva):
        return descuento * (1 + iva / 100)

    def mostrar(producto, iva):
        print(f"{producto}: {iva:.2f}")

    for producto, precio in diccionario_compra.items():
        descuento = diccionario_compra[producto]
        descuento = calcularDescuento(precio, descuento)
        iva = aplicarIva(descuento, iva)
        mostrar(f"Producto {producto}", iva)

listaCompra = {100: 10, 250: 5, 1500: 30, 150: 10}
ivaUsuario = float(input("Introduce el IVA a aplicar (%): "))

aplicarDescuento(listaCompra, ivaUsuario)
