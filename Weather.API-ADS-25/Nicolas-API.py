import requests
import json
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

def traduzir_direcao_vento(sigla):
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
    
    return direcoes.get(sigla, "Direção desconhecida")


#Essa parte do codigo define a função get_weather, que é responsável por fazer a requisição à API de clima, processar os dados recebidos e exibir as informações de forma organizada. A função também inclui tratamento de erros para lidar com possíveis problemas durante a consulta à API ou processamento dos dados.

def get_weather(cidade):
    BASE_URL = "http://api.weatherapi.com/v1/current.json"

    api_key = "f4abfbefbb60416098d230246260705"
    #isso aqui é o dicionário de parâmetros que será enviado na requisição para a API, contendo a chave de acesso, a cidade a ser consultada e o idioma da resposta.
    params = {
        "key": api_key,
        "q": cidade,
        "lang": "pt"
    }
    #Tratamento de erros para garantir que o programa continue funcionando mesmo se ocorrerem problemas durante a consulta à API ou processamento dos dados.

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()

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

            print("=============================================")
            print(f"Clima em: {cidade}")
            print("=============================================")
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
            print("=============================================\n")

            return data_clima

        else:
            print(f"Erro ao obter os dados de {cidade}.")
            print(f"Código de status: {response.status_code}")
            print(f"Resposta da API: {response.text}\n")
            return None
    
    except requests.Timeout:
        print(f"Tempo limite excedido ao consultar {cidade}.\n")
        return None

    except requests.RequestException as erro:
        print(f"Erro de conexão ao consultar {cidade}.")
        print(f"Detalhes: {erro}\n")
        return None

    except KeyError as erro:
        print(f"Erro ao processar os dados JSON de {cidade}.")
        print(f"Campo não encontrado: {erro}\n")
        return None

    except Exception as erro:
        print(f"Erro inesperado ao consultar {cidade}.")
        print(f"Detalhes: {erro}\n")
        return None
#As cidades estão aqui.

cidades = [
    "Brasília",
    "Macapá",
    "Belém",
    "São Paulo",
    "Rio de Janeiro"
]

resultados = []

for cidade in cidades:
    print(f"Buscando clima para: {cidade}...\n")

    clima = get_weather(cidade)

    if clima is not None:
        resultados.append(clima)

    time.sleep(4)  # Aguardar 4 segundos entre as consultas para melhor leitura mesmo.

with open("UPN.json", "w", encoding="utf-8") as arquivo:
    json.dump(resultados, arquivo, ensure_ascii=False, indent=4)

print("Consultas finalizadas.")
print("Dados salvos no arquivo UPN.json.")