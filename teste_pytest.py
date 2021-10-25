import requests
from cursos.models import Curso


class TestCurso:
    headers = {'Authorization': 'Token a1cd3b565c85355dab17777ad9cadad4bfcb9b77'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)
        expected = Curso.objects.count()

        assert cursos.status_code == 200
        breakpoint()
        assert(len(cursos.data))