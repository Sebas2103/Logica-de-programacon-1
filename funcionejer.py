#Diseñe  un prgrama   modular en python que imprima la tabla de umtiplicar de un numero ingresado por el uauario
def tablaMultiplicar (num1):
    for i in range (1,10+1):
        print("""{} * {} ={}""".format(num1,i,num1*i))

num1=int(input("Ingresa el primer numero"))
tablaMultiplicar(num1) 