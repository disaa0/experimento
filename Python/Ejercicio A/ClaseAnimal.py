import csv

class ClaseAnimal:
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f'{self.nombre}'

def readClases(file_path:str = './clases.csv') -> list[ClaseAnimal]:
    clases = []
    with open(file_path,'r',encoding='utf-8') as fi:
        reader = csv.reader(fi)
        
        for clase in reader:
            clases.append(ClaseAnimal(*clase))
        
    return clases

            

