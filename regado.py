def calcular_requerimiento_agua(temperatura, tipo_suelo, humedad, estacion):
    # 1. Temperatura
    if temperatura > 30:
        agua_por_metro_cuadrado = 10
    elif 20 <= temperatura <= 30:
        agua_por_metro_cuadrado = 5
    else:
        agua_por_metro_cuadrado = 0

    # 2. Tipo de suelo
    if tipo_suelo.lower() == "arenoso":
        agua_por_metro_cuadrado *= 1.2
    elif tipo_suelo.lower() == "arcilloso":
        agua_por_metro_cuadrado *= 0.9

    # 3. Nivel de humedad del suelo
    if humedad > 80:
        agua_por_metro_cuadrado = 0
    elif 50 <= humedad <= 80:
        agua_por_metro_cuadrado *= 0.5

    # 4. Estación del año
    if estacion.lower() == "verano":
        agua_por_metro_cuadrado *= 1.3
    elif estacion.lower() == "invierno":
        agua_por_metro_cuadrado *= 0.8

    return agua_por_metro_cuadrado

# Solicitar al usuario la información necesaria
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
tipo_suelo = input("Ingrese el tipo de suelo (Arenoso, Arcilloso, Limoso): ")
humedad = float(input("Ingrese el nivel de humedad del suelo en %: "))
estacion = input("Ingrese la estación del año (Verano, Invierno, Primavera, Otoño): ")

# Calcular el requerimiento de agua
requerimiento_agua = calcular_requerimiento_agua(temperatura, tipo_suelo, humedad, estacion)

# Mostrar el resultado
print(f"El requerimiento de agua es de {requerimiento_agua:.2f} litros por metro cuadrado.")