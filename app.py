from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cursos")
def cursos():
    return render_template("cursos.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
