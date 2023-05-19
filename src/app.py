from flask import Flask, render_template, request, redirect, session, Response, jsonify

app = Flask(__name__)

@app.route("/")
def index_():
    return render_template('clinica.html')

@app.route("/clinica.html")
def index():
    return render_template('clinica.html')
@app.route("/login.html")
def PedirCita():
    return render_template('login.html')

@app.route("/agregar_datos.html")
def formulario_agregar_dato():
    return render_template('agregar_datos.html')

@app.route("/actualizar.html")
def actualizar():
    return render_template('actualizar.html')

@app.route("/Contactanos.html")
def Contactanos():
    return render_template('Contactanos.html')

@app.route("/QuienesSomos.html")
def QuienesSomos():
    return render_template('QuienesSomos.html')

@app.route("/servicios.html")
def servicios():
    return render_template('servicios.html')

@app.route("/pedircita.html")
def pedircita():
    return render_template('pedircita.html')

@app.route("/registro.html")
def registro():
    return render_template('registro.html')

@app.route("/form.html")
def form():
    return render_template('form.html')

@app.route("/nombre.html")
def nombre():
    return render_template('nombre.html')

if __name__  == '__main__':
    app.run(host='0.0.0.0', port='4000', debug=True) 