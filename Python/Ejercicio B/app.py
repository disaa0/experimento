from flask import Flask, render_template, request, redirect, url_for, flash
from Pelicula import Pelicula
from BasePeliculas import BasePeliculas

app = Flask(__name__)
basePeliculas = BasePeliculas()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar-por-<caracteristica>')
def buscar_por_caracteristica(caracteristica:str):
    print(caracteristica)
    return render_template('busqueda.html', caracteristica=caracteristica)

@app.route('/desplegar-todas')
def desplegar_todas():
    return render_template('despliegue.html', caracteristica='todas', listaPeliculas=basePeliculas.desplegarPeliculas())

@app.route('/despliegue-por-<caracteristica>')
def desplegar_por_caracteristica(caracteristica:str):
    print(caracteristica)
    valor = request.args.get('valor')

    lista = []
    
    if caracteristica == 'titulo':
        lista = basePeliculas.buscarPorTitulo(valor)
    elif caracteristica == 'sinopsis':
        lista = basePeliculas.buscarPorSinopsis(valor)
    elif caracteristica == 'mes':
        if len(valor) == 1:
            valor = '0' + valor
        lista = basePeliculas.buscarPorMes(valor)


    return render_template('despliegue.html', caracteristica=caracteristica, listaPeliculas=lista)

@app.route('/registrar')
def registrar():
    return render_template('ingresarPelicula.html')

@app.route('/registrar-pelicula', methods=['POST'])
def registrarPelicula():
    titulo = request.form['titulo']
    titulo_original = request.form['titulo_original']
    url_imagen = request.form['url_imagen']
    fecha_estreno = request.form['fecha_estreno']
    sinopsis = request.form['sinopsis']

    pelicula = Pelicula(titulo, titulo_original, url_imagen, fecha_estreno, sinopsis)
    basePeliculas.registrarPeliculas([pelicula])

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

