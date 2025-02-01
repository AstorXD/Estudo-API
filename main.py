import requests
import csv

api_key = "b5f546a581ec7e5675a954a64b4e5ddb"
countrycode = {}

def org_countrycode():

    #define que está utilizando a variável global
    global countrycode

    #abre o arquivo, utilizando with para que seja fechado logo depois de recuperar os dados
    with open("countrycodes.csv", newline="", encoding="utf-8") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            #garante que terá 3 colunas no mínimo
            if len(linha) >= 3:
                chave = linha[0]
                #algumas linhas estão com a segunda coluna sendo outro dado além do código, isso impede que aconteça de registrar esse dado.
                valor = linha[2]
                if len(linha[1]) <= 2:
                    valor = linha[1]
                countrycode[chave.lower()] = valor
def get_countrycode(countrycode, country):
    #tratamento de erro em pegar um código de país
    country = country.lower()
    try:
        return countrycode[country]
    except Exception as error :
        return f"Erro ao buscar código do país: {error}"
def translate_countryname(country):

    with open("countrycodes.csv", newline="", encoding="utf-8") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            if len(linha) >= 2:
                if linha[1] == country:
                    try:
                        return linha[0]
                    except Exception as error:
                        return f"Erro ao traduzir nome do país: {error}"

#apenas testes
org_countrycode()
cidade = input("Insira o nome da cidade que deseja saber o clima: ")
pais = input("Insira o pais dessa cidade: ")
pais = str(translate_countryname(pais))
c_code = get_countrycode(countrycode, pais)
response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={cidade},{c_code}&limit=1&appid={api_key}").json()
lat_cidade = "Não foi possível recuperar a latitude"
lon_cidade = "Não foi possível recuperar a longitude"
if isinstance(response, list) and len(response) > 0:
    try:
        lat_cidade = response[0]["lat"]
        lon_cidade = response[0]["lon"]
    except Exception as error:
        lat_cidade = "Não foi possível recuperar a latitude"
        lon_cidade = "Não foi possível recuperar a longitude"
print (response)
print (lat_cidade)
print (lon_cidade)
weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat_cidade}&lon={lon_cidade}&appid={api_key}").json()
print(weather)