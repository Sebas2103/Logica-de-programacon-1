categoria=int(input("Ingrese la categoria del empleado "))
valor=int(input("Valor de la casa "))


match categoria:
    case 1:

        subsidio=0.2*valor
      

    case 2:
        subsidio=0.15*valor
    case 3:
        subsidio=0.10*valor
    case 4:
        subsidio=0.05*valor

    case _:
        print("Usted a digitado un caso erroneo")
        subsidio=0

    
print("El subsidio de su casa es ",valor-subsidio) if subsidio!=0 else print("El sde su casa es ",valor)