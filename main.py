import requests
import csv
import flask

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
        print(countrycode[country])
        return countrycode[country]
    except Exception as error :
        return f"Erro ao buscar código do país: {error}"
def translate_countryname(country):

    with open("countrynames.csv", newline="", encoding="utf-8") as arquivo_csv2:
        leitor = csv.reader(arquivo_csv2, delimiter=";")
        for linha in leitor:
            if len(linha) >= 2:
                if linha[1].lower() == country.lower():
                    try:
                        print (linha[0])
                        return linha[0]
                    except Exception as error:
                        return f"Erro ao traduzir nome do país: {error}"
def request_location(cidade, pais):
    global api_key
    pais = str(translate_countryname(pais))
    c_code = get_countrycode(countrycode, pais)
    try:
        response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={cidade},{c_code}&limit=1&appid={api_key}").json()
        if isinstance(response, list) and len(response) > 0:
            lat_cidade = response[0]["lat"]
            lon_cidade = response[0]["lon"]
            return lat_cidade, lon_cidade
    except Exception as error:
        return f"Erro ao fazer a requisição de latitude e longitude: {error}"
def request_weather(lat, lon):
    global api_key
    try:
        weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&lang=pt_br").json()
        return weather
    except Exception as error:
        return f"Erro ao fazer a requisição do clima: {error}"
def exibit_weather(response):
    print(f"Nome da cidade: {response["name"]}")

#testes
@app.route("/weather", methods=["GET"])
def response_weather(cidade, pais):
    try:
        lat_cidade, lon_cidade = request_location(cidade, pais)
        weather = request_weather(lat_cidade, lon_cidade)
        return flask.jsonify(weather)
    except Exception as error:
        return flask.jsonify({"error": str(error)})


cidade = input("Insira o nome da cidade que deseja saber o clima: ")
pais = input("Insira o pais dessa cidade: ")


print(weather, "\n\n\n")
exibit_weather(weather)



org_countrycode()
app = Flask(__name__)



