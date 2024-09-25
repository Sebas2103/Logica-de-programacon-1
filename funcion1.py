def suma(num1,num2):
    suma=num1+num2
    return suma 
a=int(input(""" Ingrese el primer numero """))
b=int(input(""" Ingrse el  segundo numero """))

resultado=suma(a,b)
#Format  COLOCA EN CADA PARENTESIS LO QUE ESTA  EN CADA CORCHETE
print (""" El resultado es {} de  {}-{} """.format(resultado,a,b))
 

