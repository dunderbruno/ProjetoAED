class Titulo():
    """Classe Titulo."""

    def __init__(self, inscricao, zona, secao):
        """Construtor."""
        self.__inscricao = inscricao
        self.__zona = zona
        self.__secao = secao

    def __repr__(self):
        s = ''
        s += str(self.getInscricao()) + '-'
        s += str(self.getZona()) + '-'
        s += str(self.getSecao())
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