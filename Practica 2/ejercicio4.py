nombre = input("Ingrese un nombre de usuario: ")
if len(nombre) < 5:
    print("el nombre debe contener 5 o mas caracteres")
else:
    numero = False
    mayuscula = False
    solo_letras_y_numeros = True

    for char in nombre:
        if char.isdigit():
            numero = True
        if char.isupper():
            mayuscula = True
        if not char.isalnum():
            solo_letras_y_numeros = False
            break
    if not numero:
        print("el nombre debe contener al menos un numero")
    elif not mayuscula:
        print("el nombre debe contener al menos una mayuscula")
    elif not solo_letras_y_numeros:
        print("el nombre solo puede contener letras y numeros")
    else:
        print("nombre de usuario valido")