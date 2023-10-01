class Pelicula:
    def __init__(self,titulo,titulo_original,url_imagen,fecha_estreno,sinopsis) -> None:
        self.titulo = titulo
        self.titulo_original = titulo_original
        self.url_imagen = url_imagen
        self.fecha_estreno = fecha_estreno
        self.sinopsis = sinopsis

    def __str__(self) -> str:
        return f"{self.titulo} | {self.fecha_estreno}"