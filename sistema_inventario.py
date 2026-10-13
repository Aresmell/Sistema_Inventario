#Sistema básico de inventario con programación orientada a objetos

import math

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un texto.")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        self.nombre = nombre.strip()
        self.actualizar_precio(precio)
        self.actualizar_cantidad(cantidad)

    def actualizar_precio(self, nuevo_precio):
        # También se aceptan enteros, pero no valores booleanos.
        if isinstance(nuevo_precio, bool) or not isinstance(nuevo_precio, (int, float)):
            raise TypeError("El precio debe ser un número.")
        if not math.isfinite(nuevo_precio) or nuevo_precio < 0:
            raise ValueError("El precio debe ser un número finito mayor o igual a cero.")
        self.precio = float(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad):
        if isinstance(nueva_cantidad, bool) or not isinstance(nueva_cantidad, int):
            raise TypeError("La cantidad debe ser un número entero.")
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return (
            f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | "
            f"Cantidad: {self.cantidad} | Total: ${self.calcular_valor_total():.2f}"
        )


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de la clase Producto.")
        if self.buscar_producto(producto.nombre) is not None:
            raise ValueError("Ya existe un producto con ese nombre. Puedes buscarlo y actualizarlo.")
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("El nombre de búsqueda debe ser un texto.")
        if not nombre.strip():
            raise ValueError("Escribe el nombre del producto que deseas buscar.")

        for producto in self.productos:
            if producto.nombre.casefold() == nombre.strip().casefold():
                return producto
        return None

    def calcular_valor_inventario(self):
        total = 0.0
        for producto in self.productos:
            total += producto.calcular_valor_total()
        return total

    def listar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- PRODUCTOS REGISTRADOS ---")
            for producto in self.productos:
                print(producto)


def menu_principal(inventario):
    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        opcion = input("Selecciona una opción: ").strip()

        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio unitario (ejemplo: 2.50): "))
                cantidad = int(input("Cantidad de unidades: "))

                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                print("Producto agregado correctamente.")

            elif opcion == "2":
                nombre = input("Nombre del producto que deseas buscar: ")
                producto = inventario.buscar_producto(nombre)

                # La búsqueda devuelve None; el menú maneja el caso como error.
                if producto is None:
                    raise LookupError("No se encontró un producto con ese nombre.")

                print(producto)
                print("\n1. Actualizar precio")
                print("2. Actualizar cantidad")
                print("3. Volver al menú principal")
                cambio = input("Selecciona una opción: ").strip()

                if cambio == "1":
                    precio = float(input("Nuevo precio: "))
                    producto.actualizar_precio(precio)
                    print("Precio actualizado correctamente.")
                    print(producto)
                elif cambio == "2":
                    cantidad = int(input("Nueva cantidad: "))
                    producto.actualizar_cantidad(cantidad)
                    print("Cantidad actualizada correctamente.")
                    print(producto)
                elif cambio != "3":
                    print("Opción inválida. Se vuelve al menú principal.")

            elif opcion == "3":
                inventario.listar_productos()

            elif opcion == "4":
                total = inventario.calcular_valor_inventario()
                print(f"Valor total del inventario: ${total:.2f}")

            elif opcion == "5":
                print("Gracias por usar el sistema. ¡Hasta pronto!")
                break

            else:
                print("Opción inválida. Selecciona un número del 1 al 5.")

        except ValueError as error:
            print(f"Dato inválido: {error}")
            print("Usa números para el precio y enteros para la cantidad.")
        except TypeError as error:
            print(f"Tipo de dato incorrecto: {error}")
        except LookupError as error:
            print(error)


if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)
