import pytest
from src.e7 import Data


@pytest.mark.parametrize('input, result', [
    ((11, 8, 2001), "11/8/2001")
])
def test_verificar_se_o_texto_esta_certo(input, result):
    assert str(Data(input[0], input[1], input[2])) == result


@pytest.mark.parametrize('input, result', [
    ((11, 8, 2001), 3)
])
def test_verificar_se_existem_3_entradas(input, result):
    assert len(input) == result
