def valorLLamada(minutos,rango):

    valorLlamada=1000 if minutos<3 else 0
    """ valorLLamada=minutos*200 if rango==1 else 0
    valorLLamada=minutos*300 if rango==2 else 0 """
    if (minutos<3):
        valorLlamada=1000
    else:
        valorLlamada=0

    if(rango==1):
        valorLlamada=valorLlamada+(minutos-3)*200
    elif(rango==2):
        valorLlamada=valorLlamada+(minutos-3)*300

    print(f""" El valor final de la llamada es {valorLlamada} """)

    return valorLlamada



minutos=int(input(""" Ingrese los minutos  de la llamada """))
rango=int(input(""" Ingrese si es 1.nacional 
                              2.Intercional  """))
valorLLamada(minutos,rango)



