import csv
class Pelicula:
    def __init__(self,titulo,titulo_original,url_imagen,fecha_estreno,sinopsis):
        self.titulo = titulo
        self.titulo_original = titulo_original
        self.url_imagen = url_imagen
        self.fecha_estreno = fecha_estreno
        self.sinopsis = sinopsis
    def __str__(self):
        return f"{self.titulo} ({self.fecha_estreno})"
      
#def lee_archivo_csv(archivo):
#    lista = []
#    try:
#        with open(archivo, "r", encoding="utf-8") as fh:
#            csv_reader = csv.reader(fh)
#            for row in csv_reader:
#                lista.append(row)
#    except IOError:
#        print("Error al abrir el archivo")
#    return lista

def lee_diccionario_estrenos(archivo):
    diccionario = {}
    try:
        with open(archivo, "r", encoding="utf-8") as fh:
            csv_reader = csv.reader(fh)
            for row in csv_reader:
                llave = row['id']
                diccionario[llave] = row
    except IOError:
        print("Error al abrir el archivo")
    return diccionario



#agregar una pelicula
#with open ('estrenos.csv',newline='') as File:
#    reader = csv.reader(File)
#    data = [line for line in reader]
#    with open ('estrenos.csv','w',newline='') as File:
#        writer = csv.writer(File)
#        writer.writerow(['id','nombre','genero','estreno','sinopsis'])
#        writer.writerow(data)

if __name__ == "__main__":
    print(lee_diccionario_estrenos("estrenos.csv"))