def mesa(cantidad_jugadores,dic,fichas_apostadas): # Mostrar mesas
    fichas_apostadas = str(fichas_apostadas)+'💲💸'
    nombres_jugadores = list(dic.keys())

    if cantidad_jugadores == 2: # La mesa és de 2
        print(nombres_jugadores[0].center(150),'\n')
        print(fichas_apostadas.center(150),'\n')
        print(nombres_jugadores[1].center(150))
    
    elif cantidad_jugadores == 6: # La mesa és de 6
        print(nombres_jugadores[0].center(150),'\n\n')
        print(nombres_jugadores[1].center(95),nombres_jugadores[2].center(0))
        print(fichas_apostadas.center(150)) # Meter Fichas en medio
        print(nombres_jugadores[3].center(95),nombres_jugadores[4].center(0),'\n\n')
        print(nombres_jugadores[5].center(150))
    
    elif cantidad_jugadores == 9: # La mesa és de 9
        print(nombres_jugadores[0].center(90),nombres_jugadores[1].center(0),'\n\n')
        print(nombres_jugadores[2].center(65),nombres_jugadores[3].center(80),'\n\n')
        print(nombres_jugadores[4].center(65),fichas_apostadas.center(12),nombres_jugadores[5].center(43),'\n\n') # Meter Fichas en medio
        print(nombres_jugadores[6].center(90),nombres_jugadores[7].center(0),'\n\n')
        print(nombres_jugadores[8].center(147))