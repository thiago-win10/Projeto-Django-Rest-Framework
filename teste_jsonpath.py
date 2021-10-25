import requests
import jsonpath

#avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')
#resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
#print(resultados)


#avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')
#nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
#print(nome)


#Todas as notas das avaliações

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')
notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].comentario')
for c in enumerate(notas, +1):
    print(c)


