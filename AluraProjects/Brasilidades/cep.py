import requests

class Cep:
  
  def __init__(self, cep):
    cep = str(cep)
    if self.cep_valido(cep):
      self.cep = cep
    else:
      raise ValueError("CEP inválido!")
  
  def cep_valido(self, cep):
    if len(cep) == 8:
      return True
    else:
      return False
  
  def get_info_cep(self):
    url = f"https://viacep.com.br/ws/{self.cep}/json/"
    r = requests.get(url)
    dados = r.json()
    return (
      dados['logradouro'],
      dados['bairro'],
      dados['localidade'],
      dados['uf']
    )
  
  def __str__(self):
    return f"{self.cep[:5]}-{self.cep[5:]}"