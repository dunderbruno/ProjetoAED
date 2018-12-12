class Titulo():
    """Classe Titulo."""

    def __init__(self, inscricao, zona, secao):
        """Construtor."""
        self.__inscricao = str(inscricao)
        self.__zona = str(zona)
        self.__secao = str(secao)

    def __repr__(self):
        s = ''
        s += self.__inscricao + '-'
        s += self.__zona + '-'
        s += self.__secao
        return s

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
