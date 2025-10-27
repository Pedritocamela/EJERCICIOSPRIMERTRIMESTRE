# Pedro Lorenzo Pérez Briceño
# programa para buscar y contar ocurrencias de una cadena en un archivo

import sys

def mostrar_uso():
    """muestra el uso correcto del programa"""
    print("\nuso correcto: python buscarcoincidencia.py <nombre_archivo> <cadena_a_buscar>")
    print("ejemplo: python buscarcoincidencia.py hola.txt hola")
    print("asegurate de que el archivo exista y que proporciones ambos argumentos.\n")

def encontrar_archivo(nombre_archivo, cadena):
    """busca y cuenta las ocurrencias de una cadena en el archivo especificado"""
    try:
        # abre el archivo en modo lectura con codificación utf-8
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            # cuenta cuántas veces aparece la cadena en el contenido
            ocurrencia = contenido.count(cadena)
            print(f"'{cadena}': {ocurrencia}")
    except FileNotFoundError:
        print(f"error: el archivo '{nombre_archivo}' no existe o la ruta es incorrecta.")
        mostrar_uso()
    except Exception as e:
        print(f"ocurrio un error al leer el archivo: {e}")
        mostrar_uso()

# punto de entrada del programa
if __name__ == "__main__":
    # verifica que se pasen los dos argumentos requeridos
    if len(sys.argv) != 3:
        print("error: debes proporcionar el nombre de un archivo y la cadena a buscar como argumentos.")
        mostrar_uso()
    else:
        # obtiene los argumentos de la línea de comandos
        archivo = sys.argv[1]
        texto = sys.argv[2]
        encontrar_archivo(archivo, texto)