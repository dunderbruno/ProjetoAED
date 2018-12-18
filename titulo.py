"""Titulo de Eleitor."""


class Titulo():
    """Classe Titulo."""

    def __init__(self, inscricao, zona, secao):
        u"""
        O objeto Titulo é iniciado com 3 argumentos.

        Argumentos:
            - inscricao: string com 8 caracteres numéricos
            - zona:      string com 3 caracteres numéricos
            - secao:     string com 4 caracteres numéricos
        Atributos:
            - numero:    string que concatena os demais atributos
        """
        self.__inscricao = str(inscricao)
        self.__zona = str(zona)
        self.__secao = str(secao)
        self.__numero = self.__inscricao + self.__zona + self.__secao

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

    def cadastrar():
        """Recebe uma String e retorna um objeto Titulo."""
        numero = input('Cadastrar Título: ')
        return Titulo(numero[0:8], numero[8:11], numero[11:])

    def descadastrar():
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
