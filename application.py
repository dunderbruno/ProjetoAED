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
                      "1 - Cadastrar título" + '\n' +
                      "2 - Descadastrar título" + '\n' +
                      "3 - Carregar de um arquivo" + '\n' +
                      "4 - Exibir títulos cadastrados" + '\n' + '\n'
                      "5 - Finaliza cadastro" + '\n' + '\n'
                      "Escolha: "))

    if opcao == 1:
        os.system('clear')
        titulos.insert(titulo.Titulo.cadastrar())
        quantidade_cadastrada += 1
    elif opcao == 2:
        os.system('clear')
        if not titulos.isEmpty():
            eliminar = titulos.search(titulo.Titulo.descadastrar())
            if eliminar is not titulos.nil:
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

candidatos = {}

while True:
    opcao = int(input("Votos registrados: %d" % votos_registrados + '\n'
                      "1 - Cadastrar canditado" + '\n' +
                      "2 - Deletar canditado" + '\n' +
                      "3 - Listar candidatos" + '\n' +
                      "4 - sair" + '\n' + '\n' +
                      "Escolha: "))

    if opcao == 1:  # cadastrar canditado
        os.system('clear')
        numero = int(input('Número: '))
        nome = input('Nome: ')
        candidatos[numero] = [nome, 0]
    elif opcao == 2:
        os.system('clear')
        numero = int(input('Digite o número a ser apagado: '))
        del candidatos[numero]
    elif opcao == 3:
        os.system('clear')
        for i in candidatos:
            print(i, '-', candidatos[i][0])
    elif opcao == 4:
        os.system('clear')
        break

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
