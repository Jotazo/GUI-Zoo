import datetime

ahora = datetime.datetime.now()

fecha = ahora.strftime("%d-%m-%Y %H:%M:%S")

def devuelveFecha():
    
    mensaje = f"{'Fecha Venta:':^38}\
        \n {fecha:^38}\n"

    return mensaje