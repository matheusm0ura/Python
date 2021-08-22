import re
#{} - quantificadores: dizem quantas vezes um grupo aparece na str
#[] - grupo: representa um conjunto de opções para o caractere.
#() - correspondência exata.
#? - pode existir ou não (pode ser substituído por {0, 1})
#Search() - usado para procurar o padrão dentro da string 
#Match() - usado para verificar se o padrão bate com o da string

url = "bytebank.com.br/cambio"

endereco = "Rua Jose Francisco de Sá, 129, Fortaleza-CE, Brasil, 62344-904"

dados = "Rafaela Brasil, CPF: 718.457.190-88"

padra_url = re.compile('(http(s)://)?(www.)?bytebank.com(.br)?/cambio')

pardrao_cep = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

padrao_cpf = re.compile("[0-9]{3}[.]{0,1}[0-9]{3}[.]{0,1}[0-9]{3}[.]{0,1}[-]{0,1}[0-9]{2}")

busca_cep = pardrao_cep.search(endereco)

busca_cpf = padrao_cpf.search(dados)

match_url = padra_url.match(url)

if busca_cep:
  cep = busca_cep.group()
  print(f"CEP: {cep}")

elif not busca_cep:
  print("CEP não encontrado.")

if busca_cpf:
  print(f"CPF: {busca_cpf.group()}")

elif not busca_cpf:
  print("CPF não encontrado.") 

if match_url:
  print("A URL é válida")

elif not match_url:
  print("A URL NÁO é válida.")