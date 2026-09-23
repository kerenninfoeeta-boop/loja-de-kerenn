# Lojinha com classe Produto

## Objetivo

Este projeto é uma atividade de Programação Orientada a Objetos. Ele simula uma lojinha da Sabor & Cia, com cadastro de produtos, consulta de catálogo e controle de estoque. As páginas Flask que já existiam também foram mantidas.

## Como executar

No terminal, dentro da pasta do projeto:

```bash
python app.py
```

O comando abre o menu interativo da lojinha. Para iniciar as páginas Flask, execute:

```bash
python app.py --web
```

A aplicação web fica disponível em `http://127.0.0.1:5000`.

## Funcionalidades

- Cadastrar produto com nome, preço e estoque inicial.
- Listar o catálogo e os dados de cada produto.
- Vender unidades, validando a quantidade e o estoque disponível.
- Repor unidades no estoque.
- Acessar as páginas inicial, de produtos e sobre a loja no Flask.

## Classe Produto

A classe `Produto` representa cada item da loja. O nome é guardado em `nome`; preço e estoque ficam em atributos privados (`__preco` e `__estoque`) e são acessados pelas properties `preco` e `estoque`. Os setters impedem valores negativos e tipos inválidos.

O método `exibir()` mostra nome, preço em reais com duas casas decimais e estoque. `vender(qtd)` só reduz o estoque quando a quantidade é válida e há unidades suficientes, retornando `True` em caso de venda ou `False` quando recusa. `repor(qtd)` valida a quantidade antes de aumentar o estoque.
