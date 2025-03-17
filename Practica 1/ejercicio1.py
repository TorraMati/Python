# Desarrolla un programa que solicite al usuario que ingrese su edad 
# y luego calcule y muestre cuántos años le faltan para alcanzar los 100 años.

edad = int(input("Ingresa tu edad para saber cuanto faltaria para que llegues a los 100: "))
edad_faltante = 100 - edad
print("Ingresaste el numero",edad,", por lo que te faltan",edad_faltante,"para llegar a los 100")