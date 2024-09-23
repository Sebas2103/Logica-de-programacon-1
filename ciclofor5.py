#Contar al interior de un ciclo  for, cuantos numeros entre el 0 al 100 son multiplos del 20.Para ello haremos el uso del operador % que obtiene el residuo de una division y un condiconal para verificar que el modulo sea cero al dividiar por 20
contadorP=0
for i in range (0,101):
    contadorP+=1  if i%20==0 else 0
print(f""" la cantidad de numeros multiplos son {contadorP} """)