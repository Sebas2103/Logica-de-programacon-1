from random import randrange
import os

Saldo=randrange(15000,4000000000)
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
os.system("cls")
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
             os.system("cls")
             print(f"""
                                $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo}    

                            Saldo insuficiente para su retiro


            ------------------------------------------------------------------------------
           """)
            

        else:
            os.system("cls")
            print(f"""
                                $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo-valor}    

                            Su retiro se realizo exitosamente


            ------------------------------------------------------------------------------
           """)
         

            
    case 2:
        os.system("cls")
        valor=int(input(f"""
                                   $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo}    

                            Ingrese el saldo a depositar


            ------------------------------------------------------------------------------
                                                    """))
        
        os.system("cls")
        valor=int(input(f"""
                                   $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo+valor}    

                            Se realizo correctamente el deposito


            ------------------------------------------------------------------------------
                                                    """))
        

    case 3:
        os.system("cls")
        valor=int(input(f"""
                                   $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo}    

                            Ingrese el saldo a transferir


            ------------------------------------------------------------------------------
                                                    """))
        
        if Saldo<valor :
          os.system("cls")
          print(f"""
                                    $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo}    

                            Saldo insuficiente para su transferencia


            ------------------------------------------------------------------------------
           """)
             

            
        else:
          os.system("cls")
          print(f"""
                                $ Cajero $
            --------------------------Menu----------------------------------------------
             Saldo : {Saldo-valor}    

                            Su transferencia se realizo exitosamente


            ------------------------------------------------------------------------------
           """)
         

          
    
    case  None:
         os.system("cls")
         print(f"""
                                    $ Cajero $
            --------------------------Menu----------------------------------------------

                                      Error
                                Retire su tarjeta para salir
               
            ------------------------------------------------------------------------------
           """)
    case  _:
         os.system("cls")
         print(f"""
                                    $ Cajero $
            --------------------------Menu----------------------------------------------

                                    
                                Retire su tarjeta para salir
            ------------------------------------------------------------------------------
           """)
        
         