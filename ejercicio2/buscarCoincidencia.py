#Pedro Lorenzo Pérez Briceño
import sys

def mostrar_uso():
    print("\nuso correcto: python buscarCoincidencia.py <nombre_archivo> <cadena_a_buscar>")
    print("ejemplo: python buscarCoincidencia.py hola.txt hola")
    print("asegurate de que el archivo exista y que proporciones ambos argumentos.\n")

def encontrar_archivo(nombre_archivo, cadena):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            ocurrencia = contenido.count(cadena)
            print(f"'{cadena}': {ocurrencia}")
    except FileNotFoundError:
        print(f"error: el archivo '{nombre_archivo}' no existe o la ruta es incorrecta.")
        mostrar_uso()
    except Exception as e:
        print(f"ocurrio un error al leer el archivo: {e}")
        mostrar_uso()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("error: debes proporcionar el nombre de un archivo y la cadena a buscar como argumentos.")
        mostrar_uso()
    else:
        archivo = sys.argv[1]
        texto = sys.argv[2]
        encontrar_archivo(archivo, texto)