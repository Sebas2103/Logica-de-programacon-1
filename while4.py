opcion="si"
acumulador=0
while opcion!="no":
    numero=int(input(""" Digite un numero entero """))
    opcion=input(""" Desea continuar si o no """)
    acumulador+=numero
    
print(f""" La suma de los numeros enteros {acumulador} """)

