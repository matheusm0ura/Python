from programa import Programa

class Filme(Programa):
  
  def __init__(self, nome, ano, duracao):
    super().__init__(nome, ano)
    self._duracao = duracao
    self._likes = 0
  
  @property
  def duracao(self):
    return self._duracao
  
  @duracao.setter
  def duracao(self, duracao):
    self._duracao = duracao
  
  def __str__(self):
    return f'Nome: {self._nome}\nAno: {self._ano}\nDuração: {self._duracao}\nLikes: {self._likes}'
  

    
  