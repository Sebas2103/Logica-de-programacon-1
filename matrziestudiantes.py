def datos(dat):
    from random import randint
    for sucursal in range(5):
        for mes in range(12):
            dat[mes][sucursal] = randint(0, 10)
            print(dat[mes][sucursal], end=" ")
        print()
    return dat

def prom_anual(dat, prom):
    for sucursal in range(5):
        suma = 0
        for mes in range(12):
            suma += dat[mes][sucursal]
        prom[sucursal] = suma / 12 
    return prom  # Mover el return fuera del bucle

def prom_total(prom):
    sumat = 0
    for i in range(5):
        sumat += prom[i]
    return sumat / 5

def mayores_ventas(prom, prom_general_todas_suc):
    for i in range(5):
        if prom[i] > prom_general_todas_suc:  # Corregir la comparación
            print(f"Las ventas en la sucursal {i + 1} superan el promedio.")

dat = [[0 for c in range(5)] for f in range(12)]
prom = [0 for ele in range(5)]
dat = datos(dat)
prom_suc = prom_anual(dat, prom)
print(prom_suc)
prom_general_todas_suc = prom_total(prom)  # Corregir la llamada a la función
print(prom_general_todas_suc)
mayores_ventas(prom, prom_general_todas_suc)  # Corregir la llamada a la función