# Implementa un programa que solicite al usuario que ingrese una lista de números. 
# Luego, imprime la lista pero detén la impresión si encuentras un número negativo. 
# Nota: utilice la sentencia `break` cuando haga falta.

lista = []
num = input("Ingresa una lista de numeros separada por espacios: ")
numeros_str = num.split(" ")
for i in numeros_str:
    lista.append(int(i))
print("lista de numeros ingresada: ", lista)

for n in lista:
    if n >= 0:
        print(n)
    else:
        break