def buscadorElement(matriz,filas,columnas):
    diagonal=0  
    
    for i in range (filas):
        for j in range (columnas):
            if i==j:
                diagonal+= matriz[i][j]
          
    print(diagonal)
matriz=[[2,4,1]
        ,[3,4,6]
        ,[1,6,9]]
n=len(matriz)
buscadorElement(matriz,n,n)

