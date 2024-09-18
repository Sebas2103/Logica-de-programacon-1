#Diseñar un algoritmo que sume los gatos realizados en un viaje tenga en cuenta que se desconoce la cantidad gastos realizados
gastos=0
opcion="no"
while opcion!="si":
    viaje=int(input(""" Ingrese los gastos del viaje """))
    opcion=input("Deasea escriba si o no ")
    gastos+=viaje
print(f""" Los gatos totales son {gastos} """)