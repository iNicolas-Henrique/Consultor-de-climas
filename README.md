# Sistema de Consulta de Clima em Python

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-Requisições%20HTTP-green)
![JSON](https://img.shields.io/badge/JSON-Armazenamento-orange)
![WeatherAPI](https://img.shields.io/badge/WeatherAPI-Clima%20em%20tempo%20real-lightblue)
![VS Code](https://img.shields.io/badge/VS%20Code-Editor-blue?logo=visualstudiocode&logoColor=white)
![Status](https://img.shields.io/badge/Status-Finalizado-brightgreen)
![License](https://img.shields.io/badge/Licença-Acadêmica-purple)
![Funciona na minha máquina](https://img.shields.io/badge/Funciona-na%20minha%20máquina-brightgreen)
![Gambiarra controlada](https://img.shields.io/badge/Gambiarra-controlada-yellow)
![Movido a café](https://img.shields.io/badge/Movido%20a-café-brown)
![IFAP](https://img.shields.io/badge/IFAP-ADS-green)
![Acadêmico](https://img.shields.io/badge/Fins-Acadêmicos-informational)
![Aprendizado](https://img.shields.io/badge/Foco-Aprendizado-yellow)
![Boas Práticas](https://img.shields.io/badge/Código-Boas%20práticas-brightgreen)



Este projeto é uma aplicação bem simples em Python que consulta informações climáticas atuais de cidades brasileiras usando uma API externa de clima.

O sistema utiliza a biblioteca `requests` para fazer requisições HTTP para a WeatherAPI e exibe os dados organizados no terminal. Além disso, salva os resultados das consultas em um arquivo JSON chamado `UPN.json`.

## Objetivo

O objetivo principal do mini projeto é praticar o uso de APIs REST em Python, trabalhar com dados em formato JSON, utilizar funções, estruturas de repetição e tratamento de exceções.

## Tecnologias utilizadas

- Python 3
- Biblioteca `requests`
- Biblioteca `json`
- Biblioteca `os`
- Biblioteca `time`
- WeatherAPI

## Funcionalidades

- Consulta clima atual em tempo real
- Consulta automaticamente 5 cidades brasileiras
- Exibe os dados no terminal de forma organizada
- Salva os resultados em um arquivo `UPN.json`
- Usa tratamento de erros com `try` e `except`
- Continua executando mesmo se uma cidade apresentar algum erro
- Utiliza delay entre as consultas para melhor leitura

## Cidades consultadas

O sistema consulta automaticamente as seguintes cidades:

- Brasília
- Macapá
- Belém
- São Paulo
- Rio de Janeiro

## Informações exibidas

Para cada cidade, o sistema mostra:

- Nome da cidade
- Região/Estado
- País
- Horário local
- Temperatura atual
- Sensação térmica
- Condição climática
- Umidade
- Velocidade do vento
- Direção do vento
- Visibilidade
- Percentual de nuvens
- Última atualização

## Como instalar as dependências

Antes de executar o projeto, instale a biblioteca `requests`:

```bash
pip install requests

```

## Como usar no VS Code

1. Baixe ou clone este projeto para o seu computador.

2. Abra a pasta do projeto no Visual Studio Code.

3. Verifique BEM se o Python está instalado no computador.

4. Abra o terminal do VS Code:

## Créditos

Desenvolvido por **Nicolas Henrique Costa Santos**.

Projeto criado para fins acadêmicos, com foco em usar e aprender sobre APIs, manipulação de JSON e prática de programação em Python.

