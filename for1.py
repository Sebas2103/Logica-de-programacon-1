#Diseñe un programa en python que calcule el promedio de n numeros ingresados por el usuario.El valor d n tambien lo proporciona el 
# usuario
n=int(input(""" Ingrese la cantidad de notas"""))
acumulador=0

for i in range(1,n+1):
    nota=float(input("""Ingrese el primer numero  """))
    acumulador+=nota

print(f""" El promedio de los numeros es {acumulador/n} """)