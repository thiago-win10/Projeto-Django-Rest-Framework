import requests

headers = {'Authorization': 'Token a1cd3b565c85355dab17777ad9cadad4bfcb9b77'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
	"titulo": "Matematica Estatistica 56",
	"url": "https://www.udemy.com/course/matematica-estatistica-56/"
}

#Buscando o curso com o ID 5

curso = requests.get(url=f'{url_base_cursos}5/', headers=headers)
print(curso.json())
