# Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas listas, 
# una con los número pares y otras con los que son impares. 
# Imprima las listas al terminar de procesarlas.

lista = [1,2,3,4,5,6,7,8,9,10]
lista_par = []
lista_impar = []
for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print(lista_par)
print(lista_impar)
    