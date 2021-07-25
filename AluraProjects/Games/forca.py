from random import randint
import re

def jogar_forca():
  
  imprime_mensagem("JOGO DA FORCA")
  
  palavra_secreta = ler_arquivo("palavras.txt")
  print(palavra_secreta)
  erros = 0

  letras_acertadas = ["_" for letra in palavra_secreta]
  letras_digitadas = []

  while(True):
    
    mostra_palavra(letras_acertadas)
    
    print("\n")
    chute = verifica_palpite(letras_digitadas)
    
    if(chute in palavra_secreta):
      index = 0
      for letra in palavra_secreta:
        
        if(chute == letra):
          letras_acertadas[index] = letra
        index += 1

    elif(chute not in palavra_secreta):
      erros += 1
      print(f"Você possui {7 - erros} tentativas!")
      desenha_forca(erros)
      
      if(erros == 7):
        mostra_palavra(letras_acertadas)
        imprime_mensagem_perdedor(palavra_secreta)
        break

    if("_" not in letras_acertadas):
      mostra_palavra(letras_acertadas)
      imprime_mensagem_vencedor()      
      break


def mostra_palavra(letras_acertadas):
  print("Palavra: ", end = " ")
  for item in letras_acertadas:
      print(f"[ {item} ]", end = " ")
  print("\n")

def ler_arquivo(nome_arquivo):
  palavras = []
  with open(nome_arquivo, "r") as arquivo:
    for linha in arquivo:
      palavras.append(linha.strip().lower())   

  return palavras[randint(0, len(palavras) - 1)]

def imprime_mensagem(msg):
  print("=" * len(msg))
  print(msg)
  print("=" * len(msg))

def verifica_palpite(letras_digitadas):

    chute = pede_palpite()
    
    while(chute in letras_digitadas or len(chute) < 1 or len(chute) > 1 or checa_splcharacter(chute) or checa_digito(chute)):

       contains_digit = checa_digito(chute)
       contains_special = checa_splcharacter(chute)
       
       if(chute in letras_digitadas):
         print("Essa letra já foi digitada!")
         chute = pede_palpite()
       
       elif(contains_digit):
         print("Números não são permitidos!")
         chute = pede_palpite()
       
       elif(contains_special):
         print("Caracteres especiais não são permitidos.")
         chute = pede_palpite()

       elif(len(chute) < 1 or len(chute) > 1):
         print("Digite apenas uma letra!")
         chute = pede_palpite()
       
    letras_digitadas.append(chute)

    return chute  

def pede_palpite():
  chute = str(input("Digite uma letra: ")).strip().lower()
  return chute

def imprime_mensagem_perdedor(palavra_secreta):
    print("GAME OVER!")
    print(f"A palavra secreta era {palavra_secreta}.")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def checa_splcharacter(chute):
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')
 
    if(string_check.search(chute) == None):
        return False
    else: 
        return True
        
def checa_digito(chute):
  return any(map(str.isdigit, chute))

if(__name__ == "__main__"):
    jogar_forca()    