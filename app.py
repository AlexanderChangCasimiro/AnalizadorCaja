from flask import Flask, render_template, request

from analizador.lexer import analizar_lexico
from analizador.parser import analizar_sintaxis
from analizador.afd import ejecutar_afd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():

    tokens = []
    resultado_sintaxis = ""

    recorrido_afd = []
    resultado_afd = ""

    if request.method == "POST":

        texto = request.form["proceso"]

        tokens = analizar_lexico(texto)

        resultado_sintaxis = analizar_sintaxis(tokens)

        recorrido_afd, resultado_afd = ejecutar_afd(tokens)

    return render_template(
        "index.html",
        tokens=tokens,
        resultado_sintaxis=resultado_sintaxis,
        recorrido_afd=recorrido_afd,
        resultado_afd=resultado_afd
    )

if __name__ == "__main__":
    app.run(debug=True)