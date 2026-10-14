import pytest

from src.calculadora import dividir, multiplicar, restar, sumar


def test_sumar_positivos():
    assert sumar(2, 3) == 5


def test_sumar_negativos():
    assert sumar(-1, -1) == -2


def test_restar():
    assert restar(10, 4) == 6


def test_multiplicar():
    assert multiplicar(3, 4) == 12


def test_multiplicar_por_cero():
    assert multiplicar(5, 0) == 0


def test_dividir_normal():
    assert dividir(10, 2) == 5


def test_dividir_decimal():
    assert dividir(1, 4) == 0.25


def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
