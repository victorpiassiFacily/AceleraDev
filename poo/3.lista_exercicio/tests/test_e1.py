import pytest
from src.e1 import media


@pytest.mark.parametrize('input, result', [
    ([5, 5, 5, 5], 5),
])
def test_deve_retornar_media_correta(input, result):
    assert media(input) == result


@pytest.mark.parametrize('input, result', [
    ([5, 6, 3, 7], 4)
])
def test_deve_possuir_quatro_notas(input, result):
    assert len(input) == result
