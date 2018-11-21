"""Tree."""


class Node:
    """Classe Nodo."""

    def __init__(self, data):
        """Construtor do Nodo da Arvore."""
        self.data = data
        self.leftNode = None
        self.rightNode = None

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

    def __init__(self, data):
        """Construtor."""
        self.p = None
        self.data = data
