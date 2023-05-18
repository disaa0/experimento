import  csv
from Pelicula import Pelicula

def leer_peliculas_csv(archivo:str) -> list:
    lista_peliculas = []
    with open(archivo, 'r', encoding='utf8') as a:
        reader = csv.reader(a)
        for row in reader:
            lista_peliculas.append(row)
    return lista_peliculas

def main():
    peliculas = leer_peliculas_csv("Python\Ejercicio B\estrenos.csv")
    diccionario_peliculas = {}
    for i in peliculas:
        diccionario_peliculas[i[0]] = i[3]

    #tomar diccionario peliculas y hacer diccionario de peliculas por mes
    diccionario_meses = {}
    for i in diccionario_peliculas:
       diccionario_meses[i] = diccionario_peliculas[i][5:7]
    print(diccionario_meses)

    

if __name__ == "__main__":
    main()