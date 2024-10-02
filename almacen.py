def calcularTP(descuento,Tpagar):
    descuento=descuento*Tpagar
    Tpagar= descuento-Tpagar
    return Tpagar
    #--------------------------------------    
def descuento(Tpago,Tpagar):
    if Tpago=="E" and Tpagar<=100000:
        descuento=0.2
    if Tpago=="T" and Tpagar<=100000:
        descuento=0.1
    #------------------------------------- 
    if Tpago=="E" and Tpagar>100000  and Tpagar<=200000:
        descuento=0.3
    if Tpago=="T" and Tpagar>100000  and Tpagar<=200000:
        descuento=0.15
    #----------------------------------------  
    if Tpago=="E" and Tpagar>200000:
        descuento=0.4
    if Tpago=="T" and Tpagar>200000:
        descuento=0.2
    #---------------------------------- 
    return descuento

tipoP=input(""" DAME EL TIPO DE PAGO """)
pagarT=float(input(""" dame el total de tu compra """))
descuento=descuento(tipoP,pagarT)
calcularTP=calcularTP(descuento,pagarT)
print(f""" este es el descuento={descuento}, y este es el total pagar={calcularTP} """)


