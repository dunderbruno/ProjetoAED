"""
Red-Black Tree.

Autores: Bruno Santos
         Jonathas Silva
"""


class Node():
    u"""Unidade básica para funcionamento da Árvore Binária."""

    def __init__(self, data):
        u"""Classe Node é iniciada com argumentos color e data.

        Argumentos:
            data - informação armazenada pelo objeto Node.
        Atributos:
            parent - nó pai
            color  - cor (preto ou vermelho)
            data   - informação armazenada pelo nó
            left   - filho esquerdo
            right  - filho direito
        """
        self.__parent = None
        self.__color  = None
        self.__data   = data
        self.__left   = None
        self.__right  = None

    def getColor(self):
        """Retorna chave de acesso."""
        return self.__color

    def getData(self):
        u"""Retorna conteúdo armazenado."""
        return self.__data

    def getLeft(self):
        """Retorna filho esquerdo."""
        return self.__left

    def getRight(self):
        """Retorna filho direito."""
        return self.__right

    def getParent(self):
        u"""Retorna nó pai."""
        return self.__parent

    def setColor(self, color):
        """Define chave de acesso."""
        self.__color = color

    def setData(self, data):
        u"""Define conteúdo armazenado."""
        self.__data = data

    def setLeft(self, left):
        """Define filho esquerdo."""
        self.__left = left

    def setRight(self, right):
        """Define filho direito."""
        self.__right = right

    def setParent(self, parent):
        u"""Define nó pai."""
        self.__parent = parent


class Tree():
    u"""Árvore Vermelho e Preto."""

    nil = Node(None)
    nil.setColor("black")
    nil.setParent(nil)
    nil.setLeft(nil)
    nil.setRight(nil)
    nil.setData(None)

    def __init__(self):
        """Construtor da arvore."""
        self.__root = self.nil

    def setRoot(self, root):
        u"""Define raiz da árvore."""
        self.__root = root

    def getRoot(self):
        """Retorna a raiz da arvore."""
        return self.__root

    def bigger(self, h1, h2):
        """Retorna o maximo da altura da arvore."""
        if h1 > h2:
            return h1+1
        else:
            return h2+1

    def height(self, x):
        """Altura da arvore."""
        if x is None:
            return -1
        h1 = self.height(x.getLeft())
        h2 = self.height(x.getRight())
        return self.bigger(h1, h2)

    def calFatorBalance(self, x):
        """Calcala o fator de balanceamento das subarvores."""
        esq = x.getEsquerdo()
        dir = x.getDireito()
        return self.height(esq) - self.height(dir)

    def minimum(self, node):
        """Retorna o minino daquele no."""
        if node is not None:
            while node.getLeft() is not None:
                node = node.getLeft()
            return node.getData()

    def maximum(self, node):
        """Retorna o maximo daquel no."""
        if node is not None:
            while node.getRight() is not None:
                node = node.getRight()
            return node.getData()

    def successor(self, x):
        """Retorna o sucessor."""
        if x is not None:
            if x.getRight() is not None:
                return self.minimum(x.getRight())
            else:
                father = x.getParent()
                while father is not None and x is father.getRight():
                    x = father
                    father = x.getParent()
                    return father

    def antecessor(self, x):
        """Retorna o antecessor."""
        if x.getLeft() is not None:
            return self.maximum(x.getLeft())
        y = x.getParent()
        while (y is not None) and (x == y.getLeft()):
            x = y
            y = y.getParent()
            return y

    def preOrderTreeWalk(self, x):
        """Plota arvore em preOrdem."""
        if x is not None:
            print(x.getData(), end = " ")
            self.preOrderTreeWalk(x.getLeft())
            self.preOrderTreeWalk(x.getRight())

    def inOrderTreeWalk(self, x):
        """Plota arvore em ordem."""
        if x is not None:
            self.inOrderTreeWalk(x.getLeft())
            print(x.getData(), end = " ")
            self.inOrderTreeWalk(x.getRight())

    def postOrderTreeWalk(self, x):
        """Plota arvore em posOrdem."""
        if x is not None:
            self.postOrderTreeWalk(x.getLeft())
            self.postOrderTreeWalk(x.getRight())
            print(x.getData(), end = " ")

    def search(self, k):
        """Busca e retorna o no."""
        x = self.getRoot()
        while x is not None and k != x.getData():
            if k < x.getData():
                x = x.getLeft()
            else:
                x = x.getRight()
        return x

    def leftRotate(self, x):
        """Rotaçao simples a esquerda."""
        y = x.getRight()
        x.setRight(y.getLeft())
        y.getLeft().setParent(x)
        y.setParent(x.getParent())
        if x.getParent() is None:
            self.setRoot(y)
        elif x is x.getParent().getLeft():
            x.getLeft().setParent(y)
        else:
            x.getRight().setParent(y)
        y.setLeft(x)
        x.setParent(y)

    def rightRotate(self, x):
        """Rotaçao simples a direita."""
        y = x.getLeft()
        x.setLeft(y.getRight())
        y.getRight().setParent(x)
        y.setParent(x.getParent())
        if x.getParent() is None:
            self.setRoot(y)
        elif x is x.getParent().getRight():
            x.getRight().setParent(y)
        else:
            x.getLeft().setParent(y)
        y.setRight(x)
        x.setParent(y)

    def insert(self, z):
        """Insere um novo no."""
        z = Node(z)
        y = self.nil
        x = self.getRoot()
        while x is not self.nil:
            y = x
            if z.getData() < x.getData():
                x = x.getLeft()
            else:
                x = x.getRight()
        z.setParent(y)
        if y == self.nil:
            self.setRoot(z)
        elif z.getData() < y.getData():
            y.setRight(z)
        else:
            y.setRight(z)
        z.setLeft(self.nil)
        z.setRight(self.nil)
        z.setColor("red")
        self.insertFixUp(z)

    def insertFixUp(self, z):
        while z.getParent().getColor() == 'red':
            if z.getParent() == z.getParent().getParent().getEsquerdo()
                y = z.getParent().getParent().getRight()
                if y.getColor() == 'red':
                    z.getParent().setColor('black')
                    y.setColor('black')
                    z.getParent().getParent().setColor('red')
                    z = z.getParent().getParent()
                else:
                    if z == z.getParent().getRight():
                        z = z.getParent()
                        self.leftRotate(z)
                    z.getParent().setColor('black')
                    z.getParent().getParent().setColor('red')
                    self.rightRotate(z.getParent().getParent())
            else:
                y = z.getParent().getParent().getLeft()
                if y.getColor() == 'red':
                    z.getParent().setColor('black')
                    y.setColor('black')
                    z.getParent().getParent().setColor('red')
                    z = z.getParent().getParent()
                else:
                    if z == z.getParent().getLeft():
                        z = z.getParent()
                        self.rightRotate(z)
                    z.getParent().setColor('black')
                    z.getParent().getParent().setColor('red')
                    self.leftRotate(z.getParent().getParent())
        self.getRoot().setColor('black')

    def transplant(self, u, v):
        if u.getParent() is self.nil:
            self.setRoot(v)
        elif u is u.getParent().getLeft():
            u.getParent().setLeft(v)
        else:
            u.getParent().setRight(v)
