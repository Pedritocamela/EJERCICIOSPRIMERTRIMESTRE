# Pedro Lorenzo Pérez Briceño
# Programa para leer y mostrar el contenido de un archivo línea por línea con su número y cantidad de caracteres

import sys

def mostrar_uso():
    """muestra el uso correcto del programa"""
    print("\nuso correcto: python tipefile.py <nombre_archivo>")
    print("ejemplo: python tipefile.py archivo_prueba.txt")
    print("asegurate de que el archivo exista en el mismo directorio o proporciona la ruta completa.\n")

# verifica que se pase el argumento requerido
if len(sys.argv) != 2:
    print("\nerror: debes proporcionar el nombre de un archivo como argumento.")
    mostrar_uso()
    sys.exit(1)

# obtiene el nombre del archivo del argumento
name = sys.argv[1]

try:
    # abre el archivo en modo lectura con codificación utf-8
    with open(name, 'r', encoding="utf-8") as file:
        # itera sobre cada línea del archivo
        for num, line in enumerate(file, start=1):
            # muestra el número de línea, cantidad de caracteres y el contenido
            print(f"línea {num} ({len(line)} caracteres): {line}", end='')
except FileNotFoundError:
    print(f"error: el archivo '{name}' no existe o la ruta es incorrecta.")
    mostrar_uso()
except Exception as e:
    print(f"ocurrió un error al leer el archivo: {e}")
    mostrar_uso()