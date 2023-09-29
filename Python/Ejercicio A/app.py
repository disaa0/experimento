import os
from funciones import mostrar_datos_clases, mostrar_datos_zoo, listar_x_caracteristica, listar_x_clase

datos_clases = mostrar_datos_clases('Python/Ejercicio A/clases.csv')
datos_animales = mostrar_datos_zoo('Python/Ejercicio A/zoo.csv')

while True:
    print("Opciones:")
    print("1. Listar animal por su clase")
    print("2. Listar animal por su característica")
    print("3. Exit")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        clase_id = int(input("Ingrese el ID de la clase a listar: "))
        if clase_id in datos_clases:
            clase_tipo = datos_clases.get(clase_id)
            animales = listar_x_clase(datos_animales, clase_id)
            print(f"Animales de la clase '{clase_tipo}':")
            for animal in animales:
                print(f"Nombre: {animal['nombre_animal']}")
        else:
            print("404 not found, intente de nuevo.")

    elif opcion == '2':
        caracteristica = input("Ingrese el nombre o parte del nombre del animal a buscar: ")
        animales = listar_x_caracteristica(datos_animales, caracteristica)
        print(f"Resultados de la búsqueda '{caracteristica}':")
        for animal in animales:
            print(f"Nombre: {animal['nombre_animal']}")

    elif opcion == '3':
        print("Exit")
        break

    else:
        print("404 not found, intentelo de nuevo.")

