dicNumEntradas = {
    'Bebe':0,
    'Niño':0,
    'Adulto':0,
    'Jubilado':0,
}

def defineTexto(opcion, numEntradas):
    """Función que pulsando el boton 'Aceptar' nos introducira el texto en el widget Text"""

    sumaEntradas(opcion, numEntradas) # Actualiza numero entradas

    total = (dicNumEntradas['Bebe']*0)+(dicNumEntradas['Niño']*14)+(dicNumEntradas['Adulto']*23)+(dicNumEntradas['Jubilado']*18)

    texto = f"{dicNumEntradas['Bebe']:>2} {compruebaEnt('Bebe'):>8} de {'Bebé':>8} ( 0€) = {dicNumEntradas['Bebe']*0:6.2f}€\
        \n{dicNumEntradas['Niño']:>2} {compruebaEnt('Niño'):>8} de {'Niño':>8} (14€) = {dicNumEntradas['Niño']*14:6.2f}€\
        \n{dicNumEntradas['Adulto']:>2} {compruebaEnt('Adulto'):>8} de {'Adulto':>8} (23€) = {dicNumEntradas['Adulto']*23:6.2f}€\
        \n{dicNumEntradas['Jubilado']:>2} {compruebaEnt('Jubilado'):>8} de Jubilado (18€) = {dicNumEntradas['Jubilado']*18:6.2f}€\
        \n\t\t\t     ----------\
        \n\t\t\tTotal   {total:6.2f}€"

    return texto

def sumaEntradas(valor, numEntradas):
    """Función que pasandole el valor aumentarán el numero de entradas 
    en el diccionario en función al numero de entradas
    que le pasemos"""

    if valor == 1:
        dicNumEntradas['Bebe']+=numEntradas
    elif valor == 2:
        dicNumEntradas['Niño']+=numEntradas
    elif valor == 3:
        dicNumEntradas['Adulto']+=numEntradas
    elif valor == 4:
        dicNumEntradas['Jubilado']+=numEntradas

def compruebaEnt(tipo):
    """Función que cambia el singular/plural de la palabra entradas/entrada"""

    textoEntradas = 'entradas'
    if dicNumEntradas[tipo] == 1:
        textoEntradas = 'entrada'

    return textoEntradas

def noEntradas():
    """Función que devolverá True si no hay entradas y False si hay alguna"""

    totalEntradas = 0
    for k,v in dicNumEntradas.items():
        totalEntradas += v
    if totalEntradas == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(defineTexto(3,2))