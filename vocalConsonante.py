# Ingresar una letra e imprimir si es vocal  mayuscula,vocal minuscula o consonante
letra = input("Ingrese una letra ")

if letra == "A" or letra == "E" or letra == "O" or letra == "I" or letra == "U":
    print(" Su letra es una vocal mayuscula ")

elif letra == "a" or letra == "e" or letra == "o" or letra == "i" or letra == "u":
    print(" Su letra es una vocal minuscula ")
else:
    print(" Su letra es una consonante",letra)