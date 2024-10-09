cantidad=int(input("Ingrese la cantidad de datos"))
vector=cantidad*[""]
acumulador=0

for i in range(cantidad,3):
    vector[i]=int(input(""" Ingrese un numero """))
    acumulador+=vector[i]
print(f""" El promedio es {acumulador/cantidad} """)
print (vector)

