n=int(input(""" Ingrese la cantidad de numeros que va ingresar """))
cont=1
bandera=0
while cont<=n:
  numero=int(input("Ingrese un numero "))
  cont+=1
  if numero<0:
    bandera=1

    
print(f""" Ingreso al menos {bandera} numeros negativos """)



    


