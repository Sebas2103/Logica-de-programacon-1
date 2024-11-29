def  multiplos3(matriz):
    
    
    for  filas in range (6):
        for columnas in range(6):
            if (filas%2==0):
            
               matriz[filas][columnas]=3*(columnas+1)
            else:
                matriz[filas][columnas]=2*(columnas+1)
            print(matriz[filas][columnas],end=" ")

        print()
    return matriz
def sumatoria(matrizCompleta):
    sumatoria=0
    for filas in range (6):
        for columnas in range(6):
            sumatoria+=matriz[filas][columnas]
    return sumatoria
    

matriz=[[0 for columnas in  range (6)] for filas in range(6)]
matrizCompleta=multiplos3(matriz)
print(sumatoria(matrizCompleta))
