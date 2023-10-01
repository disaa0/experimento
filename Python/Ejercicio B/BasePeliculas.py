from Pelicula import Pelicula
import csv
import os

class BasePeliculas:
    def __init__(self,archivo:str = 'estrenos.csv'):
        print("Inicializando Base de Peliculas")

        registros = self.cargar_archivoCSV(archivo)
        self.campos = registros.pop(0)
        self.peliculas = self.cargarPeliculas(registros)
        self.peliculas_por_mes = self.ordenarPorMes()


    def cargar_archivoCSV(self,archivo:str) -> list[list[str]]:
        print("Cargando archivo CSV")

        with open(archivo, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            return list(reader)
    
    def cargarPeliculas(self, registros:list[list[str]]):
        peliculas = []
        for registro in registros:
            peliculas.append(Pelicula(*registro))
        
        return peliculas
    
    def ordenarPorMes(self) -> dict[str,list[Pelicula]]:
        peliculas_por_mes = {}
        for pelicula in self.peliculas:
            mes = pelicula.fecha_estreno.split('-')[1]
            if mes in peliculas_por_mes:
                peliculas_por_mes[mes].append(pelicula)
            else:
                peliculas_por_mes[mes] = [pelicula]
        
        return peliculas_por_mes
    
    def buscarPorMes(self, mes:str) -> list[Pelicula]:
        try:
            return self.peliculas_por_mes[mes]
        except KeyError:
            return []
    
    def buscarPorSinopsis(self, sinopsis:str) -> list[Pelicula]:
        peliculas = []
        for pelicula in self.peliculas:
            if sinopsis.lower() in pelicula.sinopsis.lower():
                peliculas.append(pelicula)
        
        return peliculas
    
    def buscarPorTitulo(self, titulo:str) -> list[Pelicula]:
        peliculas = []
        for pelicula in self.peliculas:
            if titulo.lower() in pelicula.titulo.lower():
                peliculas.append(pelicula)
        
        return peliculas

    def desplegarPeliculas(self) -> list[Pelicula]:        
        return self.peliculas
    
    
    def registrarPeliculas(self, peliculas:list[Pelicula]):
        registros = []
        
        for pelicula in peliculas:
            registros.append(f'"{pelicula.titulo}","{pelicula.titulo_original}",{pelicula.url_imagen},"{pelicula.fecha_estreno}","{pelicula.sinopsis}"')
        
        with open('estrenos.csv', 'a', encoding='utf-8') as f:
            f.write('\n'.join(registros))

        self.peliculas.extend(peliculas)
        
    
if __name__ == '__main__':
    archivo = os.path.abspath('estrenos.csv')
    base_peliculas = BasePeliculas(archivo)
    print(base_peliculas.peliculas_por_mes.items())