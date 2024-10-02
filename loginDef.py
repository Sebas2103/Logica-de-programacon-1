import os
def login(user,password,validacion):
    
    if user=="usuario1" and  password=="IUE":
        validacion=True

    return validacion 

#-----------------------------------------------------------------------------------
validacion=False
cont=1
while cont<=3 :
    if validacion==False:
        print(f"""------------INTENTO #{cont} ---------------""")
        Usuario=input(""" Ingrese  el Usuario """)
        Contraseña=input(""" Ingrese  la contraseña """)
        validacion=login(Usuario,Contraseña,validacion)
        cont+=1
        os.system("cls")

    if validacion==True:
        break

#----------------------------------------------------------------------------------------------------
os.system("cls")
if(validacion==True):
    print("|||Acceso Exitoso|||")
elif(validacion==False ):
    print("********Acesso Denegado*********")