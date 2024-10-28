def multiplos():
    vector=10*[0]
    posicion=0
    sumatoria=0
    for i in range (3,33,3):
     
     vector[posicion]= i
     sumatoria+=i
     posicion+=1

    print(vector)
    print(sumatoria)
multiplos()
    