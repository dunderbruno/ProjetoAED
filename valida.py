def valida(no):
    titulo = no.getData()
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