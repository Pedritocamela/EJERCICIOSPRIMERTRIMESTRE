import sys
import os
import random
import string

def mostrar_uso():
    print("\nuso correcto: python createpng.py <nombre_carpeta> <cantidad_archivos>")
    print("ejemplo: python createpng.py Imagenes 20")

def generar_nombre_aleatorio():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(15))

def generar_nombre_unico(carpeta, nombres_usados):
    while True:
        nombre = generar_nombre_aleatorio() + ".png"
        if nombre not in nombres_usados:
            return nombre

def crear_pngs(carpeta, cantidad):
    try:
        cantidad = int(cantidad)
        if cantidad <= 0:
            print("error: la cantidad debe ser un número positivo.")
            mostrar_uso()
            return

        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            print(f"carpeta '{carpeta}' creada.")

        nombres_usados = set()
        if os.path.exists(carpeta):
            archivos_existentes = os.listdir(carpeta)
            for archivo in archivos_existentes:
                if archivo.endswith('.png'):
                    nombres_usados.add(archivo)
            if len(nombres_usados) > 0:
                print(f"{len(nombres_usados)} archivos png existentes encontrados.")

        for i in range(cantidad):
            nombre = generar_nombre_unico(carpeta, nombres_usados)
            nombres_usados.add(nombre)
            ruta = os.path.join(carpeta, nombre)
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
