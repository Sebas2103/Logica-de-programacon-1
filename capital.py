 #2.Dado un capital inicial equivalente  a $800.000 
 # ,se desea encontrar el valor futuro F para las siguientes tasas de interes (I1=0.02,i2=0.08) con periodos 
#(n1=5,n2=13)respectivamente.
#Tenga en cuenta que :f=P(1+I)n
#donde 
#F es valor futuro
#capital inicial
#n=periodos
#i=tasa deinteres
def capital(tasa,periodo):
    F=800000*(1+tasa)*periodo
    return F
print(capital(0.02,5))
print(capital(0.08,13))


