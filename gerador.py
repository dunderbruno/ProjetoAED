u"""Gerador de Títulos."""

arquivo = open('titulos.txt', 'a')

for i in range(55550001, 55551001):
    linha = str(i)+'333'+'4444'+'\n'
    arquivo.write(linha)

arquivo.close()
