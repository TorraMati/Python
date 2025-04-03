descriptions = [
"Streaming de música en vivo con covers y composiciones",
"Charla interactiva con la audiencia sobre series y películas",
"Jugamos a juegos retro y charlamos sobre su historia",
"Exploramos la mejor música de los 80s y 90s",
"Programa de entretenimiento con noticias y curiosidades del mundo gamer",
"Sesión de charla con invitados especiales del mundo del streaming",
"Música en directo con improvisaciones y peticiones del chat",
"Un espacio para charlar relajada sobre tecnología y cultura digital",
"Exploramos el impacto de la música en los videojuegos clásicos"]

musica = 0
entretenimiento = 0
charla = 0

for linea in descriptions:
    if "música" in linea.lower():
        musica+= 1
    if "entretenimiento" in linea.lower():
        entretenimiento+= 1
    if "charla " in linea.lower():
        charla+= 1
print("menciones de musica: ",musica)
print("menciones de entretenimiento: ",entretenimiento)
print("menciones de charla: ",charla)        
