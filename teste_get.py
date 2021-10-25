import requests

headers = {'Authorization': 'Token a1cd3b565c85355dab17777ad9cadad4bfcb9b77'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=f'{url_base_cursos}8/', headers=headers)
print(resultado.json())



