import re

class Extrator_url:
  def __init__(self, url):
    self.url = self.remove_espacos(url)
    self.valida_url()

  def remove_espacos(self, url):
    if type(url) == str:
      return url.strip()
    else:
      return ""
  
  def valida_url(self):
    if self.url == "":
      raise ValueError("A URL está vazia.")
    
    padra_url = re.compile('(http(s)://)?(www.)?bytebank.com(.br)?/cambio')
    match_url = padra_url.match(self.url)
    if not match_url:
      raise ValueError("A URL NÃO é válida.")

  
  def get_url_base(self):
    url_base =self.url[:self.url.find("?")]
    return url_base
  
  def get_url_parametros(self):
    url_parametros = self.url[self.url.find("?") + 1:]
    return url_parametros
  
  def get_valor_parametro(self, parametro_busca):
  
    indice_parametro = self.get_url_parametros().find(parametro_busca)

    indice_valor = indice_parametro + len(parametro_busca) + 1

    indice_e_comercial = self.get_url_parametros().find("&", indice_valor)

    if indice_e_comercial == -1:
      valor = self.get_url_parametros()[indice_valor:]
    else:
      valor =self.get_url_parametros()[indice_valor:indice_e_comercial]
    
    return valor
  
  def __len__(self):
    return(len(self.url))
  
  def __str__(self):
    return f'URL base: {self.get_url_base()}\nParâmetros: {self.get_url_parametros()}'


