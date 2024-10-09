#A una lista  de tring adicionar a cada elemento con -p 
lista=["abc","def","ghi","jkl"]
i=0
for i in range(4):
    lista[i]+="-p"
    i+=i
print(lista)

