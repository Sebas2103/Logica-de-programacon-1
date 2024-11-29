def crear (matriz,datos):
   
    for filas in range(3):
        contador=0
        for columnas in range(4):
            respuesta=input(" Ingrese datos "+ datos[contador])
            matriz[filas][columnas]=respuesta
            contador+=1

    return matriz
def imprimir(matriz,datos):
      for filas in range(3):
        contador=0
        for columnas in range(4):
            respuesta=print(datos[contador],": ",matriz[filas][columnas])
            contador+=1

matriz=[["" for columnas in range (4)] for filas in range (3)]
datos=["nombre","Apellido","Direccion","telefono"]


matriz =crear(matriz,datos)
imprimir(matriz,datos)

