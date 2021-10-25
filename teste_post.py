import requests

headers = {'Authorization': 'Token a1cd3b565c85355dab17777ad9cadad4bfcb9b77'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
	"titulo": "Matematica Estatistica 56",
	"url": "https://www.udemy.com/course/matematica-estatistica-56/"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)
#print(resultado.json())

#Testando o status code 201 Created

assert resultado.status_code == 201

#Testando se o titulo do curso retorna o mesmo informado
assert resultado.json()['titulo'] == novo_curso['titulo']
