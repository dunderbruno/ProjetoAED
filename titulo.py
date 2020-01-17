"""Titulo de Eleitor."""


class Titulo():
    """Classe Titulo."""

    def __init__(self, numero):
        self.__inscricao = str(numero[0:8])
        self.__zona = str(numero[8:11])
        self.__secao = str(numero[11:])
        self.__numero = str(numero)

    def __repr__(self):
        u"""O objeto é exibido no formato: XXXXXXXXYYYZZZZ."""
        return self.__numero

    def __str__(self):
        """
        Quando convertido em string.

        'XXXXXXXX-YYY-ZZZZ'
        """
        return self.__inscricao + '-' + self.__zona + '-' + self.__secao

    def __lt__(self, other):
        """Menor que."""
        return self.__numero < other

    def __eq__(self, other):
        """Igual a."""
        return self.__numero == other

    def __gt__(self, other):
        """Maior que."""
        return self.__numero > other

    def descadastrar(self):
        """Le uma string para repassar pra alicacao principal."""
        return input('Descadastrar Título: ')

    def getInscricao(self):
        return self.__inscricao

    def setInscricao(self, inscricao):
        self.__inscricao = inscricao

    def getZona(self):
        return self.__zona

    def setZona(self, zona):
        self.__zona = zona

    def getSecao(self):
        return self.__secao

    def setSecao(self, secao):
        self.__secao = secao

    def getNumero(self):
        return self.__numero
