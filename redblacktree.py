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
