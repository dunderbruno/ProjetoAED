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


class Tree:
    u"""Red-Black Tree."""

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

    def set_root(self, root):
        u"""Define raiz da árvore."""
        self.__root = root

    def get_root(self):
        """Retorna a raiz da arvore."""
        return self.__root

    def is_empty(self):
        """Retorna se a arvore esta vazia ou nao."""
        if self.get_root() is self.nil:
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

    def pre_order_tree_walk(self, x):
        """Plota arvore em preOrdem."""
        if x is not self.nil:
            print(x.get_data(), end =" ")
            self.pre_order_tree_walk(x.get_left())
            self.pre_order_tree_walk(x.get_right())

    def in_order_tree_walk(self, x):
        """Plota arvore em ordem."""
        if x is not self.nil:
            self.in_order_tree_walk(x.get_left())
            print(x.get_data(), end ="\n")
            self.in_order_tree_walk(x.get_right())

    def post_order_tree_walk(self, x):
        """Plota arvore em posOrdem."""
        if x is not self.nil:
            self.post_order_tree_walk(x.get_left())
            self.post_order_tree_walk(x.get_right())
            print(x.get_data(), end =" ")

    def search(self, k):
        """Busca e retorna o no."""
        x = self.get_root()
        while (x is not self.nil) and (k != x.get_data()):
            if k < x.get_data():
                x = x.getLeft()
            else:
                x = x.getRight()
        return x

    def left_rotate(self, x):
        """Rotaçao simples à esquerda."""
        y = x.get_right()
        x.set_right(y.get_left())
        if y.get_left() is not self.nil:
            y.get_left().set_parent(x)
        y.set_parent(x.get_parent())
        if x.get_parent() is self.nil:
            self.set_root(y)
        elif x is x.get_parent().get_left():
            x.get_parent().set_left(y)
        else:
            x.get_parent().set_right(y)
        y.set_left(x)
        x.set_parent(y)

    def right_rotate(self, x):
        """Rotaçao simples à direita."""
        y = x.get_left()
        x.set_left(y.get_right())
        if x.get_right() is not self.nil:
            y.get_right().set_parent(x)
        y.set_parent(x.get_parent())
        if x.get_parent() is self.nil:
            self.set_root(y)
        elif x is x.get_parent().get_right():
            x.get_parent().set_right(y)
        else:
            x.get_parent().set_left(y)
        y.set_right(x)
        x.set_parent(y)

    def insert(self, z):
        """Recebe uma entrada e a insere na árvore."""
        x = self.get_root()
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
            self.set_root(z)
        elif z.get_data() < y.get_data():
            y.set_left(z)
        else:
            y.set_right(z)
        z.set_left(self.nil)
        z.set_right(self.nil)
        z.set_color('red')
        self.insert_fix_up(z)

    def insert_fix_up(self, z):
        while z.get_parent().get_color() == 'red':
            if z.get_parent() is z.get_parent().get_parent().get_left():
                y = z.get_parent().get_parent().get_right()
                if y.get_color() == 'red':
                    z.get_parent().set_color('black')
                    y.set_color('black')
                    z.get_parent().get_parent().set_color('red')
                    z = z.get_parent().get_parent()
                else:
                    if z == z.get_parent().get_right():
                        z = z.get_parent()
                        self.left_rotate(z)
                    z.get_parent().set_color('black')
                    z.get_parent().get_parent().set_color('red')
                    self.right_rotate(z.get_parent().get_parent())
            else:
                y = z.get_parent().get_parent().get_left()
                if y.get_color() == 'red':
                    z.get_parent().set_color('black')
                    y.set_color('black')
                    z.get_parent().get_parent().set_color('red')
                    z = z.get_parent().get_parent()
                else:
                    if z == z.get_parent().get_left():
                        z = z.get_parent()
                        self.right_rotate(z)
                    z.get_parent().set_color('black')
                    z.get_parent().get_parent().set_color('red')
                    self.left_rotate(z.get_parent().get_parent())
        self.get_root().set_color('black')

    def transplant(self, u, v):
        if u.get_parent() is self.nil:
            self.set_root(v)
        elif u is u.get_parent().get_left():
            u.get_parent().set_left(v)
        else:
            u.get_parent().set_right(v)
        v.set_parent(u.get_parent())

    def delete(self, z):
        y = z
        y_original_color = y.get_color()
        if z.get_left() is self.nil:
            x = z.get_right()
            self.transplant(z, z.get_right())
        elif z.get_right() is self.nil:
            x = z.get_left()
            self.transplant(z, z.get_left())
        else:
            y = self.minimum(z.get_right())
            y_original_color = y.get_color()
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
            y.set_color(z.get_color())
        if y_original_color == 'black':
            self.delete_fix_up(x)

    def delete_fix_up(self, x):
        while x is not self.get_root() and x.get_color() == 'black':
            if x is x.get_parent().get_left():
                w = x.get_parent().get_right()
                if w.get_color() == 'red':
                    w.set_color('black')
                    x.get_parent().set_color('red')
                    self.left_rotate(x.get_parent())
                    w = x.get_parent().get_right()
                if w.get_left().get_color() == 'black' and w.get_right().get_color() == 'black':
                    w.set_color('red')
                    x = x.get_parent()
                else:
                    if w.get_right().get_color() == 'black':
                        w.get_left().set_color('black')
                        w.set_color('red')
                        self.right_rotate(w)
                        w = x.get_parent().get_right()
                    w.set_color(x.get_parent().get_color())
                    x.get_parent().set_color('black')
                    w.get_right().set_color('black')
                    self.left_rotate(x.get_parent())
                    x = self.get_root()
            else:
                w = x.get_parent().get_left()
                if w.get_color() == 'red':
                    w.set_color('black')
                    x.get_parent().set_color('red')
                    self.right_rotate(x.get_parent())
                    w = x.get_parent().get_right()
                if w.get_right().get_color() == 'black' and w.get_left().get_color() == 'black':
                    w.set_color('red')
                    x = x.get_parent()
                else:
                    if w.get_left().get_color() == 'black':
                        w.get_right().set_color('black')
                        w.set_color('red')
                        self.left_rotate(w)
                        w = x.get_parent().get_left()
                    w.set_color(x.get_parent().get_color())
                    x.get_parent().set_color('black')
                    w.get_left().set_color('black')
                    self.right_rotate(x.get_parent())
                    x = self.get_root()
        x.set_color('black')
