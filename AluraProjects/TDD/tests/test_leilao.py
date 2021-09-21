from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.exception import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):  # método do framework para criar o cenário de teste
        self.user = Usuario("Matheus", 500)
        self.lance_matheus = Lance(self.user, 500)

        self.leilao = Leilao("Leilão de carros")

    def test_deve_retornar_o_maior_e_menor_valor_quando_adicionados_em_ordem_crescente(self):
        user2 = Usuario("João", 500)
        lance_joao = Lance(user2, 9000)

        self.leilao.propoe(lance_joao)
        self.leilao.propoe(self.lance_matheus)

        menor_valor_esperado = 9000
        maior_valor_esperado = 10000

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            user2 = Usuario("João", 500)
            lance_joao = Lance(user2, 9000)

            self.leilao.propoe(self.lance_matheus)
            self.leilao.propoe(lance_joao)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_para_o_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_matheus)

        self.assertEqual(10000, self.leilao.menor_lance)
        self.assertEqual(10000, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_leilao_tiver_tres_lances(self):
        user3 = Usuario("Roberto", 500)
        user2 = Usuario("João", 500)

        lance_joao = Lance(user2, 9000)
        lance_roberto = Lance(user3, 12000)

        self.leilao.propoe(lance_joao)
        self.leilao.propoe(self.lance_matheus)
        self.leilao.propoe(lance_roberto)

        self.assertEqual(9000, self.leilao.menor_lance)
        self.assertEqual(12000, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_matheus)

        self.assertEqual(1, len(self.leilao.lances))

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        carlos = Usuario("Carlos", 500)
        lance_do_carlos = Lance(carlos, 12000)

        self.leilao.propoe(self.lance_matheus)
        self.leilao.propoe(lance_do_carlos)

        self.assertEqual(2, len(self.leilao.lances))

    def test_nao_deve_permitir_o_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_matheus_12000 = Lance(self.user, 12000)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_matheus)
            self.leilao.propoe(lance_matheus_12000)


