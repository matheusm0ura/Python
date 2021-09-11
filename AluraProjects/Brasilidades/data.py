from datetime import datetime, timedelta

class Data:
  def __init__(self):
    self.momento = datetime.today()
  
  def __str__(self):
   return self.momento.strftime("%d/%m/%Y %H:%M")

  def mes_cadastro(self):
    meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

    return meses [self.momento.month - 1]
  
  def dia_cadastro(self):
    dias = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
    return dias[self.momento.weekday() - 1]
  
  def tempo_cadastro(self):
    return  (datetime.today() + timedelta(days=30)) - self.momento