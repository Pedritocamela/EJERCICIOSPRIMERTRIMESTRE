# pedro lorenzo pérez briceño
# programa para crear múltiples archivos png con nombres aleatorios

import sys
import os
import random
import string

def mostrar_uso():
    """muestra el uso correcto del programa"""
    print("\nuso correcto: python createpng.py <nombre_carpeta> <cantidad_archivos>")
    print("ejemplo: python createpng.py imagenes 20")

def generar_nombre_aleatorio():
    """genera un nombre aleatorio de 15 caracteres usando letras y números"""
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(15))

def generar_nombre_unico(carpeta, nombres_usados):
    """genera un nombre único que no se haya usado anteriormente"""
    while True:
        nombre = generar_nombre_aleatorio() + ".png"
        ruta = os.path.join(carpeta, nombre)
        # verifica que el nombre no esté repetido
        if nombre not in nombres_usados:
            return nombre

def crear_pngs(carpeta, cantidad):
    """crea la cantidad especificada de archivos png en la carpeta indicada"""
    try:
        # convierte la cantidad a entero
        cantidad = int(cantidad)
        if cantidad <= 0:
            print("error: la cantidad debe ser un número positivo.")
            mostrar_uso()
            return

        # crea la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            print(f"carpeta '{carpeta}' creada.")

        # set para evitar nombres duplicados
        nombres_usados = set()

        # crea cada archivo png
        for i in range(cantidad):
            nombre = generar_nombre_unico(carpeta, nombres_usados)
            nombres_usados.add(nombre)
            ruta = os.path.join(carpeta, nombre)
            # crea el archivo vacío
            with open(ruta, 'w') as file:
                pass

        print(f"{cantidad} archivos png creados exitosamente.")

    except ValueError:
        print("error: la cantidad debe ser un número entero válido.")
        mostrar_uso()
    except PermissionError:
        print("error: no tienes permisos para crear archivos.")
        mostrar_uso()
    except Exception as e:
        print(f"error inesperado: {e}")
        mostrar_uso()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("\nerror: debes proporcionar el nombre de la carpeta y la cantidad de archivos.")
        mostrar_uso()
        sys.exit(1)

    crear_pngs(sys.argv[1], sys.argv[2])
