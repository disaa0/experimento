import csv

class Pelicula:

    def __init__(self, lista:list):
        self.titulo =lista[0]
        self.titulo_original = lista[1]
        self.url_imagen = lista[2]
        self.fecha_estreno = lista[3][5:6]
        self.sinopsis = lista[4]
     
    def convertir_a_letra(self, fecha:str) -> str:
        if fecha == "01":
            return "Enero"
        elif fecha == "02":
            return "Febrero"
        elif fecha == "03":
            return "Marzo"
        elif fecha == "04":
            return "Abril"
        elif fecha == "05":
            return "Mayo"
        elif fecha == "06":
            return "Junio"
        elif fecha == "07":
            return "Julio"
        elif fecha == "08":
            return "Agosto"
        elif fecha == "09":
            return "Septiembre"
        elif fecha == "10":
            return "Octubre"
        elif fecha == "11":
            return "Noviembre"
        elif fecha == "12":
            return "Diciembre"
        else:
            return "Fecha invalida"
    
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Duracion: {self.duracion}, Genero: {self.genero}'