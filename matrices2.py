def buscadorElement(matriz,filas,columnas):
    for i in range (filas):
        for j in range (columnas):
            if matriz[i][j]==5:
                print(f"se encontro un 5 en la fila",i,"columna",j) 
          

matriz=[[2,4,1]
        ,[3,4,6]
        ,[1,5,9]]
n=len(matriz)
buscadorElement(matriz,n,n)

