from flask import Flask, redirect, render_template, request, url_for
from funciones import *
app = Flask(__name__)


@app.route("/")
def listado():
    return render_template('index.html', lista=listar(), clases=crearDict('clases.csv'))


@app.route("/<columna>")
def filtar(columna):
    return render_template('index.html', lista=listar(columna), clases=crearDict('clases.csv'))


@app.route("/agregar/", methods=["GET", "POST"])
def agregar():
    if request.method == 'GET':
        return render_template('agregar.html', zoo=listar(), clases=crearDict('clases.csv'))
    if request.method == 'POST':
        animal = request.form.to_dict()
        agregarAnimal(animal)
        return render_template('index.html', lista=listar(), clases=crearDict('clases.csv'))
