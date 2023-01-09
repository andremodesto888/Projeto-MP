""" Import file.
"""
import oito_rainhas


entrada = '00001000', '01000000',\
    '00010000', '00000010',\
    '00100000', '00000001',\
    '00000100', '10000000'


def test_is_solution():
    """
    A entrada é uma solução para o problema.
    """
    assert oito_rainhas.build(entrada) == 1


def test_is_not_solution():
    """
    A entrada não é uma solução para o problema
    """
    assert oito_rainhas.build(entrada) == 0


def test_is_invalid():
    """
    A entrada é inválida
    """
    assert oito_rainhas.build(entrada) == -1
