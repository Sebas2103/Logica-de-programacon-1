from random import randint
def sucursal():
    

    dat=[[0 for meses in range(12)]for sucursal in  range(5)]

    for sucursal in range (5):
        for meses in range (12):
                dat[sucursal][meses]=randint(0,10)
                print(dat[sucursal][meses],end=" 0")
        print()

sucursal()


#filas= 5 sucursales
#columnas=12 meses



