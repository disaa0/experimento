
import pandas as pd 
from datetime import datetime
new_dict = {"01": [],
            "02": [],
            "03": [],
            "04": [],
            "05": [],
            "06": [],
            "07": [],
            "08": [],
            "09": [],
            "10": [],
            "11": [],
            "12": []}

class Pelicula:
    def __init__(self, titulo, titulo_original, url_imagen, fecha_estreno, sinopsis):
        self.titulo
        self.titulo_original
        self.url_imagen
        self.fecha_estreno
        self.sinopsis

    def __str__(self):
        return f'{self.titulo} {self.titulo_original} {self.url_imagen} {self.fecha_estreno} {self.sinopsis}'


def LeerArchivo(file):
   
    datos = pd.read_csv(file, 
                sep=',', 
                header=None, 
                names=['titulo', 'titulo_original', 'url_imagen', 'fecha_estreno', 'sinopsis'],)
    for row in datos.itertuples():
        
       
        for key, value in new_dict.items():
            if key == row.fecha_estreno[5:7]:
                new_dict[key].append(row.titulo)
        
    print(new_dict)


def imprimirCartelera():
    for key, value in new_dict.items():
        print( "MES: " + key)
        print( "PELICULAS: ")
        for i in value:
            print(i)

def agregarPelicula(file):
    titulo = input("Ingrese el titulo de la pelicula: ")
    titulo_original = input("Ingrese el titulo original de la pelicula: ")
    url_imagen = input("Ingrese la url de la imagen de la pelicula: ")
    fecha_estreno = input("Ingrese la fecha de estreno de la pelicula: ")
    sinopsis = input("Ingrese la sinopsis de la pelicula: ")
    datos = pd.read_csv(file, 
                sep=',', 
                header=None, 
                names=['titulo', 'titulo_original', 'url_imagen', 'fecha_estreno', 'sinopsis'],)
    datos = datos.append({'titulo': titulo, 'titulo_original': titulo_original, 'url_imagen': url_imagen, 'fecha_estreno': fecha_estreno, 'sinopsis': sinopsis}, ignore_index=True)
    datos.to_csv(file, index=False, header=None)
    print("Pelicula agregada con exito")