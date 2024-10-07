lista=[2,3,4,1,3,6,7,4,8]
for i in lista:
    if i==7:
        break
    print(i)

#cuando el elemento es par se imprime
for i in lista:
    if i% 2!=0:
        continue
    print(lista)

lista=[30,50,21,-39,0]
i=0
for x in lista:
    lista[i]=x+1
    i+=1
print(lista)