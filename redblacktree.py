"""
Red-Black Tree.

Baseado no pseudocódigo do livro INTRODUCTION TO ALGORITHMS, 3ed.
e em anotações de aula da disciplina Algorítmos e Estruturas de Dados
do Professor Tiago A. E. Ferreira - BSI - UFRPE
"""


class Node:
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

    def get_color(self):
        """Retorna chave de acesso."""
        return self.__color

    def get_data(self):
        u"""Retorna conteúdo armazenado."""
        return self.__data

    def get_left(self):
        """Retorna filho esquerdo."""
        return self.__left

    def get_right(self):
        """Retorna filho direito."""
        return self.__right

    def get_parent(self):
        u"""Retorna nó pai."""
        return self.__parent

    def set_color(self, color):
        """
        Define chave de acesso.
        ex:
        x.setColor('red')
        """
        self.__color = color

    def set_data(self, data):
        u"""Define conteúdo armazenado."""
        self.__data = data

    def set_left(self, left):
        """Define filho esquerdo."""
        self.__left = left

    def set_right(self, right):
        """Define filho direito."""
        self.__right = right

    def set_parent(self, parent):
        u"""Define nó pai."""
        self.__parent = parent


class Tree():
    u"""Árvore Vermelho e Preto."""

    def __init__(self):
        """
        A árvore é iniciada com o nó 'nil',
        para onde todas as folhas irão apontar
        """
        self.nil = Node(None)
        self.nil.set_color('black')
        self.nil.set_parent(self.nil)
        self.nil.set_left(self.nil)
        self.nil.set_right(self.nil)
        self.__root = self.nil

    def setRoot(self, root):
        u"""Define raiz da árvore."""
        self.__root = root

    def getRoot(self):
        """Retorna a raiz da arvore."""
        return self.__root

    def isEmpty(self):
        """Retorna se a arvore esta vazia ou nao."""
        if self.getRoot() is self.nil:
            return True
        else:
            return False

    def minimum(self, node):
        """Retorna o minino daquele no."""
        if node is not self.nil:
            while node.get_left() is not self.nil:
                node = node.get_left()
            return node

    def maximum(self, node):
        """Retorna o maximo daquel no."""
        if node is not self.nil:
            while node.get_right() is not self.nil:
                node = node.get_right()
            return node

    def successor(self, x):
        """Retorna o sucessor."""
        if x is not self.nil:
            if x.get_right() is not self.nil:
                return self.minimum(x.get_right())
            else:
                father = x.get_parent()
                while (father is not self.nil) and (x is father.get_right()):
                    x = father
                    father = x.get_parent()
                    return father

    def preOrderTreeWalk(self, x):
        """Plota arvore em preOrdem."""
        if x is not self.nil:
            print(x.get_data(), end =" ")
            self.preOrderTreeWalk(x.get_left())
            self.preOrderTreeWalk(x.get_right())

    def inOrderTreeWalk(self, x):
        """Plota arvore em ordem."""
        if x is not self.nil:
            self.inOrderTreeWalk(x.get_left())
            print(x.get_data(), end ="\n")
            self.inOrderTreeWalk(x.get_right())

    def postOrderTreeWalk(self, x):
        """Plota arvore em posOrdem."""
        if x is not self.nil:
            self.postOrderTreeWalk(x.get_left())
            self.postOrderTreeWalk(x.get_right())
            print(x.get_data(), end =" ")

    def search(self, k):
        """Busca e retorna o no."""
        x = self.getRoot()
        while (x is not self.nil) and (k != x.get_data()):
            if k < x.get_data():
                x = x.getLeft()
            else:
                x = x.getRight()
        return x

    def leftRotate(self, x):
        """Rotaçao simples à esquerda."""
        y = x.get_right()
        x.set_right(y.get_left())
        if y.get_left() is not self.nil:
            y.get_left().set_parent(x)
        y.set_parent(x.get_parent())
        if x.get_parent() is self.nil:
            self.setRoot(y)
        elif x is x.get_parent().get_left():
            x.get_parent().set_left(y)
        else:
            x.get_parent().set_right(y)
        y.set_left(x)
        x.set_parent(y)

    def rightRotate(self, x):
        """Rotaçao simples à direita."""
        y = x.get_left()
        x.set_left(y.get_right())
        if x.get_right() is not self.nil:
            y.get_right().set_parent(x)
        y.set_parent(x.get_parent())
        if x.get_parent() is self.nil:
            self.setRoot(y)
        elif x is x.get_parent().get_right():
            x.get_parent().set_right(y)
        else:
            x.get_parent().set_left(y)
        y.set_right(x)
        x.set_parent(y)

    def insert(self, z):
        """Recebe uma entrada e a insere na árvore."""
        x = self.getRoot()
        y = self.nil
        z = Node(z)
        while x is not self.nil:
            y = x
            if (z.get_data() < x.get_data()):
                x = x.getLeft()
            else:
                x = x.getRight()
        z.set_parent(y)
        if y is self.nil:
            self.setRoot(z)
        elif z.get_data() < y.get_data():
            y.set_left(z)
        else:
            y.set_right(z)
        z.set_left(self.nil)
        z.set_right(self.nil)
        z.set_color('red')
        self.insertFixUp(z)

    def insertFixUp(self, z):
        while z.getParent().getColor() == 'red':
            if z.getParent() is z.getParent().get_parent().get_left():
                y = z.getParent().get_parent().get_right()
                if y.getColor() == 'red':
                    z.getParent().set_color('black')
                    y.set_color('black')
                    z.getParent().get_parent().set_color('red')
                    z = z.getParent().get_parent()
                else:
                    if z == z.getParent().get_right():
                        z = z.getParent()
                        self.leftRotate(z)
                    z.getParent().set_color('black')
                    z.getParent().get_parent().set_color('red')
                    self.rightRotate(z.getParent().get_parent())
            else:
                y = z.getParent().get_parent().get_left()
                if y.getColor() == 'red':
                    z.getParent().set_color('black')
                    y.set_color('black')
                    z.getParent().get_parent().set_color('red')
                    z = z.getParent().get_parent()
                else:
                    if z == z.getParent().get_left():
                        z = z.getParent()
                        self.rightRotate(z)
                    z.getParent().set_color('black')
                    z.getParent().get_parent().set_color('red')
                    self.leftRotate(z.getParent().get_parent())
        self.getRoot().set_color('black')

    def transplant(self, u, v):
        if u.get_parent() is self.nil:
            self.setRoot(v)
        elif u is u.get_parent().get_left():
            u.get_parent().set_left(v)
        else:
            u.get_parent().set_right(v)
        v.set_parent(u.get_parent())

    def delete(self, z):
        y = z
        y_original_color = y.getColor()
        if z.get_left() is self.nil:
            x = z.get_right()
            self.transplant(z, z.get_right())
        elif z.get_right() is self.nil:
            x = z.get_left()
            self.transplant(z, z.get_left())
        else:
            y = self.minimum(z.get_right())
            y_original_color = y.getColor()
            x = y.get_right()
            if y.get_parent() is z:
                x.set_parent(y)
            else:
                self.transplant(y, y.get_right())
                y.set_right(z.get_right())
                y.get_right().set_parent(y)
            self.transplant(z, y)
            y.set_left(z.get_left())
            y.get_left().set_parent(y)
            y.set_color(z.getColor())
        if y_original_color == 'black':
            self.deleteFixUp(x)

    def deleteFixUp(self, x):
        while x is not self.getRoot() and x.getColor() == 'black':
            if x is x.getParent().get_left():
                w = x.get_parent().get_right()
                if w.getColor() == 'red':
                    w.set_color('black')
                    x.get_parent().set_color('red')
                    self.leftRotate(x.get_parent())
                    w = x.get_parent().get_right()
                if w.get_left().getColor() == 'black' and w.get_right().getColor() == 'black':
                    w.set_color('red')
                    x = x.get_parent()
                else:
                    if w.get_right().getColor() == 'black':
                        w.get_left().set_color('black')
                        w.set_color('red')
                        self.rightRotate(w)
                        w = x.get_parent().get_right()
                    w.set_color(x.get_parent().getColor())
                    x.get_parent().set_color('black')
                    w.get_right().set_color('black')
                    self.leftRotate(x.get_parent())
                    x = self.getRoot()
            else:
                w = x.get_parent().get_left()
                if w.getColor() == 'red':
                    w.set_color('black')
                    x.get_parent().set_color('red')
                    self.rightRotate(x.get_parent())
                    w = x.get_parent().get_right()
                if w.get_right().getColor() == 'black' and w.get_left().getColor() == 'black':
                    w.set_color('red')
                    x = x.get_parent()
                else:
                    if w.get_left().getColor() == 'black':
                        w.get_right().set_color('black')
                        w.set_color('red')
                        self.leftRotate(w)
                        w = x.get_parent().get_left()
                    w.set_color(x.get_parent().getColor())
                    x.get_parent().set_color('black')
                    w.get_left().set_color('black')
                    self.rightRotate(x.get_parent())
                    x = self.getRoot()
        x.set_color('black')
