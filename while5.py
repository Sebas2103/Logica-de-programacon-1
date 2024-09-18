#Diseñar un algoritmo que calcule el promedio de los pesos de un grupo de gimnastas.Se desconoce cuantos gimnastas conforman el grupo           
cont=1
opcion="n"
acumulador=0
while opcion!="s":
    peso=int(input("Ingrese el peso del primer gimnastas"))
    acumulador+=peso
    opcion=input(""" Desea salir s o n """)
    cont+=1

print(f""" El promedio del peso de gimnastas es 
      {acumulador/(cont-1)} """)
