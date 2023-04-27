from flask import Flask, render_template, jsonify
from otros import cargar_archivo, relacionar_diccionarios


app = Flask(__name__)

@app.route("/")
def index(): 
    lista_clases = cargar_archivo("../clases.csv")
    lista_zoo = cargar_archivo("../zoo.csv")
    lista_animales_relacionada = relacionar_diccionarios(lista_zoo, lista_clases)
    return render_template("index.html", lista_animales_relacionada=lista_animales_relacionada, lista_clases=lista_clases)


@app.route("/animales")
def datos():
    lista_clases = cargar_archivo("../clases.csv")
    lista_zoo = cargar_archivo("../zoo.csv")
    lista_animales_relacionada = relacionar_diccionarios(lista_zoo, lista_clases)
    return jsonify(lista_animales_relacionada)

app.run(debug=True)