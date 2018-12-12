def valida(no):
    titulo = no.getData()
    ins = False
    sec = False
    zon = False
    if len(titulo.getInscricao()) == 8 and titulo.getInscricao().isnumeric():
        ins = True
    if len(titulo.getSecao()) == 4 and titulo.getSecao().isnumeric():
        sec = True
    if len(titulo.getZona()) == 3 and titulo.getZona().isnumeric():
        zon = True

    if ins and sec and zon:
        return True
    else:
        return False