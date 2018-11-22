"""Tree."""


class Node:
    """Classe Nodo."""

    def __init__(self, data):
        """Construtor do Nodo da Arvore."""
        self.data = data
        self.father = None
        self.leftNode = None
        self.rightNode = None

    def __repr__(self):
        """Plota o dado do no."""
        s = ''
        s += str(self.father) + '\n'
        s += '^' + '\n'
        s += str(self.leftNode) + ' <- '
        s += str(self.data) + ' -> '
        s += str(self.rightNode)
        return s

    def getData(self):
        """Retorna o Dado armazenado no nodo."""
        return self.data

    def setData(self, data):
        """Atribui valor ao Dado do nodo."""
        self.data = data

    def getLeftNode(self):
        """Retorna a referencia do no a esquerda nodo."""
        return self.leftNode

    def setLeftNode(self, data):
        """Atribui valor do no a esquerda."""
        self.leftNode = data

    def getRightNode(self):
        """Retorna o no da direita."""
        return self.rightNode

    def setRightNode(self, data):
        """Atribui o valor do no da direita."""
        self.rightNode = data


class Tree:
    """Tree class."""

    def __init__(self, node):
        """Construtor."""
        self.p = None
        self.node = node
