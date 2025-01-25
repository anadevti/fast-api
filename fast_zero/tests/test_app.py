from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

"""
Esse teste faz uma requisição GET no endpoint / e verifica se o código de status da resposta é 200 e se o conteúdo da resposta é {'message': 'Olá Mundo!'}.
"""
def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange fase 1 - ela monta o ambiente para que o teste possa ser executado

    response = client.get('/')  # Act fase 2 - Agir aqui significa interagir diretamente com a parte do sistema que queremos avaliar, para ver como ela se comporta.

    assert response.status_code == HTTPStatus.OK  # Assert fase 3 - Esta é a etapa de verificar se tudo correu como esperado.
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert