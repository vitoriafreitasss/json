nome = input("Digite o nome: ")

email = input("Digite o e-mail:")


import json

pythonValue = {'email': email,'name': nome,}

stringofJsonData = json.dumps(pythonValue)

print(stringofJsonData)

with open("pessoa.json", "a") as arquivo:
    arquivo.write(stringofJsonData+",\n")