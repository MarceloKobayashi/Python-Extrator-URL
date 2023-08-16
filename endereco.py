import re

endereco = "SQSW 302, Bloco J, apartamento 603, Brasília, DF, 70673-210"
padrao = re.compile("[0-9]{5}-{0, 1}[0-9]{3}")
busca = padrao.search(endereco)   # Match

if busca:
    cep = busca.group()
    print(cep)
