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
        """
        Define chave de acesso.
        ex:
        x.setColor('red')
        """
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


    def __init__(self):
        """Construtor da arvore."""
        self.nil = Node(None)
        self.nil.setColor('black')
        self.nil.setParent(self.nil)
        self.nil.setLeft(self.nil)
        self.nil.setRight(self.nil)
        self.__root = self.nil

    def setRoot(self, root):
        u"""Define raiz da árvore."""
        self.__root = root

    def getRoot(self):
        """Retorna a raiz da arvore."""
        return self.__root

    def minimum(self, node):
        """Retorna o minino daquele no."""
        if node is not self.nil:
            while node.getLeft() is not self.nil:
                node = node.getLeft()
            return node

    def maximum(self, node):
        """Retorna o maximo daquel no."""
        if node is not self.nil:
            while node.getRight() is not self.nil:
                node = node.getRight()
            return node

    def successor(self, x):
        """Retorna o sucessor."""
        if x is not self.nil:
            if x.getRight() is not self.nil:
                return self.minimum(x.getRight())
            else:
                father = x.getParent()
                while (father is not self.nil) and (x is father.getRight()):
                    x = father
                    father = x.getParent()
                    return father

    def preOrderTreeWalk(self, x):
        """Plota arvore em preOrdem."""
        if x is not self.nil:
            print(x.getData(), end = " ")
            self.preOrderTreeWalk(x.getLeft())
            self.preOrderTreeWalk(x.getRight())

    def inOrderTreeWalk(self, x):
        """Plota arvore em ordem."""
        if x is not self.nil:
            self.inOrderTreeWalk(x.getLeft())
            print(x.getData(), end = " ")
            self.inOrderTreeWalk(x.getRight())

    def postOrderTreeWalk(self, x):
        """Plota arvore em posOrdem."""
        if x is not self.nil:
            self.postOrderTreeWalk(x.getLeft())
            self.postOrderTreeWalk(x.getRight())
            print(x.getData(), end = " ")

    def search(self, k):
        """Busca e retorna o no."""
        x = self.getRoot()
        while (x is not self.nil) and (k is not x.getData().getNumero()):
            if k < x.getData().getNumero():
                x = x.getLeft()
            else:
                x = x.getRight()
        return x

    def leftRotate(self, x):
        """Rotaçao simples a esquerda."""
        y = x.getRight()
        x.setRight(y.getLeft())
        if y.getLeft() is not self.nil:
            y.getLeft().setParent(x)
        y.setParent(x.getParent())
        if x.getParent() is self.nil:
            self.setRoot(y)
        elif x is x.getParent().getLeft():
            x.getParent().setLeft(y)
        else:
            x.getParent().setRight(y)
        y.setLeft(x)
        x.setParent(y)

    def rightRotate(self, x):
        """Rotaçao simples a direita."""
        y = x.getLeft()
        x.setLeft(y.getRight())
        if x.getRight() is not self.nil:
            y.getRight().setParent(x)
        y.setParent(x.getParent())
        if x.getParent() is self.nil:
            self.setRoot(y)
        elif x is x.getParent().getRight():
            x.getParent().setRight(y)
        else:
            x.getParent().setLeft(y)
        y.setRight(x)
        x.setParent(y)

    def insert(self, z):
        """Insere um novo no."""
        x = self.getRoot()
        y = self.nil
        z = Node(z)
        while x is not self.nil:
            y = x
            if (z.getData() < x.getData()):
                x = x.getLeft()
            else:
                x = x.getRight()
        z.setParent(y)
        if y is self.nil:
            self.setRoot(z)
        elif z.getData() < y.getData():
            y.setLeft(z)
        else:
            y.setRight(z)
        z.setLeft(self.nil)
        z.setRight(self.nil)
        z.setColor('red')
        self.insertFixUp(z)

    def insertFixUp(self, z):
        while z.getParent().getColor() == 'red':
            if z.getParent() is z.getParent().getParent().getLeft():
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
        v.setParent(u.getParent())

    def delete(self, z):
        y = z
        y_original_color = y.getColor()
        if z.getLeft() is self.nil:
            x = z.getRight()
            self.transplant(z, z.getRight())
        elif z.getRight() is self.nil:
            x = z.getLeft()
            self.transplant(z, z.getLeft())
        else:
            y = self.minimum(z.getRight())
            y_original_color = y.getColor()
            x = y.getRight()
            if y.getParent() is z:
                x.setParent(y)
            else:
                self.transplant(y, y.getRight())
                y.setRight(z.getRight())
                y.getRight().setParent(y)
            self.transplant(z, y)
            y.setLeft(z.getLeft())
            y.getLeft().setParent(y)
            y.setColor(z.getColor())
        if y_original_color == 'black':
            self.deleteFixUp(x)

    def deleteFixUp(self, x):
        while x is not self.getRoot() and x.getColor() == 'black':
            if x is x.getParent().getLeft():
                w = x.getParent().getRight()
                if w.getColor() == 'red':
                    w.setColor('black')
                    x.getParent().setColor('red')
                    self.leftRotate(x.getParent())
                    w = x.getParent().getRight()
                if w.getLeft().getColor() == 'black' and w.getRight().getColor() == 'black':
                    w.setColor('red')
                    x = x.getParent()
                else:
                    if w.getRight().getColor() == 'black':
                        w.getLeft().setColor('black')
                        w.setColor('red')
                        self.rightRotate(w)
                        w = x.getParent().getRight()
                    w.setColor(x.getParent().getColor())
                    x.getParent().setColor('black')
                    w.getRight().setColor('black')
                    self.leftRotate(x.getParent())
                    x = self.getRoot()
            else:
                w = x.getParent().getLeft()
                if w.getColor() == 'red':
                    w.setColor('black')
                    x.getParent().setColor('red')
                    self.rightRotate(x.getParent())
                    w = x.getParent().getRight()
                if w.getRight().getColor() == 'black' and w.getLeft().getColor() == 'black':
                    w.setColor('red')
                    x = x.getParent()
                else:
                    if w.getLeft().getColor() == 'black':
                        w.getRight().setColor('black')
                        w.setColor('red')
                        self.leftRotate(w)
                        w = x.getParent().getLeft()
                    w.setColor(x.getParent().getColor())
                    x.getParent().setColor('black')
                    w.getLeft().setColor('black')
                    self.rightRotate(x.getParent())
                    x = self.getRoot()
        x.setColor('black')
