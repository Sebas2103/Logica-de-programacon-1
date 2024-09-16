#Ingresar varias notas y calcular el promedio.s para ingresar nueva nota n para salir
opcion="s"
cont=1
acumulador=0
while opcion!="n":
      
    nota=int(input(f""" Ingrese una nota  #{cont}  """))
    cont+=1
    acumulador=nota+acumulador
  
    opcion=input("Ingrese la n para salir y s para continuar ingresando notas ")
    
print(f"su promedio es: {acumulador/(cont-1)}")






