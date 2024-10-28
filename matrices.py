def matrices(mat,filas,columnas):

    for i in range (filas):
        for j in range (columnas):
            print(mat[i][j],end="-") 
        print()

mat=[[1,2,3]
    ,[4,4,5]]
filas=2
columnas=3
matrices(mat,filas,columnas)