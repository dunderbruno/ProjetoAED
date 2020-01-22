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
        return f"{self.__inscricao}-{self.__zona}-{self.__secao}"

    def __lt__(self, other):
        """Menor que."""
        return self.__numero < other

    def __eq__(self, other):
        """Igual a."""
        return self.__numero == other

    def __gt__(self, other):
        """Maior que."""
        return self.__numero > other

    def get_inscricao(self):
        return self.__inscricao

    def set_inscricao(self, inscricao):
        self.__inscricao = inscricao

    def get_zona(self):
        return self.__zona

    def set_zona(self, zona):
        self.__zona = zona

    def get_secao(self):
        return self.__secao

    def set_secao(self, secao):
        self.__secao = secao

    def get_numero(self):
        return self.__numero
