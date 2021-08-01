class Playlist:
  
  def __init__(self, nome, programas):
    self._nome = nome
    self._programas = programas
  
  def __getitem__(self, item):
    return self._programas[item]
  
  def __len__(self):
    return len(self._programas)
  

    