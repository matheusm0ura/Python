from src.leilao.dominio import Lance, Leilao, Usuario, Avaliador

user = Usuario("Matheus")
user2 = Usuario("João")

lance_joao = Lance(user2, 9000)
lance_matheus = Lance(user, 10000)

leilao = Leilao("Leilão de carros")
print(leilao.descricao)

leilao.lances.append(lance_matheus)
leilao.lances.append(lance_joao)

for lance in leilao.lances:
    print(f"O usuário {lance.usuario.nome} deu um lance de R$ {lance.valor:.2f}")

avaliador = Avaliador()
avaliador.avalia(leilao)
print(f"Maior lance: {avaliador.maior_lance}\nMenor lance: {avaliador.menor_lance}")
