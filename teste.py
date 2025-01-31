import csv

dicionarios = {}

def org_countrycode():

    with open("countrycodes.csv", newline="", encoding="utf-8") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        
        for linha in leitor:

            if len(linha) >= 3:
                chave = linha[0]
                valor = linha[2]
                if len(linha[1]) <= 2:
                    valor = linha[1]
                
                dicionarios[chave] = valor
    return dicionarios

dicionarios = org_countrycode()

country = input("Insira um país em inglês para saber o coutry code: ")
print(dicionarios[country])


