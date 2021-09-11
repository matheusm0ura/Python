from docs import Documento
from telefone import TelefoneBr
from data import Data
from cep import Cep

import requests

documento = Documento.cria_documento("08296195348")
print(documento)
print()

fone = TelefoneBr("85993067171")
print(fone)
print()

data = Data()
print(data)
print(data.tempo_cadastro())
print()

cep = Cep(62884270)
rua, bairro, localidade, uf = cep.get_info_cep()
print(rua)

#for key in dic:
#  print(f"{key}: {dic[key]}")



