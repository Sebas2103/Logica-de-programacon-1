#Pida el salario de un empleado y realice un incremento del 20% si el salario es inferior a $2.000.000, en caso contrario se realizaun incremento
salario=float(input("Ingrese su salario "))
if salario <10:
    incremento=0.2*salario
    salario=incremento+salario
    print("Se aplico  con el 20 incremento")
else:
    salario=0.1*salario
    print("Se aplico el 10  incremento")

print("Su salario es ",salario)
    
