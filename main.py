from tkinter import *

import fechas
import calculosEntradas

# ----- Main window ----- #

root = Tk()
root.geometry("650x490")
root.title("Entradas Zoo")
root.resizable(0, 0)

# ----- Variables ----- #
_radioY = 60 # Posicion Y radiobuttons
_labelX = 20 # Posicion X labels
fuente = 'Helvetica 10 bold'

opcionRadio = IntVar() # Variable radioButtons
numEntradas = IntVar() # Variable del Spinbox num entradas

# ----- Funciones ----- #

def resumenCompra():
    """Imprime un mensaje en la caja de texto 'Resumen' que nos muestra el numero de entradas\
        de cada uno y el total"""
    
    if opcionRadio.get() >= 1 and opcionRadio.get() <= 4: # Si no seleccionamos un radiobutton no imprimirá nada

        txtResumen.config(state=NORMAL)

        txtResumen.delete(1.0, END) # Borramos todo el texto en el widget Text

        texto = calculosEntradas.defineTexto(opcionRadio.get(), numEntradas.get()) # Recuperamos el texto a introducir

        txtResumen.insert(INSERT, texto) # Insertamos el texto en el widget Text

        numEntradas.set(1) # Reseteamos a 1 el Spinbox

        txtResumen.config(state=DISABLED)
        
def guardar():
    """Función que pulsando el boton 'Guardar' nos guardará en un archivo .txt el texto del widget Text"""

    if calculosEntradas.noEntradas() == False: # Si se han introducido entradas, guardará info, si no, no
        fichero = open('data.txt', 'a+')
        fechaActual = fechas.devuelveFecha()
        data = fechaActual + '\n' + txtResumen.get("1.0", END) +'-\n'
        fichero.write(data)
        fichero.close()
        
# ----- Widgets ----- #

lblTipoEntradas = Label(root, text="Tipo entradas:", font=fuente)
lblTipoEntradas.place(x= _labelX, y=20)

raBebe = Radiobutton(root, text="Bebe (0-2 años)", variable=opcionRadio, value=1)
raBebe.place(x=45, y=_radioY)
raInf = Radiobutton(root, text="Infantil (3-12 años)", variable=opcionRadio, value=2)
raInf.place(x=180, y=_radioY)
raAdulto = Radiobutton(root, text="Adulto (13-64 años)", variable=opcionRadio, value=3)
raAdulto.place(x=330, y=_radioY)
raJub = Radiobutton(root, text="Jubilado (>65 años)", variable=opcionRadio, value=4)
raJub.place(x=475, y=_radioY)

lblNumEntradas = Label(root, text="Número de entradas:", font=fuente)
lblNumEntradas.place(x=_labelX, y=110)

entryNumEntradas = Spinbox(root, from_=1, to=99, width=91, textvariable=numEntradas, state="readonly")
entryNumEntradas.place(x=45, y=145)

btnAceptar = Button(root, text="Aceptar", width=12, command=resumenCompra)
btnAceptar.place(x=508, y=178)

lblResumen = Label(root, text="Resumen:", font=fuente)
lblResumen.place(x=_labelX, y=250)

txtResumen = Text(root, width=69, height=8, state=DISABLED)
txtResumen.place(x=45, y=285)

btnImprimir = Button(root, text="Imprimir", width=12)
btnImprimir.place(x=400, y=430)

btnGuardar = Button(root, text="Guardar", width=12, command=guardar)
btnGuardar.place(x=508, y=430)

root.mainloop()