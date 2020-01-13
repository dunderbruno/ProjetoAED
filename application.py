u"""Projeto 3: Eleições – Contagem e Checagem de Votos.

Nas nossas eleições é sabido que são utilizadas urnas eletrônicas.
É desejado a construção de um sistema que consiga contar os votos e checar
quais os títulos que realizaram o processo de votação e os que não votaram.
Algumas medidas a serem tomadas são: verificar no momento que um indivíduo
vota se o título de eleitor dele é válido e, verificar também, se este eleitor
ainda não votou.

    Alunos: Bruno Olimpio dos Santos
            Jonathas Felipe da Silva
"""

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

candidatos = {}  # armazena os candidatos no formato {numero: [nome, votos]}
numeros = []     # guarda o número dos candidatos para usar em random.choice()

# CADASTRAMENTO DE TÍTULOS DE ELEITOR
os.system('clear')
while True:
    opcao = int(input("Títulos Cadastrados: %d" % quantidade_cadastrada+'\n\n' +
                      "1 - Cadastrar título" + '\n' +
                      "2 - Descadastrar título" + '\n' +
                      "3 - Carregar de um arquivo" + '\n' +
                      "4 - Exibir títulos cadastrados" + '\n' + '\n'
                      "5 - Finaliza cadastro de títulos" + '\n' + '\n'
                      "Escolha: "))

    if opcao == 1:
        os.system('clear')
        titulos.insert(titulo.Titulo.cadastrar())
        quantidade_cadastrada += 1
    elif opcao == 2:
        os.system('clear')
        if not titulos.is_empty():
            eliminar = titulos.search(titulo.Titulo.descadastrar())
            # quando um ítem não é encontrado a função search retorna 'nil'
            # para não apagar a folha é feita a verificação abaixo
            if eliminar is not titulos.nil:
                titulos.delete(eliminar)
                quantidade_cadastrada -= 1
            else:
                print('Titulo nao encontrado!')
        else:
            print('Árvore vazia!')
    elif opcao == 3:
        os.system('clear')
        try:
            arquivo = input('Nome do arquivo: ')
            with open(arquivo) as lista:
                for i in lista.readlines():
                    titulos.insert(titulo.Titulo(i[0:8], i[8:11], i[11:-1]))
                    # ultimo slice vai até -1 para evitar o '\n'
                    quantidade_cadastrada += 1
            print('\n')
        except Exception as exc:
            print('\nArquivo não encontrado!\n')
    elif opcao == 4:
        os.system('clear')
        titulos.in_order_tree_walk(titulos.get_root())
        print('\n')
    elif opcao == 5:
        os.system('clear')
        break

# CADASTRAMENTO DE CANDIDATOS
while True:
    opcao = int(input("1 - Cadastrar canditado" + '\n' +
                      "2 - Deletar canditado" + '\n' +
                      "3 - Listar candidatos" + '\n' +
                      "4 - Finalizar cadastro de candidatos" + '\n' + '\n' +
                      "Escolha: "))

    if opcao == 1:  # cadastrar canditado
        os.system('clear')
        numero = int(input('Número: '))
        nome = input('Nome: ')
        candidatos[numero] = [nome, 0]
        numeros.append(numero)
    elif opcao == 2:  # Deletar candidato
        os.system('clear')
        numero = int(input('Digite o número a ser apagado: '))
        del candidatos[numero]
    elif opcao == 3:  # listar candidatos
        os.system('clear')
        for i in candidatos:
            print(i, '-', candidatos[i][0])
        print('\n')
    elif opcao == 4:  # encerrar o loop
        os.system('clear')
        break

# VOTAÇÃO
while True:
    opcao = int(input("\nVotos registrados: %d" % votos_registrados + '\n'
                      "1 - Nova votação" + '\n' +
                      "2 - Adicionar voto" + '\n' +
                      "3 - Gerar votos aleatórios" + '\n' +
                      "4 - Apresentar resultado parcial" + '\n' +
                      "5 - Sair" + '\n' + '\n' +
                      "Escolha: "))

    if opcao == 1:
        os.system('clear')
        votos = redblacktree.Tree()
        votos_registrados = 0
        for i in candidatos:
            candidatos[i][1] = 0
        print('Árvore de Votação zerada.')
        time.sleep(1)
    elif opcao == 2:  # Adiciona um voto
        os.system('clear')
        entrada = input('Título de eleitor: ')
        eleitor = titulos.search(entrada)
        if eleitor is not titulos.nil:
            if valida.valida(eleitor) and (votos.search(entrada) is votos.nil):
                voto = int(input('Voto: '))
                titulos.delete(eleitor)
                votos.insert(eleitor.get_data().getNumero())
                candidatos[voto][1] += 1
                votos_registrados += 1
            else:
                print('Título Inválido!')
        else:
            print('Título não encontrado!')
    elif opcao == 3:  # Gerar votos aleatórios(para encher a árvore de votação)
        os.system('clear')
        while not titulos.is_empty():
            titulo = titulos.minimum(titulos.get_root())
            if valida.valida(titulo) and (votos.search(titulo.get_data()) is votos.nil):
                # verifica que o título é válido e que
                # não consta na árvore de votação (se search retorna votos.nil)
                titulos.delete(titulo)
                votos.insert(titulo.get_data().getNumero())
                voto = (random.choice(numeros))
                candidatos[voto][1] += 1
                votos_registrados += 1
            else:
                titulos.delete(titulo)
    elif opcao == 4:  # Apresentar o resultado parcial da eleição
        os.system('clear')
        for i in candidatos:
            print(i, '-', candidatos[i][0], ': ', candidatos[i][1])
    elif opcao == 5:  # Destrói todas as estruturas e encerra o programa.
        os.system('clear')
        titulos = redblacktree.Tree()
        votos = redblacktree.Tree()
        sys.exit()
