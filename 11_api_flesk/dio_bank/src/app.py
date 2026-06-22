from flask import Flask, url_for, request

app = Flask(__name__)


# =========================
# ROTA UTILIZANDO UM RETORNO HTML
# =========================
@app.route("/")
def hello_world():
    return "<p>Hello world</p>"


# =========================
# ROTA UTILIZANDO UM RETORNO JSON
# =========================
@app.route("/ola/<user>/<idade>/<gosto>")
def welcome(user, idade, gosto):
    return {
        'nome': user,
        'idade': idade,
        'gosto': gosto
    }


# =========================
# ROTA UTILIZANDO CHAMADA DE 2 MÉTODOS
# =========================
@app.route("/user/<usuario>", methods=["POST", "GET"])
def usuario_teste(usuario):
    return f"<h1>Ola ${usuario}</h1>"

# =========================
# ROTA UTILIZANDO CHAMADA DE DOIS MÉTODOS E VALIDAÇÕES DOS MESMOS
# =========================
@app.route("/teste-method/<usuario>", methods=["POST", "GET"])
def testeMethod(usuario):
    if request.method == "GET":
        return f"This is a method get {usuario}"
    else:
        return f"This is a method post {usuario}"


# =========================
# TESTES UTILIZANDO URL_FOR, UTILIZADO PARA VERIFICAR AS URLS
# =========================
with app.test_request_context():
    print(url_for("welcome", user="Vinicius", idade=12, gosto="Academia"))
    print(url_for("usuario_teste", usuario="Vinicius"))
    print(url_for("hello_world"))