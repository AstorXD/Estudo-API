import requests
import csv
import flask
from flask_cors import CORS
import waitress

api_key = "b5f546a581ec7e5675a954a64b4e5ddb"
countrycodelist = {}
app = flask.Flask(__name__)
CORS(app)

def org_countrycode():

    #define que está utilizando a variável global
    global countrycodelist

    #abre o arquivo, utilizando with para que seja fechado logo depois de recuperar os dados
    with open("./countrycodes.csv", newline="", encoding="utf-8") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            #garante que terá 3 colunas no mínimo
            if len(linha) >= 3:
                chave = linha[0]
                #algumas linhas estão com a segunda coluna sendo outro dado além do código, isso impede que aconteça de registrar esse dado.
                valor = linha[2]
                if len(linha[1]) <= 2:
                    valor = linha[1]
                countrycodelist[chave.lower()] = valor
def get_countrycode(countrycodelist, country):
    #tratamento de erro em pegar um código de país
    if country is None:
        print("Erro ao buscar código do país:!")
        return None
    country = country.lower()
    try:
        return countrycodelist[country]
    except Exception as error :
        print("Erro ao buscar código do país!")
        return None
def translate_countryname(country):

    with open("./countrynames.csv", newline="", encoding="utf-8") as arquivo_csv2:
        leitor = csv.reader(arquivo_csv2, delimiter=";")
        for linha in leitor:
            if len(linha) >= 2:
                if linha[1].lower() == country.lower():
                        return linha[0]
        print ("Erro ao traduzir nome do país!")
        return None
def request_location(cidade, pais):
    global api_key
    pais = str(translate_countryname(pais))
    print(pais)
    c_code = get_countrycode(countrycodelist, pais)
    try:
        response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={cidade},{c_code}&limit=1&appid={api_key}").json()
        if not response:
            print("Nenhum resultado encontrado")
            return None, None
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
        if not weather:
            return flask.jsonify({"error": "Nenhum resultado encontrado para essas informações."}), 404
        return weather
    except Exception as error:
        return f"Erro ao fazer a requisição do clima: {error}"

org_countrycode()

@app.route("/weather", methods=["GET"])
def response_weather():
    cidade = flask.request.args.get('cidade')
    pais = flask.request.args.get('pais')
    if not cidade:
        return flask.jsonify({"error": "Cidade é uma informação obrigatória!"}), 400
    try:
        lat_cidade, lon_cidade = request_location(cidade, pais)
        if lat_cidade is None or lon_cidade is None:
            return flask.jsonify({"error": "Nenhum resultado encontrado para essas informações."}), 404
        weather = request_weather(lat_cidade, lon_cidade)
        if weather is None:
            return flask.jsonify({"error": "Nenhum resultado encontrado para essas informações."}), 404
        print("Solicitação respondida")
        return flask.jsonify(weather)
    except Exception as Error:
        return flask.jsonify({"error": str(Error)}), 400

if __name__ == "__main__":
    waitress.serve(app, host="0.0.0.0", port=8080, threads=8)








