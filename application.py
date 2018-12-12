import redblacktree
import titulo
import valida

# ÁRVORE DE TÍTULOS
titulos = redblacktree.Tree()

# ÁRVORE DE VOTOS
votos = redblacktree.Tree()

numero = input('Cadastrar Título: ')
atual = titulo.Titulo(numero[0:8], numero[8:11], numero[11:])

print(atual)
'''
O cadastramento de títulos de eleitor possuem as seguintes opções:
• Cadastrar título;
• Descadastrar título ;
• Carregar títulos (VÁRIOS DE UMA VEZ)
'''

# cadastrar candidatos


# VOTAR:
    #Nova votação: dá um “reset” na árvore de votação que guarda os títulos que já votaram.
    #Esse “reset” corresponde à liberação da memória dinamicamente alocada;
    #• Adicionar voto: ler número do título e o voto. Se o número do título é válido e se ainda
    #não votou, contabiliza o voto e atualiza a árvore de votação que armazena os títulos de
    #quem já votou;
    #• Gerar votos aleatórios (para encher a árvore de votação mais rapidamente): sempre
    #acionando a operação de inserir mais um elemento na árvore de votação;
    # validação

# Sair: destruir todas as estruturas e encerrar o programa.
