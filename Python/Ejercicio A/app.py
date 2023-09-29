import os
from funciones import info_zoo, info_clases, guardar_datos, listaclases, info_caracteristicas

# Cargar datos iniciales desde archivos CSV
datos_clases = info_clases('Python/Ejercicio A/clases.csv')
datos_animales = info_zoo('Python/Ejercicio A/zoo.csv')

while True:
    print("menú, seleccione la opción:")
    print("a. lista por clsase")
    print("b. listar por característica")
    print("c. agregar animal")
    print("d. salir")
    opcion = input("seleccione una opción: ")



    if opcion == 'a':
        clase_id = int(input("ingrese el id de la clase a listar: "))
        if clase_id in datos_clases:
            clase_tipo = datos_clases.get(clase_id)
            animales = listaclases(datos_animales, clase_id)
            print(f"Animales de la clase '{clase_tipo}':")
            for animal in animales:
                print(f"Nombre: {animal['nombre_animal']}")
        else:
            print("no se encuentra la clase.")

    elif opcion == 'b':
        caracteristica = input("ingrese parte del nombre del animal a buscar: ")
        animales = info_caracteristicas(datos_animales, caracteristica)
        print(f"Resultados de '{caracteristica}':")
        for animal in animales:
            print(f"Nombre: {animal['nombre_animal']}")

    elif opcion == 'c':
        nombre = input("ingrese   nombre del animal: ")
        clase_id = int(input("ingrese el ID de la clase del animal: "))
        
        nuevo_animal = {
            'nombre_animal': nombre,
            'pelo': 1 if input("¿Posee pelo? (1/0): ") == '1' else 0,
            'plumas': 1 if input("¿Tiene plumas? (1/0): ") == '1' else 0,
            'huevos': 1 if input("¿Pone huevos? (1/0): ") == '1' else 0,
            'leche': 1 if input("¿Da leche? (1/0): ") == '1' else 0,
            'vuela': 1 if input("¿Vuela? (1/0): ") == '1' else 0,
            'acuatico': 1 if input("¿Es acuático? (1/0): ") == '1' else 0,
            'depredador': 1 if input("¿Es depredador? (1/0): ") == '1' else 0,
            'dientes': 1 if input("¿Tiene dientes? (1/0): ") == '1' else 0,
            'espinazo': 1 if input("¿Tiene espinazo? (1/0): ") == '1' else 0,
            'respira': 1 if input("¿Respira? (1/0): ") == '1' else 0,
            'venenoso': 1 if input("¿Es venenoso? (1/0): ") == '1' else 0,
            'aletas': 1 if input("¿Tiene aletas? (1/0): ") == '1' else 0,
            'patas': int(input("Número de patas: ")),
            'cola': 1 if input("¿Tiene cola? (1/0): ") == '1' else 0,
            'domestico': 1 if input("¿Es doméstico? (1/0): ") == '1' else 0,
            'tamanio_gato': 1 if input("¿Es gato? (1/0): ") == '1' else 0,
            'clase': clase_id
        }

        datos_animales[nombre] = nuevo_animal
        guardar_datos(nuevo_animal, 'zoo.csv')

        print(f"el animal '{nombre}' se ha agregado con éxito.")

    elif opcion == 'd':
        print("adios")
        break

    else:
        print("selecciona una opción válida.")
