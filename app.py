from flask import Flask, render_template

app = Flask(__name__)

produtos = [
    {"nome": "X-Burger", "preco": 15.00, "estoque": 5, "oferta": True},
    {"nome": "Batata Frita", "preco": 8.00, "estoque": 10, "oferta": False},
    {"nome": "Refrigerante", "preco": 6.00, "estoque": 0, "oferta": False}
]

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/produtos")
def produtos_page():
    return render_template("produtos.html", produtos=produtos)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

app.run(debug=True)
