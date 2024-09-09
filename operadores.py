operadores = input("Ingrese el operador")
num1 = int(input("Ingrese el numero 1"))
num2 = int(input("Ingrese el numero 2"))

if operadores == "+":
    print("La suma es ", num1+num2)

if operadores == "*":
    print("La suma es ", num1*num2)
if operadores == "-":
 print("La suma es ", num1-num2)
if operadores=="/":
    if num2 ==0:
       print("No se puede divir con 0")
    else:
       print(num1/num2)
if operadores!="+" and operadores!="-" and operadores!="*" and operadores!="/":
   print("El dato no es valido")