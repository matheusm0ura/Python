import re
class TelefoneBr:
  
  def __init__(self, telefone):
    if self.valida_numero(telefone):
      self.numero = telefone
    else:
      raise ValueError("Número inválido.")
  
  def valida_numero(self, telefone):
    padrao = "([0-9]{2})([0-9]{4,5})([0-9]{4}$)"
    busca = re.search(padrao, telefone)
    if busca:
      return True
    else:
      return False
  
  def __str__(self):
    padrao = "([0-9]{2})([0-9]{4,5})([0-9]{4})"
    busca = re.search(padrao, self.numero)
    return "({}){}-{}".format(
    busca.group(1), 
    busca.group(2), 
    busca.group(3))
  