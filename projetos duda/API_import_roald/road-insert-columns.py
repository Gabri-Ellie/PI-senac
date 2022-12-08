# Importando biblioteca ".csv", link da documentação: https://docs.python.org/pt-br/3/library/csv.html 
import csv
# Importando biblioteca ".json", link da documentação: https://www.json.org/json-en.html
import json
# Importando biblioteca "requests", responsável pela comunicação com a API .link da documentação: https://pypi.org/project/requests/
import requests
# Importando biblioteca "datetime", formula data e hora local. Link da documentação: https://docs.python.org/3/library/datetime.html
from datetime import datetime

# Aplicando metódo para abrir um arquivo no modo leitura. A partir de agora sempre que eu quiser referenciar esse arquivo, 
# Basta escrever "arquivo"
with open('/home/mariasatelis/Área de Trabalho/API_import_roald/acompanhamento_de_expedicoes.csv', 'r') as arquivo:
# A variável/objeto "leitor" esta recebendo um valor do metódo .reader() 
    df = csv.reader(arquivo, delimiter=',')
# Pulando primeira coluna "uri" pois ela é vazia. O metódo next() apenas pula para o próximo valor
    next(df)
# Quando um comando é executado em um certo número de vezes 
    for linha in df:

# # Criando váriveis que receberão cada um dos elementos de cada linha da tabela 
        schema = linha[1]
        tabela = linha[2]
        coluna = linha[3]      
        descricao = linha[4]
       
# # Try é para tentar rodar o código descrito dentro dele, ou seja, linha 28 até 42. O elemento "except" (linha 44) serve para
# # Caso o código dentro do try apresentar algum erro, seja executado o que esta nas linhas após o "except" 
        try:

# # Payload significa o formato de resposta/comunicação que a API espera. Da forma que o código esta feito os objetos/váriaveis: 
# # {schema}, {tabela}, {coluna} e {descricao}; Serão substituidos pelo o que foi definido nas linhas 21 a 24. 
              
            payload = {
                "rk": f"glue://glue_cluster.redshift_{schema}/{tabela}/{coluna}/_description",
                "description_source": "description",
                "description": f"{descricao}",
                "column_rk": f"glue://glue_cluster.redshift_{schema}/{tabela}/{coluna}",
                "published_tag": "unique_tag",
                "publisher_last_updated_epoch_ms": datetime.now().timestamp()
            }       
            payload = json.dumps(payload)
            print(payload)
          
# # Response: a resposta que a API dará para nós
# # Request: a requisição/comunicação/"carta" que estamos enviando para a API
# # Post: metodo de comunicação com a API, neste caso de criação de registro. 
# # Possíveis metódos utilizados: POST, PUT, DELETE, GET, etc.          
# # Headers-> Authorization: chave necessária para comunicar com a API do roald
# # Verify: parametro responsável por acionar verificação do payload
# # Data: dicionário contendo os dados que serão enviados para a API 
# # Json.dumps: metódo responsável por converter dicionáio phyton para .json(formato de arquivo esperado pelas APIS no geral)

            response = requests.post('https://api-roald.madeiramadeira.com.br/tables/columns/descriptions',
                                     headers={
                                        'Content-Type': 'application/json',
                                        'Authorization':'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtYXJpYS5zYXRlbGlzQG1hZGVpcmFtYWRlaXJhLmNvbS5iciIsImV4cCI6MTY2NjgwOTI5Mn0.cgRoiTWN8prNH10OfxHRc3q-3dBr_NGgk-EX6wmblQ4'},
                                     verify=False, data=payload)
            print(response.text)
            
        except:
            break
            
