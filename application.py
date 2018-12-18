"""Main App."""

import redblacktree
import titulo
import valida
import os
import time
import sys
import random

# ÁRVORE DE TÍTULOS
titulos = redblacktree.Tree()
quantidade_cadastrada = 0

# ÁRVORE DE VOTOS
votos = redblacktree.Tree()
votos_registrados = 0

os.system('clear')
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
        try:
            arquivo = input('Nome do arquivo: ')
            with open(arquivo) as lista:
                for i in lista.readlines():
                    titulos.insert(titulo.Titulo(i[0:8], i[8:11], i[11:-1]))
                    quantidade_cadastrada += 1
            print('\n')
        except Exception as exc:
            print('\nArquivo não encontrado!\n')
    elif opcao == 4:
        os.system('clear')
        titulos.inOrderTreeWalk(titulos.getRoot())
        print('\n')
    elif opcao == 5:
        os.system('clear')
        break

candidatos = {}
numeros = []


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
        numeros.append(numero)
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

    if opcao == 1:
        os.system('clear')
        votos = redblacktree.Tree()
        print('Árvore de Votação zerada')
        time.sleep(3)
    elif opcao == 2:  # votar
        os.system('clear')
        entrada = input('Título de eleitor: ')
        eleitor = titulos.search(entrada)
        if eleitor is not titulos.nil:
            if valida.valida(eleitor):
                voto = int(input('Voto: '))
                titulos.delete(eleitor)
                votos.insert(eleitor.getData().getNumero())
                candidatos[voto][1] += 1
                votos_registrados += 1
            else:
                print('Título Inválido!')
        else:
            print('Título não encontrado!')
    elif opcao == 3:  # simulação
        os.system('clear')
        while not titulos.isEmpty():
            titulo = titulos.minimum(titulos.getRoot())
            if valida.valida(titulo):
                titulos.delete(titulo)
                votos.insert(titulo.getData().getNumero())
                voto = (random.choice(numeros))
                candidatos[voto][1] += 1
                votos_registrados += 1
            else:
                titulos.delete(titulo)
    elif opcao == 4:
        os.system('clear')
        for i in candidatos:
            print(i, '-', candidatos[i][0], 'Votos: ', candidatos[i][1])
    elif opcao == 5:
        os.system('clear')
        titulos = redblacktree.Tree()
        votos = redblacktree.Tree()
        sys.exit()
