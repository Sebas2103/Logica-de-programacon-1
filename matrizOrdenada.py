from random import randint

mat=[[ randint(0,10)  for  columnas  in range(30)]for filas in range(10)]


for filas in range (10):
    for columnas in range (30): 
        print(
            mat[filas][columnas], end=" ")
    print()