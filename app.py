"""Lojinha da Sabor & Cia com classe Produto e páginas Flask."""

import sys
from numbers import Real

from flask import Flask, render_template


class Produto:
    """Representa um produto com preço e estoque validados."""

    def __init__(self, nome, preco, estoque, oferta=False):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.oferta = oferta

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, Real):
            raise ValueError("O preço deve ser um número válido.")
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self.__preco = float(valor)

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise ValueError("O estoque deve ser um número inteiro válido.")
        if valor < 0:
            raise ValueError("O estoque não pode ser negativo.")
        self.__estoque = valor

    @staticmethod
    def _validar_quantidade(qtd):
        return isinstance(qtd, int) and not isinstance(qtd, bool) and qtd > 0

    def exibir(self):
        preco_formatado = f"{self.preco:.2f}".replace(".", ",")
        print(f"Produto: {self.nome} | Preço: R$ {preco_formatado} | Estoque: {self.estoque}")

    def vender(self, qtd):
        if not self._validar_quantidade(qtd):
            print("Venda recusada: informe uma quantidade inteira maior que zero.")
            return False
        if qtd > self.estoque:
            print(f"Venda recusada: estoque insuficiente. Disponível: {self.estoque}.")
            return False
        self.estoque -= qtd
        print(f"Venda realizada: {qtd} unidade(s) de {self.nome}.")
        return True

    def repor(self, qtd):
        if not self._validar_quantidade(qtd):
            print("Reposição recusada: informe uma quantidade inteira maior que zero.")
            return False
        self.estoque += qtd
        print(f"Reposição realizada: {qtd} unidade(s) de {self.nome}.")
        return True


app = Flask(__name__)

# Os produtos iniciais preservam o catálogo que já existia no projeto.
produtos = [
    Produto("X-Burger", 15.00, 5, oferta=True),
    Produto("Batata Frita", 8.00, 10),
    Produto("Refrigerante", 6.00, 0),
]


def listar_catalogo(catalogo):
    if not catalogo:
        print("O catálogo está vazio.")
        return
    print("\n--- Catálogo ---")
    for indice, produto in enumerate(catalogo, start=1):
        print(f"{indice}. ", end="")
        produto.exibir()


def escolher_produto(catalogo):
    if not catalogo:
        print("Não há produtos cadastrados.")
        return None
    try:
        numero = int(input("Número do produto: "))
    except (ValueError, EOFError):
        print("Entrada inválida. Digite o número de um produto.")
        return None
    if numero < 1 or numero > len(catalogo):
        print("Esse número de produto não existe.")
        return None
    return catalogo[numero - 1]


def ler_quantidade(mensagem):
    try:
        return int(input(mensagem))
    except (ValueError, EOFError):
        print("Entrada inválida. Digite uma quantidade inteira.")
        return None


def menu_principal(catalogo=None):
    """Executa o menu em loop; recebe catálogo opcional para facilitar o uso."""
    if catalogo is None:
        catalogo = produtos

    while True:
        print("\n=== Lojinha Sabor & Cia ===")
        print("1 - Cadastrar produto")
        print("2 - Listar catálogo")
        print("3 - Vender")
        print("4 - Repor")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome do produto: ").strip()
            if not nome:
                print("Cadastro recusado: o nome não pode ficar vazio.")
                continue
            preco = ler_quantidade_decimal("Preço do produto: R$ ")
            estoque = ler_quantidade("Estoque inicial: ")
            if preco is None or estoque is None:
                continue
            try:
                catalogo.append(Produto(nome, preco, estoque))
                print(f"Produto {nome} cadastrado com sucesso.")
            except ValueError as erro:
                print(f"Cadastro recusado: {erro}")
        elif opcao == "2":
            listar_catalogo(catalogo)
        elif opcao == "3":
            produto = escolher_produto(catalogo)
            if produto is not None:
                qtd = ler_quantidade("Quantidade para vender: ")
                if qtd is not None:
                    produto.vender(qtd)
        elif opcao == "4":
            produto = escolher_produto(catalogo)
            if produto is not None:
                qtd = ler_quantidade("Quantidade para repor: ")
                if qtd is not None:
                    produto.repor(qtd)
        elif opcao == "5":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Escolha uma opção de 1 a 5.")


def ler_quantidade_decimal(mensagem):
    try:
        # Aceita tanto vírgula quanto ponto como separador decimal.
        return float(input(mensagem).strip().replace(",", "."))
    except (ValueError, EOFError):
        print("Entrada inválida. Digite um preço numérico.")
        return None


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/produtos")
def produtos_page():
    return render_template("produtos.html", produtos=produtos)


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


if __name__ == "__main__":
    if "--web" in sys.argv:
        app.run(debug=True)
    else:
        menu_principal()
