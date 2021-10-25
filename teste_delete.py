import requests

headers = {'Authorization': 'Token a1cd3b565c85355dab17777ad9cadad4bfcb9b77'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=f'{url_base_cursos}5/', headers=headers)

#Testando o código HTTP
#assert resultado.status_code == 204

#Testando se o tamanho do conteudo retorna 0
#assert len(resultado.text) == 0

#print(resultado.json())



