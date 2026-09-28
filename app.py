from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        idade = request.form.get("idade")
        nascimento = request.form.get("nascimento")
        genero = request.form.get("genero")

        if not nome or not idade or not nascimento or not genero:
            return render_template(
                "index.html",
                erro="Preencha todos os campos do cadastro."
            )

        return render_template(
            "index.html",
            sucesso=f"Cadastro realizado com sucesso, {nome}!"
        )

    return render_template("index.html")


@app.route("/cursos")
def cursos():
    return render_template("index.html", mostrar_cursos=True)


@app.route("/entrar", methods=["POST"])
def entrar():
    nome = request.form.get("nome")

    if not nome:
        return render_template(
            "index.html",
            erro="Digite o seu nome para entrar."
        )

    return render_template(
        "index.html",
        aluno=nome,
        mostrar_cursos=True
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
