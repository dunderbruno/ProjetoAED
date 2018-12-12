import redblacktree
import titulo
import valida

# ÁRVORE DE TÍTULOS
titulos = redblacktree.Tree()

# ÁRVORE DE VOTOS
votos = redblacktree.Tree()

# EXEMPLO
titulos.insert(titulo.cadastrar())
titulos.inOrderTreeWalk(titulos.getRoot())
print('\n')

# a = titulos.search(numero)
# print(a.getData())
# print(type(a.getData()))

# print(atual)
# node = redblacktree.Node(atual)
# print(valida.valida(node))
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
