"""Main App."""

import redblacktree
import titulo
import valida
import os

# ÁRVORE DE TÍTULOS
titulos = redblacktree.Tree()
quantidade_cadastrada = 0

# ÁRVORE DE VOTOS
votos = redblacktree.Tree()
while True:
    opcao = int(input("Títulos Cadastrados: %d" % quantidade_cadastrada + '\n'
                      "1 - cadastra" + '\n' +
                      "2 - descadastra" + '\n' +
                      "3 - carregar de um arquivo" + '\n' +
                      "4 - exibir títulos cadastrados" + '\n' + '\n'
                      "Escolha: "))

    if opcao == 1:
        os.system('clear')
        titulos.insert(titulo.Titulo.cadastrar())
        quantidade_cadastrada += 1
    elif opcao == 2:
        os.system('clear')
        titulos.delete(titulos.search(titulo.Titulo.descadastrar()))
        quantidade_cadastrada -= 1
    elif opcao == 3:
        os.system('clear')
        arquivo = os.getcwd() + '/' + input('Nome do arquivo: ')
        # TODO:
        # Carregar títulos (VÁRIOS DE UMA VEZ)
        # lê o arquivo e insere na árvore com um laço
        print('\n')
    elif opcao == 4:
        os.system('clear')
        titulos.inOrderTreeWalk(titulos.getRoot())
        print('\n')


# cadastrar candidatos


'''
# lê um título e um voto
    # valida
    # contabiliza o voto
    # deleta da árvore de títulos
    # insere na árvore de votos

# preencher de uma vez
    # lê automaticamente de um por um
    # valida
    # preenche voto automaticamente (random.choice)

# Sair: destruir todas as estruturas e encerrar o programa.
'''

'''
VOTAR:
Nova votação: dá um “reset” na árvore de votação que guarda os títulos que já
votaram.
    Esse “reset” corresponde à liberação da memória dinamicamente alocada;
Adicionar voto: ler número do título e o voto. Se o número do título é válido
e se ainda
não votou, contabiliza o voto e atualiza a árvore de votação que armazena os
títulos de
quem já votou;
Gerar votos aleatórios (para encher a árvore de votação mais rapidamente):
sempreacionando a operação de inserir mais um elemento na árvore de votação;
validação
'''
# Sair: destruir todas as estruturas e encerrar o programa.
