# Poker Texas Hold'em
import os, random, time, pygame, mesa, texto, Comprobar, musica
from tabulate import tabulate
from colorama import Fore

def entrar_juego(): # Seleccionar si quieres jugar o salir del juego
    os.system('cls')
    opcion = int(input("Selecciona qué quieres hacer:\n1. Jugar\n2. Salir\n"))
    while opcion != 1 and opcion != 2: # En caso de que no hayas seleccionado ninguna de las dos
        os.system('cls')
        print(Fore.LIGHTRED_EX+'No has seleccionado una opción válida!'+Fore.RESET)
        opcion = int(input("Selecciona qué quieres hacer:\n1. Jugar\n2. Salir\n"))
    os.system('cls')
    return opcion # Devuelve la opcion seleccionada

def iniciar_sesion(nick_pass): # Iniciar sesión para poder jugar
    os.system('cls')
    nombre = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    if nombre in nick_pass.keys() and contraseña in nick_pass.values():
        os.system("cls")
        return nombre # Si esta registrado y ha introducido su usuario es True
    
    else:
        return False # En caso contrario es False

def registrarse(nick_pass): # Registrase para poder jugar
    os.system('cls')
    nombre = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    os.system('cls')
    nick_pass[nombre] = contraseña # Añado el nombre y la contraseña

def contraseña_nueva(nick_pass): # Cambiar contraseña de un usuario registrado
    os.system('cls')
    nombre = input("Nombre de usuario: ")
    contraseña = input("Contraseña nueva: ")
    os.system('cls')
    if nombre in nick_pass:
        nick_pass[nombre] = contraseña # Compruebo que el usuario esta registrado, y cambio la contraseña

    else:
        print(Fore.LIGHTRED_EX+"Ese usuario no existe!\n"+Fore.RESET) # Mensaje de error en caso de que no este registrado

def crear_partidas(): # Crear partidas
    partidas = {} # En este diccionario se guardan las caracteristicas de cada partida
    cantidad_mesas = 6

    # Sacar nombres para las mesas
    mesas = []
    nombre_mesa = ['Fun Phoenix','Fun Sita II','Fun Ankaios VI','Fun Leona','Fun Fricke','Fun Arlon','Fun Indus II','Fun Brambilia','Fun West','Fun Shaula II']
    
    while len(mesas) != cantidad_mesas:
        mesa = random.choice(nombre_mesa)
        if mesa not in mesas:
            mesas.append(mesa)
        partidas['Mesa'] = mesas

    # Sacar ID's
    numeros = []
    
    while len(numeros) != cantidad_mesas:
        id = random.randint(1,cantidad_mesas)
        if id not in numeros:
            numeros.append(id)
        partidas['ID'] = numeros

    # Sacar apuesta de cada mesa
    apuesta_inicial = []
    dinero_mesa = [50,100,200,300]

    while len(apuesta_inicial) != cantidad_mesas:
        apuestas = random.choice(dinero_mesa)
        apuesta_inicial.append(apuestas)
        partidas['Apuestas'] = apuesta_inicial

    # Sacar cantidad de jugadores en cada mesa
    jugadores = []
    cantidad_jugadores = [2,6,9]

    while len(jugadores) != cantidad_mesas:
        jugadores_aleatorios = random.choice(cantidad_jugadores)
        jugadores.append(jugadores_aleatorios)
        partidas['Jugadores'] = jugadores
    
    return partidas # Devuelvo el diccionario 'partidas'

def menu(nombre_jugador): # En el menu puedo entrar en una partida o leer las reglas del juego
    #musica.menu() # Musica del menu

    partidas = crear_partidas() # Llamo a la funcion 'crear_partidas'

    id = partidas['ID'] # Número ID
    table = partidas['Mesa'] # Nombre Mesa
    apuesta = partidas['Apuestas'] # Apuesta
    jugador = partidas['Jugadores'] # Cantidad jugadores
    
    tabla = [[id[0],table[0],apuesta[0],jugador[0]],
        [id[1],table[1],apuesta[1],jugador[1]],
        [id[2],table[2],apuesta[2],jugador[2]],
        [id[3],table[3],apuesta[3],jugador[3]],
        [id[4],table[4],apuesta[4],jugador[4]],
        [id[5],table[5],apuesta[5],jugador[5]]]

    texto.bienvenida() # Texto de bienvenida
    mostrar = Fore.WHITE+"1.Mostrar Mesas | 2.Reglas de Texas Hold'em "
    print('\n',mostrar.center(180))

    opcion = 0

    while opcion != 1: # Mientras opcion sea distinto a 1 mostrara lo siguiente
        opcion = int(input())
        if opcion == 1: # Si opcion es 1, mostrará la tabla en la cual se selecciona la mesa en la cual quiero jugar
            os.system('cls')
            print(tabulate(tabla, headers=["ID Mesa","Mesa", "Apuestas", "Jugadores"])) # Tabla
            entrar_mesa = int(input(Fore.LIGHTMAGENTA_EX+"\nSelecciona la mesa: "+Fore.RESET))

            while entrar_mesa != 1 and entrar_mesa != 2 and entrar_mesa != 3 and entrar_mesa != 4 and entrar_mesa != 5 and entrar_mesa != 6: # En caso de no haber seleccionado una mesa válida
                print(Fore.LIGHTRED_EX+'No has seleccionado una mesa válida!'+Fore.RESET)
                entrar_mesa = int(input(Fore.LIGHTMAGENTA_EX+"\nSelecciona la mesa: "+Fore.RESET))

            for x in tabla:
                carcateristicas_mesa = []
                if x[0] == entrar_mesa:
                    os.system('cls')
                    carcateristicas_mesa.append(x)
                    crear_baraja(carcateristicas_mesa,nombre_jugador) # Devolver carcteristicas de la mesa seleccionada
    
        elif opcion == 2: # Reglas del Juego
            os.system('cls')
            
            texto.titulo_reglas() # Mostrar título
            texto.reglas() # Mostrar reglas
            os.system('cls')
            texto.bienvenida() # Texto de bienvenidas
            mostrar = Fore.WHITE+"1.Mostrar Mesas | 2.Reglas de Texas Hold'em "
            print('\n',mostrar.center(180))

def crear_baraja(carcateristicas_mesa,nombre_jugador): # En esta función se crean las barajas de los jugadores
    dic = {} # En este diccionario se guardan las barajas de cada jugador y sus fichas
    baraja_fichas = []
    cantidad_jugadores = carcateristicas_mesa[0][3]
    fichas = 1500

    jugadores_IA = []
    jugadores = [nombre_jugador,'HatriX3','Remilio92','Glaxtoun1','Sovi_03','xLoui','RenGaR6','tRank_s','BraPrixx']

    for x in jugadores:
        if len(jugadores_IA) != cantidad_jugadores:
            jugadores_IA.append(x)

    # Crear Barajas
    numeros = ["A","2","3","4","5","6","7","8","9","T",'J','K','Q']
    simbolos = ["♥","♦","♣","♠"]

    barajas = []
    baraja_mesa = []

    while len(barajas) != cantidad_jugadores*2: # CREAR BARAJAS JUGADORES
        numero = str(random.choice(numeros))
        simbolo = str(random.choice(simbolos))

        baraja_final = numero+simbolo

        if baraja_final not in barajas: # Si la baraja no esta creada se añade
            barajas.append(baraja_final)

    while len(baraja_mesa) != 5: # CREAR BARAJAS MESA
        numero = str(random.choice(numeros))
        simbolo = str(random.choice(simbolos))
        baraja = numero+simbolo

        if baraja not in barajas and baraja not in baraja_mesa: # Si la baraja no esta creada se añade
            baraja_mesa.append(baraja)

    pos1 = 0
    pos2 = 2

    for jugador in jugadores_IA: # Añado a cada jugador su mano junto a sus fichas en el diccionario
        baraja_fichas.append(barajas[pos1:pos2])
        baraja_fichas.append(fichas)

        dic[jugador] = baraja_fichas
        baraja_fichas = []
        
        pos1 += 2
        pos2 += 2
    
    mi_baraja = str(dic[nombre_jugador][0:1])
    mi_baraja = mi_baraja.replace('[','')
    mi_baraja = mi_baraja.replace('(','')
    mi_baraja = mi_baraja.replace(']','')
    mi_baraja = mi_baraja.replace(')','')
    mi_baraja = mi_baraja.replace(',','')
    mi_baraja = mi_baraja.replace("'",'')
    mi_baraja = mi_baraja.replace(' ','')
    carta1 = "".join(mi_baraja[0:2])
    carta2 = "".join(mi_baraja[2:5])
    
    mi_baraja = []
    mi_baraja.append(carta1)
    mi_baraja.append(carta2)
    
    mi_mano = carta1+' | '+carta2
    apuesta_minima = carcateristicas_mesa[0][2]

    partida(dic,mi_mano,nombre_jugador,cantidad_jugadores,jugadores_IA,apuesta_minima,baraja_mesa) # Llamo a la función 'partida'


def partida(dic,mi_mano,nombre_jugador,cantidad_jugadores,jugadores_IA,apuesta_minima,baraja_mesa): # Empezar partida
    #musica.partida() # Música de la partida

    retirados = [] # Lista de retirados
    ronda = 1
    mis_fichas = dic[nombre_jugador][1]
    fichas_apostadas = 0
   
    print(Fore.YELLOW+"La partida empieza en..") # TEMPORIZADOR
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1'+Fore.RESET)
    os.system('cls')

    while not ronda > 4 and len(retirados) != cantidad_jugadores-1: # Mientras no sea mayor a 4 y que la cantidad de retirados sea distinta a la cantidad de participantes -1.
        os.system('cls')
        texto.rondas(ronda) # Mostrar texto de cada ronda
        mesa.mesa(cantidad_jugadores,dic,fichas_apostadas) # Mostrar mesa
    
        print(Fore.LIGHTMAGENTA_EX+'Mi Mano: '+Fore.WHITE,mi_mano)
        print(Fore.LIGHTMAGENTA_EX+'Mis Fichas: '+Fore.WHITE,mis_fichas,'💲')

        partida = jugar(ronda,nombre_jugador,dic,jugadores_IA,mis_fichas,apuesta_minima,retirados,baraja_mesa)
        mis_fichas = dic[nombre_jugador][1]
        fichas_apostadas += partida # Sumar fichas
        ronda += 1 # Pasar de ronda
    
    os.system('cls')
    if len(retirados) != cantidad_jugadores-1:
        Comprobar.comprobar(dic,baraja_mesa,fichas_apostadas,retirados) # Comprobar ganador si hay más de 1 jugador
    else:
        Comprobar.retirados(jugadores_IA,retirados,fichas_apostadas) # Comprovar ganador si hay menos de 1 jugador
    dic = {}
        

def jugar(ronda,nombre_jugador,dic,jugadores_IA,mis_fichas,apuesta_minima,retirados,baraja_mesa): # Está funcion llama a las 'rondas'
    apuestas = [] # Todas las apuestas que se han hecho
    cartas_mesa = baraja_mesa
    
    if ronda == 1:
        r1 = ronda1(apuesta_minima,jugadores_IA,nombre_jugador,retirados,mis_fichas,apuestas,dic) # Llamo a 'ronda1'
        fichas_apostadas = r1
        return fichas_apostadas # Devuelvo fichas apostadas
    
    elif ronda == 2:
        r2 = ronda2(cartas_mesa,jugadores_IA,nombre_jugador,retirados,apuesta_minima,apuestas,dic,mis_fichas) # Llamo a 'ronda2'
        fichas_apostadas = r2
        return fichas_apostadas # Devuelvo fichas apostadas

    elif ronda == 3:
        r3 = ronda3(cartas_mesa,jugadores_IA,nombre_jugador,retirados,apuesta_minima,apuestas,dic,mis_fichas) # Llamo a 'ronda3'
        fichas_apostadas = r3
        return fichas_apostadas # Devuelvo fichas apostadas

    elif ronda == 4:
        r4 = ronda4(cartas_mesa,jugadores_IA,nombre_jugador,retirados,apuesta_minima,apuestas,dic,mis_fichas) # Llamo a 'ronda4'
        fichas_apostadas = r4
        return fichas_apostadas # Devuelvo fichas apostadas

def ronda1(apuesta_minima,jugadores_IA,nombre_jugador,retirados,mis_fichas,apuestas,dic): # Jugar Ronda 1
    print(Fore.YELLOW+'La apuesta minima es de:'+Fore.WHITE,apuesta_minima ,'fichas!')
    for jugador in jugadores_IA:
        if jugador == nombre_jugador and jugador not in retirados: # Si no és un BOT y no se ha retirado
            print("\n¿Qué quieres hacer?"+Fore.LIGHTGREEN_EX+' 1.Apostar ','/'+Fore.RED+ ' 2.Retirarte'+Fore.RESET)
            respuesta = int(input())
            if respuesta == 1: # Llama a la función 'apostar_mi_jugador_ronda_1'
                apostar_mi_jugador_ronda_1(apuesta_minima,dic,apuestas,jugador,mis_fichas)
            
            elif respuesta == 2 and len(retirados) < len(jugadores_IA)-1:
                retirarse(retirados,jugador) # Llama a la función 'retirase'
            
            while respuesta != 1 and respuesta != 2: # Si no ha seleccionado una opción válida
                print(Fore.LIGHTRED_EX+'No has seleccionado una opción válida!'+Fore.RESET)
                respuesta = int(input())
                if respuesta == 1: # Llama a la función 'apostar_mi_jugador_ronda_1'
                    apostar_mi_jugador_ronda_1(apuesta_minima,dic,apuestas,jugador,mis_fichas)
            
                elif respuesta == 2 and len(retirados) < len(jugadores_IA)-1:
                    retirarse(retirados,jugador) # Llama a la función 'retirase'
        
        elif jugador != nombre_jugador and jugador not in retirados: # Si és un BOT y no se ha retirado
            respuesta = random.randint(1,2)
            if respuesta == 1: # Llama a la función 'apostar_IA_ronda_1'
                apostar_IA_ronda_1(apuesta_minima,apuestas,dic,jugador)

            elif respuesta == 2 and len(retirados) < len(jugadores_IA)-1:
                retirarse(retirados,jugador) # Llama a la función 'retirase'
        
    devolver = sum(apuestas) # Suma de todas las apuestas
    limpiar = input(Fore.YELLOW+"\nPulsa (Enter) para borrar la pantalla."+Fore.WHITE)
    return devolver # Devuelvo la suma de todas las apuestas


def ronda2(cartas_mesa,jugadores_IA,nombre_jugador,retirados,apuesta_minima,apuestas,dic,mis_fichas): # Jugar Ronda 2
    carta1 = ''.join(cartas_mesa[0])
    carta2 = ''.join(cartas_mesa[1])
    carta3 = ''.join(cartas_mesa[2])

    print(Fore.LIGHTMAGENTA_EX+'Cartas Mesa:'+Fore.WHITE,carta1,'|',carta2,'|',carta3,'\n') # --> MOSTRAR 3 CARTAS

    jugar = jugar_rondas(jugadores_IA,nombre_jugador,retirados,apuesta_minima,apuestas,dic,mis_fichas) # Llamo a la función 'jugar_rondas'
    fichas_apostadas = jugar
    return fichas_apostadas # Devuelvo las fichas apostadas

def ronda3(cartas_mesa,jugadores_IA,nombre_jugador,retirados,apuesta_minima,apuestas,dic,mis_fichas): # Jugar Ronda 3
    carta1 = ''.join(cartas_mesa[0])
    carta2 = ''.join(cartas_mesa[1])
    carta3 = ''.join(cartas_mesa[2])
    carta4 = ''.join(cartas_mesa[3])

    print(Fore.LIGHTMAGENTA_EX+'Cartas Mesa:'+Fore.WHITE,carta1,'|',carta2,'|',carta3,'|',carta4,'\n') # MOSTRAR 4 CARTAS

    jugar = jugar_rondas(jugadores_IA,nombre_jugador,retirados,apuesta_minima,apuestas,dic,mis_fichas) # Llamo a la función 'jugar_rondas'
    fichas_apostadas = jugar
    return fichas_apostadas # Devolver las fichas apostadas

def ronda4(cartas_mesa,jugadores_IA,nombre_jugador,retirados,apuesta_minima,apuestas,dic,mis_fichas): # Jugar Ronda 4
    carta1 = ''.join(cartas_mesa[0])
    carta2 = ''.join(cartas_mesa[1])
    carta3 = ''.join(cartas_mesa[2])
    carta4 = ''.join(cartas_mesa[3])
    carta5 = ''.join(cartas_mesa[4])
        
    print(Fore.LIGHTMAGENTA_EX+'Cartas Mesa:'+Fore.WHITE,carta1,'|',carta2,'|',carta3,'|',carta4,'|',carta5,'\n') # MOSTRAR 5 CARTAS

    jugar = jugar_rondas(jugadores_IA,nombre_jugador,retirados,apuesta_minima,apuestas,dic,mis_fichas) # Llamo a la función 'jugar_rondas'
    fichas_apostadas = jugar
    return fichas_apostadas # Devuelvo las fichas apostadas

def jugar_rondas(jugadores_IA,nombre_jugador,retirados,apuesta_minima,apuestas,dic,mis_fichas): # Jugar Rondas 2-3-4
    jugadores_pasar = [] # Jugadores que han pasado
    jugadores_apuestan = False
    mi_respuesta = ''
    respuesta_IA = random.randint(1,3)
        
    for jugador in jugadores_IA:
        if jugador == nombre_jugador and jugador not in retirados: # Mientras mi jugador no este retirado
            print("\n¿Qué quieres hacer?"+Fore.LIGHTYELLOW_EX+' 1.Pasar /'+Fore.LIGHTGREEN_EX+ ' 2.Apostar / '+Fore.RED+ '3.Retirarte'+Fore.RESET)
            respuesta_jugador = int(input())
            if respuesta_jugador == 1:
                pasar_turno(jugadores_pasar,jugador) # Llamo a la función 'pasar_turno'

            elif respuesta_jugador == 2:
                apostar_mi_jugador_ronda_2(apuesta_minima,mis_fichas,dic,apuestas,jugador,retirados) # Llamo a la función 'apostar_mi_jugador_ronda_2'
                jugadores_apuestan = True
                      
            elif respuesta_jugador == 3 and len(retirados) < len(jugadores_IA)-1: # Si es 3 y hay menos retirados que jugadores-1.
                retirarse(retirados,jugador) # Llamo a la función 'retirarse'
            
            while respuesta_jugador != 1 and respuesta_jugador != 2 and respuesta_jugador != 3: # Si no he seleccionado una opción válida
                print(Fore.LIGHTRED_EX+'No has seleccionado una opción válida!'+Fore.RESET)
                respuesta_jugador = int(input())
                if respuesta_jugador == 1:
                    pasar_turno(jugadores_pasar,jugador) # Llamo a la función 'pasar_turno'
            
                elif respuesta_jugador == 2:
                    apostar_mi_jugador_ronda_2(apuesta_minima,mis_fichas,dic,apuestas,jugador,retirados) # Llamo a la función 'apostar_mi_jugador_ronda_2'
                    jugadores_apuestan = True
                
                elif respuesta_jugador == 3 and len(retirados) < len(jugadores_IA)-1:
                    retirarse(retirados,jugador) # Llamo a la función 'retirados'
            
            mi_respuesta = respuesta_jugador
    
        elif jugador != nombre_jugador and jugador not in retirados: # BOTS que no esten retirados
            if mi_respuesta == 1 or respuesta_IA == 1: # Si yo paso la IA tiene 3 opciones --> PASAR | APOSTAR | RETIRAESE
                respuesta_IA = random.randint(1,3)
                if respuesta_IA == 1:
                    pasar_turno(jugadores_pasar,jugador) # Llama a la función 'pasar_turno'
                    
                elif respuesta_IA == 2:
                    apostar_IA_ronda_2(apuesta_minima,dic,jugador,apuestas,retirados) # Llama a la función 'apostar_IA_ronda_2'
                    jugadores_apuestan = True

                elif respuesta_IA == 3 and len(retirados) < len(jugadores_IA)-1:
                    retirarse(retirados,jugador) # Llama a la función 'retirarse'

            elif mi_respuesta == 2 or respuesta_IA == 2: # Si yo apuesto la IA tiene 2 opciones --> APOSTAR | RETIRARSE
                respuesta_IA = random.randint(2,3)
                if respuesta_IA == 2:
                    apostar_IA_ronda_2(apuesta_minima,dic,jugador,apuestas,retirados) # Llama a la función 'apostar_IA_ronda_2'
                    jugadores_apuestan = True
    
                elif respuesta_IA == 3 and len(retirados) < len(jugadores_IA)-1:
                    retirarse(retirados,jugador) # Llama a la función 'retirarse'

            elif mi_respuesta == 3 or respuesta_IA == 3: # SI yo me retiro la IA tiene 3 opciones --> PASAR | APOSTAR | RETIRARSE
                respuesta_IA = random.randint(1,3)
                if respuesta_IA == 1:
                    pasar_turno(jugadores_pasar,jugador) # Llama a la función 'pasar_turno'
                    
                elif respuesta_IA == 2:
                    apostar_IA_ronda_2(apuesta_minima,dic,jugador,apuestas,retirados) # Llama a la función 'apostar_IA_ronda_2'
                    jugadores_apuestan = True

                elif respuesta_IA == 3 and len(retirados) < len(jugadores_IA)-1:
                    retirarse(retirados,jugador) # Llama a la función 'retirarse'
        
    if len(jugadores_pasar) > 0 and jugadores_apuestan == True: # Jugadores que han pasado
        for jugador in jugadores_pasar:
            if jugador == nombre_jugador: # Si es mi jugador
                print("\n¿Qué quieres hacer?"+Fore.LIGHTGREEN_EX+' 1.Apostar ','/'+Fore.RED+ ' 2.Retirarte'+Fore.WHITE)
                respuesta_jugador = int(input())

                if respuesta_jugador == 1:
                    apostar_mi_jugador_ronda_2(apuesta_minima,mis_fichas,dic,apuestas,jugador,retirados) # Llama a la función 'apostar_mi_jugador_ronda_2'

                elif respuesta_jugador == 2 and len(retirados) < len(jugadores_IA)-1:
                    retirarse(retirados,jugador) # Llama a la función 'retirase'
                
                while respuesta_jugador != 1 and respuesta_jugador != 2: # Si no ha seleccionado una opción válida
                    print(Fore.LIGHTRED_EX+'No has seleccionado una opción válida!'+Fore.RESET)
                    respuesta_jugador = int(input())

                    if respuesta_jugador == 1:
                        apostar_mi_jugador_ronda_2(apuesta_minima,mis_fichas,dic,apuestas,jugador,retirados) # Llama a la función 'apostar_mi_jugador_ronda_2'

                    elif respuesta_jugador == 2 and len(retirados) < len(jugadores_IA)-1:
                        retirarse(retirados,jugador) # Llama a la función 'retirase'
                    
            elif jugador != nombre_jugador: # IA
                respuesta_IA = random.randint(1,2)

                if respuesta_IA == 1:
                    apostar_IA_ronda_2(apuesta_minima,dic,jugador,apuestas,retirados) # Llama a la función 'apostar_IA_ronda_2'

                elif respuesta_IA == 2 and len(retirados) < len(jugadores_IA)-1:
                    retirarse(retirados,jugador) # Llama a la función 'retirase'

    limpiar = input(Fore.YELLOW+"\nPulsa (Enter) para borrar la pantalla."+Fore.WHITE)
    devolver = sum(apuestas)
    return devolver # Devuelvo las apuestas

def pasar_turno(jugadores_pasar,jugador):
    jugadores_pasar.append(jugador) # Añado el jugador que ha pasado turno a la lista 'jugadores_pasar'
    print(f"El jugador {jugador} ha pasado")

def apostar_mi_jugador_ronda_1(apuesta_minima,dic,apuestas,jugador,mis_fichas):
    apuesta = apuesta_minima # La apuesta es la apuesta mínima que tiene definida cada mesa
    mis_fichas = mis_fichas-apuesta # Resto mis fichas
    print(f"El jugador {jugador} ha apostado {apuesta}")
    dic[jugador][1] = mis_fichas # Añado las fichas al diccionario
    apuestas.append(apuesta) # Añado la apuesta a la lista 'apuestas'

def apostar_IA_ronda_1(apuesta_minima,apuestas,dic,jugador):
    apuesta = apuesta_minima # La apuesta es la apuesta mínima que tiene definida cada mesa
    apuestas.append(apuesta) # Añado la apuesta a la lista 'apuestas'
    print(f"El jugador {jugador} ha apostado {apuesta}")
    sus_fichas = dic[jugador][1] # Añado las fichas al diccionario
    dic[jugador][1] = sus_fichas - apuesta # Resto las fichas

def apostar_mi_jugador_ronda_2(apuesta_minima,mis_fichas,dic,apuestas,jugador,retirados):
    apuesta = apuesta_minima

    if apuesta > mis_fichas: # Si la apuesta és mayor a mis fichas, me retiro
        print(f"Tu apuesta és mayor que tus fichas: {mis_fichas}!")
        retirarse(retirados,jugador) # Llamo a la función 'retirados'
                    
    else:
        mis_fichas = mis_fichas-apuesta
        print(f"El jugador {jugador} ha apostado {apuesta}")
        dic[jugador][1] = mis_fichas             
        apuestas.append(apuesta) # Añado la apuesta a la lista 'apuestas'
    
def apostar_IA_ronda_2(apuesta_minima,dic,jugador,apuestas,retirados):
    apuesta = apuesta_minima
    sus_fichas = dic[jugador][1]
                
    if apuesta > sus_fichas: # Si la apuesta és mayor a mis fichas, me retiro
        retirarse(retirados,jugador)

    else:
        apuestas.append(apuesta) # Añado la apuesta a la lista 'apuestas'
        print(f"El jugador {jugador} ha apostado {apuesta}")
        dic[jugador][1] = sus_fichas - apuesta

def retirarse(retirados,jugador):
    retirados.append(jugador) # Añado el jugador a la lista de retirados
    print(f"El jugador {jugador} se ha retirado")

def main ():
    nick_pass = {'Kells_02':'1234'} # En este diccionario se guardan los usuarios y contraseñas
    opcion = entrar_juego() # Llamo a la función 'entrar_juego'
    while opcion == 1: # Si vale 1 entras al juego
        print("1.Inicia Sesión\n2.Registrarme\n3.¿Olvidaste tu contraseña?")
        respuesta = int(input())
        if respuesta == 1:
            seguir_jugando = 1
            nombre_jugador = iniciar_sesion(nick_pass)
            while nombre_jugador != False and seguir_jugando != 2: # Si es correcto entro en el menu
                menu(nombre_jugador) # Llamo a la función 'menu'
                seguir_jugando = int(input("\n¿Quieres seguir jugando?"+Fore.LIGHTGREEN_EX+" 1.SI /"+Fore.LIGHTRED_EX+" 2.NO "+Fore.RESET))
                #pygame.mixer.stop() # Parar la música    
                os.system('cls')
            
            if nombre_jugador == False:
                os.system('cls')
                print(Fore.LIGHTRED_EX+"No existe este usuario/contraseña!\n"+Fore.RESET)
            else:
                opcion = 2

        elif respuesta == 2:
            registrarse(nick_pass) # Me registro
        
        elif respuesta == 3: # Cambio la contraseña
            contraseña_nueva(nick_pass)
        else:
            os.system('cls')
            print(Fore.LIGHTRED_EX+'No has seleccionado una opción válida!'+Fore.RESET)

    print(Fore.LIGHTRED_EX+'Hasta pronto!'+Fore.RESET)
main()