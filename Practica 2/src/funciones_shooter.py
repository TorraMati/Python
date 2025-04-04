def calcular_puntaje(kills, assists, deaths):
    return (kills * 3) + (assists * 1) + (-1 if deaths else 0)

def actualizar_estadisticas(jugadores, ronda):
    puntajes_ronda = {}
    
    for jugador, datos in ronda.items():
        kills = datos['kills']
        assists = datos['assists']
        deaths = datos['deaths']
        puntos = calcular_puntaje(kills, assists, deaths)

        if jugador not in jugadores:
            jugadores[jugador] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'puntos': 0}

        jugadores[jugador]['kills'] += kills
        jugadores[jugador]['assists'] += assists
        jugadores[jugador]['deaths'] += 1 if deaths else 0
        jugadores[jugador]['puntos'] += puntos

        puntajes_ronda[jugador] = puntos

    return puntajes_ronda

def obtener_mvp(puntajes_ronda):
    mvp = None
    mayor_puntaje = -99999

    for jugador, puntaje in puntajes_ronda.items():
        if puntaje > mayor_puntaje:
            mayor_puntaje = puntaje
            mvp = jugador
    return mvp

def imprimir_ranking(jugadores, ronda_num=None):
    if ronda_num:
        print(f"\nRanking ronda {ronda_num}:")
    else:
        print("\nRanking final:")
    
    print(f"{'Jugador':<10} {'Kills':<10} {'Asistencias':<12} {'Muertes':<10} {'MVPs':<6} {'Puntos':<6}")
    print('-' * 60)

    ranking = sorted(jugadores.items(), key=lambda x: x[1]['puntos'], reverse=True)

    for jugador, stats in ranking:
        print(f"{jugador:<10} {stats['kills']:<10} {stats['assists']:<12} {stats['deaths']:<10} {stats['mvps']:<6} {stats['puntos']:<6}")
    
    print('-' * 60)