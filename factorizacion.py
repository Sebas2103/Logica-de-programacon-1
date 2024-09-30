def factorizacion(a,b,c):
    resultadoP=(-b+(b**2-4*a*c)**0.5)/2*a
    resultadoN=(-b-(b**2-4*a*c)**0.5)/2*a
    print(f""" El resultado x1= {resultadoP}  resultado x2= {resultadoN}""")
    return resultadoN,resultadoP

factorizacion(1,5,6)


