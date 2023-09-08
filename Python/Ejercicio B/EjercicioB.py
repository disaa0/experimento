import csv
#titulo,titulo_original,url_imagen,fecha_estreno,sinopsis
class Pelicula:
    def __init__(self, titulo, tituloOriginal, urlImagen, fechaEstreno, sinopsis):
        self.titulo = titulo
        self.tituloOriginal = tituloOriginal
        self.urlImagen = urlImagen
        self.fechaEstreno = fechaEstreno
        self.sinopsis = sinopsis

    def __str__(self):
        return f'Nombre: {self.titulo} Fecha: {self.tituloOriginal} Genero: {self.urlImagen} Director: {self.fechaEstreno} Duracion: {self.sinopsis}'
    def getter(self):
        return self.titulo, self.tituloOriginal, self.urlImagen, self.fechaEstreno, self.sinopsis

def readFile(csv_file):
    data = {}
    with open(csv_file, encoding = 'utf8') as file:
        reader = csv.reader(file, delimiter = ',')
        data.update({row[0]: Pelicula(row[0], row[1], row[2], row[3], row[4]) for row in reader})
    return data


#print(readFile('Python\\Ejercicio B\\estrenos.csv'))
#test = {}
test = readFile('Python\\Ejercicio B\\estrenos.csv')
while True:
    inp = input('1 search, 2 exit ')
    if inp == '1':
        imp2 = input('Insert release date: ')
        try:
            print(test)
            #print((test.__getitem__(imp2)).getter())
        except KeyError:
            print('Unknow date')
    elif inp == '2':
        break
    else:
        print('error')