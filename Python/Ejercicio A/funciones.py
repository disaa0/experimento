import csv
def lee_archivo_csv(archivo:str)->list:
    '''
    Lee un archivo csv y regresa una lista de renglones 
    (y campos dentro de los renglones)
    '''
    lista = []
    try:
        with open(archivo,"r",encoding="utf-8") as fh: #fh: file handle
            csv_reader = csv.reader(fh)
            for linea in csv_reader:
                lista.append(linea)
    except IOError:
        print(f"No se pudo abrir el archivo {archivo}")
    
    return lista

def Clase():
    pass


def Caracteristica():
    pass

def AgregarAnimal():
    pass
