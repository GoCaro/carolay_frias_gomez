import json
import os

# Verificar existencia de archivos JSON y crearlos si no existen
if not os.path.exists("autores.json"):
    with open("autores.json", "w") as f:
        json.dump([], f)

if not os.path.exists("libros.json"):
    with open("libros.json", "w") as f:
        json.dump([], f)

# Función para agregar un nuevo autor
def agregar_autor():
    nombre = input("Ingrese el nombre del autor: ")
    nacionalidad = input("Ingrese la nacionalidad del autor: ")

    autor = {
        "nombre": nombre,
        "nacionalidad": nacionalidad
    }

    with open("autores.json", "r+") as f:
        data = json.load(f)
        data.append(autor)
        f.seek(0)
        json.dump(data, f, indent=4)

    print(f"\n✅ Autor '{nombre}' agregado con éxito.\n")

# Función para agregar un nuevo libro
def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    genero = input("Ingrese el género del libro: ")
    anio = input("Ingrese el año de publicación del libro: ")
    autor = input("Ingrese el nombre del autor: ")

    libro = {
        "titulo": titulo,
        "genero": genero,
        "anio_publicacion": anio,
        "autor": autor
    }

    with open("libros.json", "r+") as f:
        data = json.load(f)
        data.append(libro)
        f.seek(0)
        json.dump(data, f, indent=4)

    print(f"\n📚 Libro '{titulo}' agregado con éxito.\n")

# Función para mostrar la información almacenada
def mostrar_informacion():
    print("\n📖 Lista de Autores:")
    with open("autores.json", "r") as f:
        autores = json.load(f)
        for autor in autores:
            print(f"- {autor['nombre']} ({autor['nacionalidad']})")

    print("\n📚 Lista de Libros:")
    with open("libros.json", "r") as f:
        libros = json.load(f)
        for libro in libros:
            print(f"- {libro['titulo']} ({libro['genero']}, {libro['anio_publicacion']}) - Autor: {libro['autor']}")
    print()

# Menú principal
def menu():
    while True:
        print("=== SISTEMA DE GESTIÓN DE LIBROS Y AUTORES ===")
        print("1. Agregar autor")
        print("2. Agregar libro")
        print("3. Mostrar información")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            agregar_autor()
        elif opcion == "2":
            agregar_libro()
        elif opcion == "3":
            mostrar_informacion()
        elif opcion == "4":
            print("\n👋 Saliendo del sistema. ¡Hasta pronto!\n")
            break
        else:
            print("\n❌ Opción no válida. Intente de nuevo.\n")

# Ejecutar el menú
if __name__ == "__main__":
    menu()