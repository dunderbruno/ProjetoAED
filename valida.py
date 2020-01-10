u"""Validação de Título de Eleitor."""


def valida(no):
    u"""
    Recebe um objeto Node e verifica se contém um título válido.

    Formato esperado:
    XXXXXXXXYYYZZZZ

    Se todos os caracteres são numéricos e tem o tamanho certo:
        retorna verdadeiro.
    Se não:
        retorna falso
    """
    titulo = no.get_data()
    ins = False
    sec = False
    zon = False
    if len(titulo.getInscricao()) == 8 and titulo.getInscricao().isnumeric():
        ins = True
    if len(titulo.getZona()) == 3 and titulo.getZona().isnumeric():
        zon = True
    if len(titulo.getSecao()) == 4 and titulo.getSecao().isnumeric():
        sec = True

    if ins and zon and sec:
        return True
    else:
        return False
