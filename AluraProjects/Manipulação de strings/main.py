from extratorUrl import Extrator_url
#import regularEx
url = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator = Extrator_url(url)

VALOR_DOLAR = 5.50

quantidade = int(extrator.get_valor_parametro("quantidade"))

moeda_origem = extrator.get_valor_parametro("moedaOrigem")

moeda_destino = extrator.get_valor_parametro("moedaDestino")

if(moeda_origem == "dolar" and moeda_destino == "real"):
  print(f"R$ {quantidade * VALOR_DOLAR:.2f}")

elif(moeda_origem == "real" and moeda_destino == "dolar"):
  print(f"$ {quantidade / VALOR_DOLAR:.2f}")


