import string
import random

def bann_text():
    clr()
    logo = """
                ██  ██ ██▒█▒██ ██▒▒██
                ██  ██ ██ ▒ ██ ██  ██
                   ▒████▒ ██   ██ █████▒
      
                                         """
                                         
                                         
    print(logo)           

longitud = int (input("Ingrese el tamaño de la contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation  

contrasena = "".join(random.choice(caracteres) for i in range(longitud))

print ("La contraseña generada es: " + contrasena)