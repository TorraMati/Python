rules = """Respeta a los demás. No se permiten insultos ni lenguaje
ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""
#Separo las reglas en lineas
reglas_en_linea= rules.split("\n")
#.lower para que no distinga entre mayusculas y minusculas
clave = input("Ingrese una palabra clave: ").lower()

encontre= False

for reglas in reglas_en_linea:
    if clave in reglas.lower():
        print("- " + reglas)
        encontre = True
if not encontre:
    print("No se encontro ninguna regla con esa clave")