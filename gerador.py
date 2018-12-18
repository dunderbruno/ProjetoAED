u"""Gerador de Títulos."""

arquivo = open('titulos.txt', 'a')

for i in range(99990001, 99991001):
    linha = str(i)+'LLL'+'ooo'+'\n'
    arquivo.write(linha)

arquivo.close()
