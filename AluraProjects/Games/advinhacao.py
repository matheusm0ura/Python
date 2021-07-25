from random import randint

def jogar_adivinhacao():
  imprime_mensagem("JOGO DA ADIVINHAÇÃO")

  numero_secreto = randint(1, 101)
  print(numero_secreto)

  pontuacao_inicial = 1000

  count = 0

  while True:
    
    resp = pede_numero()
    
    if(numero_secreto == resp):
      print("ACERTOU!")
      count += 1
      print(f"TENTATIVAS: {count}")
      print(f"Total de pontos feitos: {pontuacao_inicial}")
      print("\n")
      break
    
    else:
      if(resp < numero_secreto):
        print("Digite um valor MAIOR!")
      
      if(resp > numero_secreto):
        print("Digite um número MENOR!")
      
      if(pontuacao_inicial < 0):
        print("GAME OVER! SEUS PONTOS FICARAM NEGATIVOS!")
        break
      
      pontuacao_inicial = calcula_pontos(numero_secreto, resp, pontuacao_inicial)
      
      print("ERROU!")
      count += 1
      print("\n")

def imprime_mensagem(msg):
  print("=" * len(msg))
  print(msg)
  print("=" * len(msg))

def pede_numero():
  print("\n")
  resp = str(input("Digite um número entre 1 e 100: "))
  
  while not resp.isnumeric():
    print("Letras não são permitidas.")
    resp = str(input("Digite um número: "))
  resp = int(resp)
  
  while (resp < 1 or resp > 100):
    print("Número inválido.")
    resp = int(input("Digite um número entre 1 e 100: "))
  
  return resp

def calcula_pontos(numero_secreto, resp, pontuacao_inicial):
  pontos_perdidos = abs(numero_secreto - resp)
  pontuacao_inicial -= pontos_perdidos
  
  return pontuacao_inicial

if(__name__ == "__main__"):
  jogar_adivinhacao()      
