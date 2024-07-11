from models.model import Entrada, TipoEntrada, Grupo_Entrada
import pytest

def test_crear_entrada():
    entrada = Entrada(12)
    assert entrada.tipo == TipoEntrada.NIÑO
    assert entrada.precio == 14

    entrada = Entrada(35)
    assert entrada.tipo == TipoEntrada.ADULTO
    assert entrada.precio == 23

    entrada = Entrada(70)
    assert entrada.tipo == TipoEntrada.JUBILADO
    assert entrada.precio == 18

    entrada = Entrada(1)
    assert entrada.tipo == TipoEntrada.BEBE
    assert entrada.precio == 0
    grupo = Grupo_Entrada()
    grupo.add_entrada(10)
    assert grupo.subtotal_tipo(TipoEntrada.NIÑO) == 14