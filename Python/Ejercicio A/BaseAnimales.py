import csv
from Animal import Animal 
from ClaseAnimal import ClaseAnimal, readClases

class BaseAnimales:
    def __init__(self):
        self.caracteristicas:dict[str,list[Animal]] = {}
        self.clases:dict[str, list[tuple[str,Animal]]] = {}
        self.clases_lista = readClases()
        lista_animales = self._readAnimals()

        self.createCaracteristicas(lista_animales.pop(0))
        self.assignAnimalsToCaracteristicas(lista_animales)
        for animal in self.animales:
            print(animal)

    
    def _readAnimals(self,file_path:str = './zoo.csv'):
        with open(file_path,'r',encoding='utf-8') as fi:
            reader = csv.reader(fi)

            return list(reader)
            

    def assignAnimalsToCaracteristicas(self,lista):
        for animal in lista:
            caracteristicasB = [*animal[1:13],*animal[14:-1]]
            caracteristicasP = [animal[0],animal[13],animal[-1]]

            objetoAnimal = Animal(*caracteristicasP)

            for index,caracteristicaB in enumerate(self.caracteristicas_booleanas):
                if caracteristicasB[index] == '1':
                    self.caracteristicas[caracteristicaB].append(objetoAnimal)
            
            for llave, valor in self.caracteristicas.items():
                print(llave,str(valor))

    def createCaracteristicas(self,caracteristicas_lista:list[str]):
        self.caracteristicas_booleanas = [*caracteristicas_lista[1:13],*caracteristicas_lista[14:-1]]
        self.caracteristicas_ponderadas = [caracteristicas_lista[0],caracteristicas_lista[13],caracteristicas_lista[-1]]
        for caracteristica in self.caracteristicas_booleanas:
            self.caracteristicas[caracteristica] = []


    
    def getAnimalsByCaracteristica(self,caracteristica):
        return self.caracteristicas[caracteristica]

if __name__ == '__main__':
    base = BaseAnimales()
        