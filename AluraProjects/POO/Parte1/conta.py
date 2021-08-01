class Conta:

  def __init__(self, numero, titular, saldo, limite):
    self.__numero = numero
    self.__titular = titular
    self.__saldo = saldo
    self.__limite = limite

  @property
  def numero(self):
    return self.__numero

  @property
  def titular(self):
    return self.__titular   
  
  @titular.setter
  def titular(self, titular):
    self.__titular = titular
  
  @property
  def saldo(self):
    return self.__saldo
  
  @saldo.setter
  def saldo(self, saldo):
    self.__saldo = saldo

  @property
  def limite(self):
    return self.__limite
  
  @limite.setter
  def limite(self, limite):
    self.__limite = limite
  

  def deposita(self, valor):
    self.__saldo += valor
  
  def saca(self, valor):
    if(valor <= self.__saldo):
      self.__saldo -= valor
    
    elif(valor > self.__saldo and valor <= self.__saldo + self.__limite ):
      aux = valor - self.__saldo
      self.__saldo -= self.__saldo
      self.__limite -= aux

    else:
      print("O valor é maior do que a soma do limite disponível mais o saldo para saque.")

  def extrato(self):
    print(f"O saldo do titular {self.__titular} é {self.__saldo}")

  def transfere(self, valor, destino):
    self.saca(valor)
    destino.deposita(valor)


