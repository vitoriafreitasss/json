import json

# Uma string no formato de JSON
dados_json = '' \
'{"nome":"Ana", "idade":25, "cidade": "São Paulo" }'

# Convertendo a strig JSON em um dicionario Python

dados_python = json.loads (dados_json)
 
# Agora você pode acessar os dados como um dicionario

print(dados_python["nome"]) # Saida de string
print(dados_python["idade"]) # Saida de inteiro