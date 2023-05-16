from funciones import leer_csv, list_to_dict, filtrar_x_criterio, organizar_x_valor
from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/listado_clase')
def clases():
    return render_template('listado_clase.html',lista_clases=lista_clases)

@app.route('/listarclase_<criterio>')
def listado(criterio):
    valor = diccionario_clases[criterio]['Clase_id']
    lista = filtrar_x_criterio(diccionario_animales, 'clase', valor)
    return render_template('listado.html', lista_animales = lista, criterio = criterio)

@app.route('/listado_caracteristicas')
def caracs():
    return render_template('listado_caracteristicas.html', lista_caracteristicas = lista_caracteristicas)

@app.route('/listarcaracteristica_<criterio>')
def listado_carac(criterio):
    dicc_filtrado = organizar_x_valor(diccionario_animales, criterio)

    return render_template('listadoxcarac.html', criterio=criterio, dicc_filtrado = dicc_filtrado)

if __name__ == '__main__':
    clases = leer_csv('Python\clases.csv')
    animales = leer_csv('Python\zoo.csv')
    diccionario_clases = list_to_dict(clases, 'Clase_tipo')
    diccionario_animales = list_to_dict(animales, 'nombre_animal')
    lista_clases = list(diccionario_clases.keys())
    lista_caracteristicas = list(animales[0].keys())
    del lista_caracteristicas[0]
    del lista_caracteristicas[-1]

    app.run(debug='on')