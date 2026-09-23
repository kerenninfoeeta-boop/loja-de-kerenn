# AGENTS.md

## Visão geral
Este repositório contém uma aplicação Flask simples para uma loja fictícia chamada "Sabor & Cia". O objetivo do projeto é exibir uma landing page, a lista de produtos e a página sobre a marca.

## Estrutura principal
- `app.py`: ponto de entrada da aplicação Flask e definição das rotas.
- `templates/`: arquivos HTML com Jinja2.
- `static/style.css`: estilos visuais da interface.

## Rotas esperadas
- `/` -> página inicial
- `/produtos` -> lista de produtos
- `/sobre` -> informações da loja

## Regras de trabalho
- Preserve o padrão de templates baseados em Jinja2.
- Mantenha o texto em português quando for alterar o conteúdo visual.
- Se alterar nomes de rotas, atualize qualquer navegação que dependa delas.
- Quando adicionar novos produtos, use a estrutura atual do dicionário em `produtos` em `app.py`.
- Prefira manter a aparência e a linguagem do projeto consistentes com o estilo já existente.

## Como rodar localmente
```bash
python app.py
```
A aplicação ficará disponível em `http://127.0.0.1:5000`.

## Verificação
Antes de concluir alterações, valide que o código ainda importa corretamente e que as rotas relevantes respondem sem erro.
