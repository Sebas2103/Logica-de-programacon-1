numero = int(input("Ingrese  un numero positivo "))
if numero < 0:
    print("Su numero es negativo ")
else:
    print("El numero es par ") if numero % 2 == 0 else print(
        "El numero es impar")