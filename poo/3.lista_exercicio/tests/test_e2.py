import pytest
from src.e2 import phrase_consonants


@pytest.mark.parametrize('input, result', [
    ("abcdef", ["b", "c", "d", "f"])
])
def test_verificar_retorno_de_vogais_e_consoantes(input, result):
    assert phrase_consonants(input) == result
