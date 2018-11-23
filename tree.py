"""Tree."""


class Node:
    """Classe Nodo."""

    def __init__(self, key, data):
        """Construtor do Nodo da Arvore."""
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        """Plota o dado do no."""
        s = ''
        s += str(self.parent) + '\n'
        s += '^' + '\n'
        s += str(self.left) + ' <- '
        s += str(self.data) + ' -> '
        s += str(self.right)
        return s

    def getKey(self):
        """Retorna a chave de acesso."""
        return self.key

    def setKey(self, key):
        """Atribui a chave de acesso."""
        self.key = key

    def getData(self):
        """Retorna o Dado armazenado no nodo."""
        return self.data

    def setData(self, data):
        """Atribui valor ao Dado do nodo."""
        self.data = data

    def getLeft(self):
        """Retorna a referencia do no a esquerda nodo."""
        return self.left

    def setLeft(self, data):
        """Atribui valor do no a esquerda."""
        self.left = data

    def getRight(self):
        """Retorna o no da direita."""
        return self.right

    def setRight(self, data):
        """Atribui o valor do no da direita."""
        self.right = data

    def getParent(self):
        """Retorna o no pai."""
        return self.parent

    def setParent(self, parent):
        """Define no pai."""
        self.parent = parent

class Tree:
    """Tree class."""

    def __init__(self):
        """Construtor."""
        self.p = None