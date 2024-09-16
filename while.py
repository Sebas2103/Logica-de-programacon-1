""" Diseñe un programa eb python que pida dos numeros,identifique el numero mayor,el menor y muestre la seuma desde el menor hasta el mayor incluyendo los numeros dados"""
num1=int(input(""" Ingrese el numero #1 """))
num2=int(input(""" Ingrese el numero #2 """))

numeroMayor=num1 if num1>num2 else num2 
numeroMenor=num1 if num1<num2 else num2 
sumatoria=0

while numeroMenor< numeroMayor:
    sumatoria+=numeroMenor
    numeroMenor+=1
print(f""" La sumatoria de los numero es {sumatoria} """)


