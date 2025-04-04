import random
import string
import datetime

usuario = input("Ingrese nombre de usuario: ").upper()
while len(usuario) > 15:
    print("El nombre no debe exceder los 15 caracteres")
    usuario = input("Ingrese nombre de usuario: ").upper()
#Tomo fecha actual    
fecha = datetime.datetime.now().strftime("%Y%m%d")

completar = 30 - len(usuario) - len(fecha)
#Tomo elementos al azar de todas las letras mayusculas y numeros que me faltan para completas 30 caracteres
completar_nombre = ''.join(random.choices(string.ascii_uppercase + string.digits, k=completar))

codigo = usuario + "-"+ fecha +"-"+ completar_nombre

print("codigo de descuento: ",codigo)