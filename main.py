import requests
import csv

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





#apenas testes
org_countrycode()
cidade = input("Insira o nome da cidade que deseja saber o clima: ")
pais = input("Insira o pais dessa cidade: ")
print(get_countrycode(countrycode, pais))


r = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={b5f546a581ec7e5675a954a64b4e5ddb}")

data = r.json()

print (data)

