from funciones import cargar_datos_mes, cargar_datos_anio, guardar_datos
import os
from datetime import datetime
import calendar

datos = cargar_datos_mes('Python/Ejercicio B/estrenos.csv')
datos_year = cargar_datos_anio('Python/Ejercicio B/estrenos.csv')

while True:
    print("\nBienvenido al sistema de películas")
    print("1. Mostrar películas por mes")
    print("2. Mostrar películas por año")
    print("3. Agregar película")
    print("4. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        mes = input("Ingrese el mes en inglés Ej: January: ")
        if mes in datos:
            for movie in datos[mes]:
                print(f"- {movie['titulo']}: {movie['titulo']}")
        else:
            print("No hay películas para ese mes")

    elif opcion == "2":
        anio = int(input("Ingrese el año Ej: 2023: "))
        if anio in datos_year:
            for movie in datos_year[anio]:
                print(f"- {movie['titulo']}: {movie['titulo']}")
        else:
            print("No hay películas para ese año")

    elif opcion == "3":
        nombre = input("Ingrese el nombre de la pelicula: ")
        nueva_pelicula = {
            'titulo': nombre,
            'titulo_original': input("Ingresa el titulo original: "),
            'url_imagen': input("Ingresa una url: "),
            'fecha_estreno': input("Ingresa fecha de estreno Ej: 2023-04-05: "),
            'sinopsis': input("Ingresa la sinopsis: ")
        }

        guardar_datos(nueva_pelicula, 'Python/Ejercicio B/estrenos.csv')

        print(f"La pelicula '{nombre}' ha sido agregado con éxito.")

    elif opcion == '4':
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")