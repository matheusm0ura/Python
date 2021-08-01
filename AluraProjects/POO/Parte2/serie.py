from programa import Programa

class Serie(Programa):
  
  def __init__(self, nome, ano, temporadas):
    super().__init__(nome, ano)
    self._temporadas = temporadas
    self._likes = 0
  
  @property
  def temporadas(self):
    return self._temporadas
  
  @temporadas.setter
  def temporadas(self, temporadas):
    self._temporadas = temporadas
  
  def __str__(self):
    return f'Nome: {self._nome}\nAno: {self._ano}\nTemporadas: {self._temporadas}\nLikes: {self._likes}'
  
 