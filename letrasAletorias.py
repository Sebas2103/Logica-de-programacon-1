#Un codigo que sea una pabalabra que sea de 4 letras y que la segunday ultima letra sean vocales
import random 
vocales=["A","E","I","O","U"] 
letras=["B","C","D","R","P","R","S","T","F","Q","H"]


print(random.choice(letras)+random.choice(vocales)+random.choice(letras)+random.choice(vocales))


