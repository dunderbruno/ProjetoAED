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
    if len(titulo.get_inscricao()) == 8 and titulo.get_inscricao().isnumeric():
        ins = True
    if len(titulo.get_zona()) == 3 and titulo.get_zona().isnumeric():
        zon = True
    if len(titulo.get_secao()) == 4 and titulo.get_secao().isnumeric():
        sec = True

    if ins and zon and sec:
        return True
    else:
        return False
