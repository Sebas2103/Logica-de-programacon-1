#Clasificar  una lista de numeros que indican al final  de numeros parres y impares,ingresar la cantidad de numeros de lista
def  listaNumeros(numero):
    contadorP=0
    contadorI=0
    for i in range (1,numero):
        contadorP+=1 if i%2==0 else 0
        contadorI+=1 if i%2==1 else 0
    print(f""" La cantidad de pares {contadorP} Y numeros impares es {contadorI} """)

numero=int(input(""" Ingrese la cantidad de numeros """))
for i  in range (1,numero+1):
    dato=int(input(f""" Ingrese el  #{i} """))
    listaNumeros(dato)
