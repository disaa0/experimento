class Pelicula:
    def __init__(self,titulo,titulo_original,url_imagen,fecha_estreno,sinopsis):
        self.titulo = titulo
        self.titulo_original = titulo_original
        self.url_imagen = url_imagen
        self.fecha_estreno = fecha_estreno
        self.sinopsis = sinopsis

    def __str__(self):
        return f'{self.titulo} ({self.fecha_estreno})'

if __name__ == "__main__":
    print()
    pelicula = Pelicula("Oso vicioso","Cocaine Bear","https://www.imdb.com/title/tt14209916/mediaviewer/rm184234241/?ref_=tt_ov_i, 2023-04-05","Cuenta la historia de un narcotraficante cuyo avión se estrella con un cargamento de cocaína que es encontrada por un oso negro, quien se la come.")
    print(pelicula)