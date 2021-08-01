from filme import Filme
from serie import Serie
from playlist import Playlist

f1 = Filme("Vingadores", "2014", 240)
f1.dar_like()
f1.dar_like()

f2 = Filme("todo mundo em pânico", "2003", 180)
f2.dar_like()
f2.dar_like()


s1 = Serie("La casa de papel", "2016", 5)
s1.dar_like()


lista = [f1, f2, s1]

play = Playlist("Fim de semana", lista)

print(f"Tamanho da playlist: {len(play)}")

for programa in play:
  print(programa)
  print("\n")

