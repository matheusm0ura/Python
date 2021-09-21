from src.leilao.dominio import Usuario, Leilao

import pytest


@pytest.fixture
def user():
    return Usuario("Matheus", 100)


@pytest.fixture
def leilao():
    return Leilao("Celular")


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_ele_propor_um_lance(user, leilao):

    user.propoe_lance(leilao, 50)

    assert user.carteira == 50


def test_deve_permitir_propor_lance_quando_o_valor_e_menor_que_o_valor_da_carteira(user, leilao):

    user.propoe_lance(leilao, 1)

    assert user.carteira == 99


def test_deve_permitir_propor_lance_quando_o_valor_e_igual_ao_valor_da_carteira(user, leilao):

    user.propoe_lance(leilao, 100)

    assert user.carteira == 0


def test_nao_deve_permitir_propor_lance_quando_o_valor_e_maior_que_o_da_carteira(user, leilao):
    with pytest.raises(ValueError):

        user.propoe_lance(leilao, 200)
