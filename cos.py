#de forma similar ,escribe otra funcion ,coseno ,que devuekva el coseno aproximado de un numeri  utilizando  su desarollo en serie de MAClAURIN
def MacLaurin(x):
    acumulador=1
    signo=(1)
    for num in range (2,x+1,2):
        signo=signo*(-1)
        

        acumulador+= signo*((x**num)/factorial(num))
        print(f""" {signo} {acumulador} """)

    
    
    return acumulador


def factorial(x):
    acum=1
    for i in range (1,x):
        acum*=i
    return acum



x=int(input(""" Ingrese X """))
cos=MacLaurin(x)
print(cos)
