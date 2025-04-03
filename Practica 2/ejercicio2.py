titles = [
"Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Música en vivo: improvisaciones al piano"
]

titulo_mas_largo= ""
cant_palabras= 0

#Cuento la cantidad de palabras de cada linea y guardo la mas larga

for titulo in titles:
    conteo = len(titulo.split())
    if conteo > cant_palabras:
        titulo_mas_largo = titulo
        cant_palabras = conteo

print(titulo_mas_largo)