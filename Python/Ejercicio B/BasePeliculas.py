from Pelicula import Pelicula
import csv
import string
import unicodedata

class BasePeliculas:
    diccionario = {}

    def __init__(self, archivo:str):
        self.enero = []
        self.febrero = []
        self.marzo = []
        self.abril = []
        self.mayo = []
        self.junio = []
        self.julio = []
        self.agosto = []
        self.septiembre = []
        self.octubre = []
        self.noviembre = []
        self.diciembre = []
        lista_registros = self.carga_archivo_csv(archivo)
        self.diccionario = {}
        for registro in lista_registros:
            titulo = registro[0]
            titulo_original = registro[1]
            url_imagen = registro[2]
            fecha_estreno = registro[3]
            sinopsis = registro[4]
            pelicula = Pelicula(titulo,titulo_original,url_imagen,fecha_estreno,sinopsis)
            self.agregarMes(pelicula,self.enero,self.febrero,self.marzo,self.abril,self.mayo,self.junio,self.julio,self.agosto,self.septiembre,self.octubre,self.noviembre,self.diciembre)
        self.agregarDiccionario(self.enero,self.febrero,self.marzo,self.abril,self.mayo,self.junio,self.julio,self.agosto,self.septiembre,self.octubre,self.noviembre,self.diciembre)

    def agregarMes(self,pelicula,enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre):
        meslista = list(pelicula.registro[3])
        mes = meslista[5]+meslista[6]
        if(mes == "01"):
            enero.append(pelicula)
        if(mes == "02"):
            febrero.append(pelicula)
        if(mes == "03"):
            marzo.append(pelicula)
        if(mes == "04"):
            abril.append(pelicula)
        if(mes == "05"):
            mayo.append(pelicula)
        if(mes == "06"):
            junio.append(pelicula)
        if(mes == "07"):
            julio.append(pelicula)
        if(mes == "08"):
            agosto.append(pelicula)
        if(mes == "09"):
            septiembre.append(pelicula)
        if(mes == "10"):
            octubre.append(pelicula)
        if(mes == "11"):
            noviembre.append(pelicula)
        if(mes == "12"):
            diciembre.append(pelicula)

    def agregarDicccionario(self,enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre):
        self.diccionario["Enero"] = enero
        self.diccionario["Febrero"] = febrero
        self.diccionario["Marzo"] = marzo
        self.diccionario["Abril"] = abril
        self.diccionario["Mayo"] = mayo
        self.diccionario["Junio"] = junio
        self.diccionario["Julio"] = julio
        self.diccionario["Agosto"] = agosto
        self.diccionario["Septiembre"] = septiembre
        self.diccionario["Octubre"] = octubre
        self.diccionario["Noviembre"] = noviembre
        self.diccionario["Diciembre"] = diciembre

    def carga_archivo_csv(self,archivo:str)->list:
        lista_registros = []
        with open(archivo,'r',encoding='utf-8') as a :
            reader = csv.reader(a)
            for renglon in reader:
                lista_registros.append(renglon)
        return lista_registros

    
if __name__ == "__main__":
    base = BasePeliculas("C:\Users\CSI PRO\Documents\GitHub\experimento\Python\Ejercicio B\estrenos.csv")
    print(base.diccionario["Enero"][0].titulo)