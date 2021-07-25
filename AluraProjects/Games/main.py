from advinhacao import jogar_adivinhacao
from forca import jogar_forca

print("[1] Jogo da adivinhação\n"
"[2] Jogo da forca\n")

op = str(input("Opção: "))
while(op not in "12"):
  op = str(input("Opção: "))

if(op == "1"):
  jogar_adivinhacao()
elif(op == "2"):
  jogar_forca()