from flask import Flask, send_from_directory, render_template, request, redirect, url_for
import datetime as dt
import random
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/sobre_nosotros")
def sobre():
    return send_from_directory("static", "sobre_nosotros.html")

@app.route("/contactar")
def contactar():
    return send_from_directory("static", "contactar.html")

@app.route("/dinamica1")
def dinamica1():
    nombre = "Jose"
    apellido = "Pablo"
    fecha = dt.datetime.now()
    return render_template("dinamica1.html", nombre=nombre, apellido=apellido, fecha=fecha)

@app.route("/dinamica2")
def dinamica2():
    nombres = ["Jose","Ramon","Ana","Marta"]
    apellidos = ["Pablo","Garcia","Kareninaa","Marcapasos"]
    nombre2= random.choice (nombres)
    apellido2=random.choice (apellidos)
    fecha = dt.datetime.now()
    return render_template("dinamica2.html", nombre2=nombre2, apellido2=apellido2, fecha=fecha)

@app.route("/dinamica3")
def dinamica3():
    personas = ["Jose","Ramon","Ana","Marta"]
    return render_template("dinamica3.html", personas=personas)

@app.route("/dinamica4")
def dinamica4():
    numeros = [2, 4, 7, 5, 9, -7]
    numeros = list(filter(lambda x:x>0, numeros))
    return render_template("dinamica4.html", numeros=numeros)

@app.route("/login", methods = ["GET", "POST"])
def login() :
    if request.method == "GET" :
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if password == "password" :
            print(username,password)
            return redirect(url_for("dashboard", username=username))
            
        else:
            return "Contraseña Incorrecta"
        
@app.route("/dashboard/<string:username>")
def dashboard(username):
    return render_template("dashboard.html", username=username)

@app.route("/math", methods = ["GET", "POST"])
def math() :
    if request.method == "GET" :
        return render_template("math.html")
    else:
        num1=request.form["num1"]
        num2=request.form["num2"]

        resultado = int(num1)+ int(num2)
        return "el resultado es " + str(resultado)
            

if __name__=="__main__":
    app.run()

