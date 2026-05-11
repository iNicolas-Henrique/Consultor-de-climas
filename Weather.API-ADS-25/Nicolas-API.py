import requests
import json
import os
import time

# Limpa o terminal antes de começar, só para a saída ficar mais organizada.
os.system('cls' if os.name == 'nt' else 'clear')


def traduzir_direcao_vento(sigla):
    # A API manda a direção do vento em siglas. Aqui eu deixo isso mais legível.
    direcoes = {
        "N": "Norte",
        "NE": "Nordeste",
        "E": "Leste",
        "SE": "Sudeste",
        "S": "Sul",
        "SW": "Sudoeste",
        "W": "Oeste",
        "NW": "Noroeste"
    }

    # Se vier alguma sigla diferente, o programa não quebra e mostra uma mensagem padrão.
    return direcoes.get(sigla, "Direção desconhecida")


def get_weather(cidade):
    # Endereço da API que retorna o clima atual.
    BASE_URL = "http://api.weatherapi.com/v1/current.json"

    # Chave usada para liberar o acesso à API.
    api_key = "f4abfbefbb60416098d230246260705"

    # Parâmetros enviados na consulta: chave, cidade e idioma da resposta.
    params = {
        "key": api_key,
        "q": cidade,
        "lang": "pt"
    }

    # Como estamos consultando uma API externa, pode dar erro de conexão,
    # cidade inválida, demora na resposta ou algum dado vindo diferente.
    try:
        # Faz a requisição para a API. O timeout evita o programa ficar travado esperando.
        response = requests.get(BASE_URL, params=params, timeout=10)

        # Código 200 significa que a API respondeu certinho.
        if response.status_code == 200:
            # Converte a resposta JSON da API para um dicionário do Python.
            data = response.json()

            # Separo só as informações que quero usar e salvar no arquivo.
            data_clima = {
                "cidade": data["location"]["name"],
                "regiao": data["location"]["region"],
                "pais": data["location"]["country"],
                "horario_local": data["location"]["localtime"],
                "temperatura_celsius": data["current"]["temp_c"],
                "sensacao_termica": data["current"]["feelslike_c"],
                "clima": data["current"]["condition"]["text"],
                "umidade": data["current"]["humidity"],
                "vento_kmh": data["current"]["wind_kph"],
                "direcao_vento": data["current"]["wind_dir"],
                "direcao_vento_descricao": traduzir_direcao_vento(data["current"]["wind_dir"]),
                "visibilidade_km": data["current"]["vis_km"],
                "nuvens_percentual": data["current"]["cloud"],
                "ultima_atualizacao": data["current"]["last_updated"]
            }

            # Mostra os dados no terminal de um jeito mais fácil de ler.
            print("=" * 20)
            print(f"Clima em: {cidade}")
            print("=" * 20)
            print(f"Cidade: {data_clima['cidade']}")
            print(f"Região: {data_clima['regiao']}")
            print(f"País: {data_clima['pais']}")
            print(f"Horário local: {data_clima['horario_local']}")
            print(f"Temperatura: {data_clima['temperatura_celsius']}°C")
            print(f"Sensação térmica: {data_clima['sensacao_termica']}°C")
            print(f"Clima: {data_clima['clima']}")
            print(f"Umidade: {data_clima['umidade']}%")
            print(f"Vento: {data_clima['vento_kmh']} km/h")
            print(f"Direção do vento: {data_clima['direcao_vento_descricao']}")
            print(f"Visibilidade: {data_clima['visibilidade_km']} km")
            print(f"Nuvens: {data_clima['nuvens_percentual']}%")
            print(f"Última atualização: {data_clima['ultima_atualizacao']}")
            print("=" * 20)

            # Retorna o dicionário para depois salvar tudo no JSON.
            return data_clima

        # Se a API respondeu, mas não deu certo, cai aqui.
        print(f"Erro ao obter os dados de {cidade}.")
        print(f"Código de status: {response.status_code}")
        print(f"Resposta da API: {response.text}\n")
        return None

    except requests.Timeout:
        # Esse erro acontece quando a API demora mais que o limite definido no timeout.
        print(f"Tempo limite excedido ao consultar {cidade}.\n")
        return None

    except requests.RequestException as erro:
        # Pega erros ligados à requisição, como falha de internet ou problema na conexão.
        print(f"Erro de conexão ao consultar {cidade}.")
        print(f"Detalhes: {erro}\n")
        return None

    except KeyError as erro:
        # Se algum campo esperado não vier no JSON, o programa avisa em vez de parar do nada.
        print(f"Erro ao processar os dados JSON de {cidade}.")
        print(f"Campo não encontrado: {erro}\n")
        return None

    except Exception as erro:
        # Última proteção para qualquer erro inesperado que não caiu nos casos acima.
        print(f"Erro inesperado ao consultar {cidade}.")
        print(f"Detalhes: {erro}\n")
        return None


# Lista das cidades que serão consultadas.
cidades = [
    "Brasília",
    "Macapá",
    "Belém",
    "São Paulo",
    "Rio de Janeiro"
]

# Aqui ficam guardados apenas os resultados que deram certo.
resultados = []

for cidade in cidades:
    print(f"Buscando clima para: {cidade}...\n")

    # Chama a função e guarda o retorno dela.
    clima = get_weather(cidade)

    # Só adiciona na lista se a consulta realmente retornou dados.
    if clima is not None:
        resultados.append(clima)

    # Pausa entre uma cidade e outra para deixar a leitura mais tranquila.
    time.sleep(4)

# Salva todos os resultados em um arquivo JSON mesmo.
with open("UPN.json", "w", encoding="utf-8") as arquivo:
    json.dump(resultados, arquivo, ensure_ascii=False, indent=4)

print("Consultas finalizadas.")
print("Dados salvos no arquivo UPN.json.")
