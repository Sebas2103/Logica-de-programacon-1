numero1= int(input("Ingrese el primer numero 1 "))
numero2= int(input("Ingrese el primer numero 2 "))
numero3= int(input("Ingrese el primer numero 3 "))

if numero1>numero2 and numero1>3:
    print("El numero mayor es ",numero1)
if numero2>numero1 and numero2>numero3 :
    print("El numero mayor es ",numero2)
if numero3>numero1 and numero3>numero2 :
    print("El numero mayor es ",numero3)
else:
    print("Los numeros son iguales")