def inicializa():   
    n_datos=int(input("cuantos datos desea ingresar :"))
    lista1=n_datos*[0]
    pos=n_datos*[""]
    return n_datos,lista1,pos

def crearlista(lista1,n_datos):
    for i in range (n_datos):
        lista1[i]=int(input("Ingresa numero "))
    print(lista1)
    return lista1
def inicio():
    n_datos,lista1,pos=inicializa()
    lista=crearlista(lista1,n_datos) 
inicio()