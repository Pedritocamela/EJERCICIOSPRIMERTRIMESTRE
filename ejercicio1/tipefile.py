#Pedro Lorenzo Pérez Briceño
import sys

def mostrar_uso():
    print("\nUso correcto: python tipefile.py <nombre_archivo>")
    print("Ejemplo: python typefile.py archivo_prueba.txt")
    print("Asegúrate de que el archivo exista en el mismo directorio o proporciona la ruta completa.\n")

if len(sys.argv) != 2:
    print("\nError: Debes proporcionar el nombre de un archivo como argumento.")
    mostrar_uso()
    sys.exit(1)

name = sys.argv[1]
try:
    with open(name, 'r', encoding="utf-8") as file:
        for num, line in enumerate(file, start=1):
            print(f"Línea {num} ({len(line)} caracteres): {line}", end='')
except FileNotFoundError:
    print(f"Error: El archivo '{name}' no existe o la ruta es incorrecta.")
    mostrar_uso()
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")
    mostrar_uso()