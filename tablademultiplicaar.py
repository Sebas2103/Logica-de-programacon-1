""" tabla de multiplica del 1 a 10 cual numero   """
numero = float(input(""" Ingrese un numero """))
i = 1
print("""   Tabla de multiplicar    """)
while i <= 10:
    print(f"| {i}*{numero}= {int(numero*i)} |")
    i += 1
