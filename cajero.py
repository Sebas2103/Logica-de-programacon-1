from random import randrange
import os

Saldo=randrange(15000,40000)
opcion=int(input(f"""
                                   $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo}    
           
            |1.Extraer Dinero 
            |2.Depositar Dinero
            |3.Transferir dinero
            |4.Salir  

            ------------------------------------------------------------------------------
                                                    """))
print("\n"*30)
match opcion:
    case 1:
        valor=int(input(f"""
                                   $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo}    

                            Ingrese el saldo a retirar



            ------------------------------------------------------------------------------
                                                    """))
        
        if Saldo<valor :
             print(f"""
                                $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo}    

                            Saldo insuficiente para su retiro


            ------------------------------------------------------------------------------
           """)
             print("\n"*30)
        else:
            print(f"""
                                $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo-valor}    

                            Su retiro se realizo exitosamente


            ------------------------------------------------------------------------------
           """)
            print("\n"*30)
    case 2:
        valor=int(input(f"""
                                   $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo}    

                            Ingrese el saldo a depositar


            ------------------------------------------------------------------------------
                                                    """))
        print("\n"*30)
        
        valor=int(input(f"""
                                   $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo+valor}    

                            Se realizo correctamente el deposito


            ------------------------------------------------------------------------------
                                                    """))
    case 3:
        valor=int(input(f"""
                                   $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo}    

                            Ingrese el saldo a transferir


            ------------------------------------------------------------------------------
                                                    """))
        print("\n"*30)
        if Saldo<valor :
             print(f"""
                                    $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo}    

                            Saldo insuficiente para su transferir


            ------------------------------------------------------------------------------
           """)
             print("\n"*30)
        else:
            print(f"""
                                $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo-valor}    

                            Su transferencia se realizo exitosamente


            ------------------------------------------------------------------------------
           """)
            print("\n"*30)
    
    case _:

         print(f"""
                                    $ Cajero $
            --------------------------Menu----------------------------------------------

                                Retire su tarjeta para salir
               
            ------------------------------------------------------------------------------
           """)
         print("\n"*30)