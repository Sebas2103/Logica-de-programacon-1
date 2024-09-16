#Diseñar un algoritmo que calcule la suma de los numeros naturales desde 1 hasta n .el valor n lo proporciona el usuario
numero=int(input(""" Ingrese el numero entero """))
cont=1
acumulador=0
while cont<=numero:
    acumulador+=cont
    cont+=1

print(f""" La suma total es {acumulador} """)
    


