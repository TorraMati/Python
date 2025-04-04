palabra1 = input("Ingrese una palabra: ").lower()
palabra2 = input("Ingrese otra palabra: ").lower()
#Ordeno las letras de las palabras
if sorted(palabra1) == sorted(palabra2):
    print("Son anagramas")
else:
    print("No son anagramas")
    