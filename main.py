import requests
import csv

countrycode = {}

def org_countrycode():

    dicionarios = {}

    with open("countrycodes.csv", newline="", encoding="utf-8") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        
        for linha in leitor:

            if len(linha) >= 3:
                chave = linha[0]
                valor = linha[2]
                if len(linha[1]) <= 2:
                    valor = linha[1]
                
                dicionarios[chave.lower()] = valor
    return dicionarios
countrycode = org_countrycode()
def get_countrycode(countrycode, country):
    country = country.lower()
    try:
        return countrycode[country]
    except Exception as error :
        return f"Erro ao buscar código do país: {error}"

print(get_countrycode(countrycode, "Brazil"))







cidade = input("Insira o nome da cidade que deseja saber o clima: ")



r = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={b5f546a581ec7e5675a954a64b4e5ddb}")

data = r.json()

print (data)

