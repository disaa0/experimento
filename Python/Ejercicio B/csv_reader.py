import csv
import os

cwd = os.getcwd()   # Get the current working directory (cwd)
mes = input("Ingrese el mes a buscar ej. 01, 02, 03: ")
peliculas = []

with open(cwd + '\\Python\\Ejercicio B\\estrenos.csv', newline='', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        fecha = row['fecha_estreno'].split('-')
        if  mes in fecha[1]:
            peliculas.append(row)

for pelicula in peliculas:
    print(pelicula)