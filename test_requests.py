import requests

#GET Avaliacoes


#headers = {'Authorization': 'Token a1cd3b565c85355dab17777ad9cadad4bfcb9b77'}

#curso = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)
#print(curso.json())

def calcularValorCorrida(ehBandeiraDois, distancia):
    if ehBandeiraDois:
        return distancia * 3.9
    else:
        return distancia * 2.1

rec = calcularValorCorrida('890,00', 2)
print(rec)





