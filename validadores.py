
def validar_patente_p(patente): # patentes actuales AA BB XX
    letras = ['A', 'M', 'N', 'I'] # Eliminadas norma actual # revisar si esta permitido DI en las actuales
    for letra in letras:
        if letra in patente:
            return False
    if not(str.isdigit(patente[:4])):
        return False
    if 10 <= int(patente[:4]) <= 99:
        return False
    return True


def validar_patente_a(patente): # patentes antiguas AA XX XX
    if ('I' in patente[:2]) and (patente[:2] != 'DI'):
        return False
    try:
        if not(1000 <= int(patente[2:]) <= 9999):
            return False
    except ValueError:
        print(ValueError, '\n error < n <')
    return True

def diferenciar(patente): # Lista
    letras = ['Q', 'O', 'Ñ'] # letras no utilizadas
    if len(patente) != 6:
        return False
    for letra in letras:
        if letra in patente:
            return False
    if str.isdigit(patente[2]):
        if str.isdigit(patente[3]):
            return validar_patente_a(patente)

    return validar_patente_p(patente)




print(diferenciar('WNTR99'))

