def dividendo(numerador,divisor,cont):
    #------------------------------------
    if(numerador>divisor):
        cont+=1
        numerador=numerador-divisor
        dividendo(numerador,divisor,cont)
    else:
        print(f""" dado que {numerador}  es menor que {divisor} entonces : el residuo es {numerador} el  cociente es {cont}""")
        
cont=0
numerador=int(input("""Ingrese numerador """))
divisor=int(input(""" Ingrese el denominador """))

dividendo(numerador,divisor,cont)
