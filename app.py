from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html", titulo="Página de inicio", saludo="Bienvenido")

@app.route("/lista")
def frutas():
    items = [ "Pera", "Manzana", "Piña", "Melón"]
    return render_template("frutas.html", items=items)

@app.route("/numeros")
def numeros():
    numeros = [1,4,5,2,3,9,7]
    return render_template("numeros.html", numeros=numeros)

@app.route("/web")
def index():
    return "Server funcionando"

@app.route("/web/usuario/<nombre>/<apellido>")
def mostrar_usuario(nombre: str, apellido: str) -> str:
    return f"Hola, {nombre} {apellido}"

@app.route("/web/edad/<int:edad>")
def mostrar_edad(edad: int) -> str:
    return f"Tienes {edad} años"

@app.route("/web/contacto", methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form["nombre"]
        email = request.form["email"]
        mensaje = request.form["mensaje"]
        return "Mensaje enviado"
    else:
        return render_template("contacto.html")

@app.route("/web/sumar", methods=['GET', 'POST'])
def sumar():
    if request.method == "POST":
        a = int(request.form["n1"])
        b = int(request.form["n2"])
        suma = a + b
        return render_template("sumar.html", suma = suma)
    else:
        return render_template("sumar.html", suma = None)

@app.route("/web/email", methods=['GET', 'POST'])
def enviar_email():
    if request.method == 'POST':
        asunto = request.form["asunto"]
        correo = request.form["email"]
        mensaje = request.form["mensaje"]
        
        email_user = os.getenv("EMAIL_USER") or "email_user"
        email_token = os.getenv("EMAIL_TOKEN") or "email_token"
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(email_user, email_token)
        
        msg = MIMEText(f"Asunto: {asunto}\nMensaje: {mensaje}")
        msg["From"] = email_user
        msg["To"] = correo
        msg["Subject"] = asunto
        
        servidor.sendmail(email_user, correo, msg.as_string())
        servidor.quit()
        
        return "Correo enviado"
    else:
        return render_template("email.html")



if __name__ == '__main__':
    app.run()
    
