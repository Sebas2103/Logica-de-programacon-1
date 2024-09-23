def tablaMultuplicar(numero):
    for i in range (1,11):
        print(f""" {numero} *{i} = {numero*i}""")


for i in range (1,11):
    tablaMultuplicar(i)
    print(""" --------------------------------------- """)