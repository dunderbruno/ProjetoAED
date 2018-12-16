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
votos_registrados = 0

while True:
    opcao = int(input("Títulos Cadastrados: %d" % quantidade_cadastrada + '\n'
                      "1 - cadastra" + '\n' +
                      "2 - descadastra" + '\n' +
                      "3 - carregar de um arquivo" + '\n' +
                      "4 - exibir títulos cadastrados" + '\n' + '\n'
                      "5 - finaliza cadastro" + '\n' + '\n'
                      "Escolha: "))

    if opcao == 1:
        os.system('clear')
        titulos.insert(titulo.Titulo.cadastrar())
        quantidade_cadastrada += 1
    elif opcao == 2:
        os.system('clear')
        if not titulos.isEmpty():
            eliminar = titulos.search(titulo.Titulo.descadastrar())
            if not eliminar is titulos.nil:
                titulos.delete(eliminar)
                quantidade_cadastrada -= 1
            else:
                print('Titulo nao encontrado!')
        else:
            print('esta vazia!')
    elif opcao == 3:
        os.system('clear')
        arquivo = input('Nome do arquivo: ')
        with open(arquivo) as lista:
            for i in lista.readlines():
                titulos.insert(titulo.Titulo(i[0:8], i[8:11], i[11:]))
                quantidade_cadastrada += 1
        print('\n')
    elif opcao == 4:
        os.system('clear')
        titulos.inOrderTreeWalk(titulos.getRoot())
        print('\n')
    elif opcao == 5:
        os.system('clear')
        break

# TODO:
# cadastrar candidatos

while True:
    opcao = int(input("Votos registrados: %d" % votos_registrados + '\n'
                      "1 - nova votação" + '\n' +
                      "2 - adicionar voto" + '\n' +
                      "3 - gerar votos aleatórios" + '\n' +
                      "4 - apresentar resultado parcial" + '\n' +
                      "5 - sair" + '\n' + '\n' +
                      "Escolha: "))

    if opcao == 1:  # votar
        os.system('clear')
        eleitor = titulos.search(input('Título de eleitor: '))
        if valida(eleitor):
            # TODO: exibir lista de candidatos(laço for)
            voto = input('Voto: ')
            # TODO:  contabiliza o voto
            titulos.delete(eleitor)
            votos.insert(str(eleitor))
            votos_registrados += 1
    elif opcao == 2:  # simulação
        os.system('clear')
        # preencher de uma vez
        # lê automaticamente de um por um
        # valida
        # preenche voto automaticamente (random.choice)
    elif opcao == 3:
        os.system('clear')
        # Sair: destruir todas as estruturas e encerrar o programa.
        break


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
