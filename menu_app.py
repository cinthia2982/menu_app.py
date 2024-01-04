def agregar_compra(compras):
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = float(input("Ingrese el precio del producto: "))

    compra = {'producto': nombre_producto, 'precio': precio_producto}
    compras.append(compra)
    print(f"Compra de {nombre_producto} agregada correctamente.\n")


def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Lista de compras:")
        for idx, compra in enumerate(compras, 1):
            print(f"{idx}. Producto: {compra['producto']}, Precio: ${compra['precio']}")
        print()


def mostrar_total(compras):
    total = sum(compra['precio'] for compra in compras)
    print(f"Total gastado: ${total:,.2f}\n")


def main():
    compras = []

    while True:
        print("Menú Principal:")
        print("1. Agregar Compra")
        print("2. Mostrar Compras")
        print("3. Mostrar Total Gastado")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            agregar_compra(compras)
        elif opcion == '2':
            mostrar_compras(compras)
        elif opcion == '3':
            mostrar_total(compras)
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.\n")


if __name__ == "__main__":
    main()
