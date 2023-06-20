from colorama import Fore
import os

def bienvenida(): # Texto de bienvenida
    print(Fore.LIGHTGREEN_EX+'██████╗░██╗███████╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗██╗██████╗░░█████╗░  ░█████╗░'.rjust(130))
    print('██╔══██╗██║██╔════╝████╗░██║██║░░░██║██╔════╝████╗░██║██║██╔══██╗██╔══██╗  ██╔══██╗'.rjust(130))
    print('██████╦╝██║█████╗░░██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║██║██║░░██║██║░░██║  ███████║'.rjust(130))
    print('██╔══██╗██║██╔══╝░░██║╚████║░╚████╔╝░██╔══╝░░██║╚████║██║██║░░██║██║░░██║  ██╔══██║'.rjust(130))
    print('██████╦╝██║███████╗██║░╚███║░░╚██╔╝░░███████╗██║░╚███║██║██████╔╝╚█████╔╝  ██║░░██║'.rjust(130))
    print('╚═════╝░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░░╚════╝░  ╚═╝░░╚═╝'.rjust(130))

    print('████████╗███████╗██╗░░██╗░█████╗░░██████╗  ██╗░░██╗░█████╗░██╗░░░░░██████╗░██╗███████╗███╗░░░███╗ ██████╗░░█████╗░██╗░░██╗███████╗██████╗░'.rjust(150))
    print('╚══██╔══╝██╔════╝╚██╗██╔╝██╔══██╗██╔════╝  ██║░░██║██╔══██╗██║░░░░░██╔══██╗╚█║██╔════╝████╗░████║ ██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗'.rjust(150))
    print('░░░██║░░░█████╗░░░╚███╔╝░███████║╚█████╗░  ███████║██║░░██║██║░░░░░██║░░██║░╚╝█████╗░░██╔████╔██║ ██████╔╝██║░░██║█████═╝░█████╗░░██████╔╝'.rjust(150))
    print('░░░██║░░░██╔══╝░░░██╔██╗░██╔══██║░╚═══██╗  ██╔══██║██║░░██║██║░░░░░██║░░██║░░░██╔══╝░░██║╚██╔╝██║ ██╔═══╝░██║░░██║██╔═██╗░██╔══╝░░██╔══██╗'.rjust(150))
    print('░░░██║░░░███████╗██╔╝╚██╗██║░░██║██████╔╝  ██║░░██║╚█████╔╝███████╗██████╔╝░░░███████╗██║░╚═╝░██║ ██║░░░░░╚█████╔╝██║░╚██╗███████╗██║░░██║'.rjust(150))
    print('░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░╚═╝░╚════╝░╚══════╝╚═════╝░░░░╚══════╝╚═╝░░░░░╚═╝ ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝'.rjust(150))

def rondas(ronda): # Título de cada ronda
    if ronda == 1:
        print(Fore.GREEN+'██████╗░░█████╗░███╗░░██╗██████╗░░█████╗░  ░░███╗░░'.center(150))
        print('██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗  ░████║░░'.center(150))
        print('██████╔╝██║░░██║██╔██╗██║██║░░██║███████║  ██╔██║░░'.center(150))
        print('██╔══██╗██║░░██║██║╚████║██║░░██║██╔══██║  ╚═╝██║░░'.center(150))
        print('██║░░██║╚█████╔╝██║░╚███║██████╔╝██║░░██║  ███████╗'.center(150))
        print('╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝  ╚══════╝\n'.center(150))
        print(Fore.RESET)
    
    elif ronda == 2:
        print(Fore.GREEN+'██████╗░░█████╗░███╗░░██╗██████╗░░█████╗░  ██████╗░'.center(150))
        print('██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗  ╚════██╗'.center(150))
        print('██████╔╝██║░░██║██╔██╗██║██║░░██║███████║  ░░███╔═╝'.center(150))
        print('██╔══██╗██║░░██║██║╚████║██║░░██║██╔══██║  ██╔══╝░░'.center(150))
        print('██║░░██║╚█████╔╝██║░╚███║██████╔╝██║░░██║  ███████╗'.center(150))
        print('╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝  ╚══════╝\n'.center(150))
        print(Fore.RESET)
    
    elif ronda == 3:
        print(Fore.GREEN+'██████╗░░█████╗░███╗░░██╗██████╗░░█████╗░  ██████╗░'.center(150))
        print('██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗  ╚════██╗'.center(150))
        print('██████╔╝██║░░██║██╔██╗██║██║░░██║███████║  ░█████╔╝'.center(150))
        print('██╔══██╗██║░░██║██║╚████║██║░░██║██╔══██║  ░╚═══██╗'.center(150))
        print('██║░░██║╚█████╔╝██║░╚███║██████╔╝██║░░██║  ██████╔╝'.center(150))
        print('╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝  ╚═════╝░\n'.center(150))
        print(Fore.RESET)
    
    elif ronda == 4:
        print(Fore.GREEN+'██████╗░░█████╗░███╗░░██╗██████╗░░█████╗░  ░░██╗██╗'.center(150))
        print('██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗  ░██╔╝██║'.center(150))
        print('██████╔╝██║░░██║██╔██╗██║██║░░██║███████║  ██╔╝░██║'.center(150))
        print('██╔══██╗██║░░██║██║╚████║██║░░██║██╔══██║  ███████║'.center(150))
        print('██║░░██║╚█████╔╝██║░╚███║██████╔╝██║░░██║  ╚════██║'.center(150))
        print('╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝  ░░░░░╚═╝\n'.center(150))
        print(Fore.RESET)

def titulo_reglas(): # Título reglas
    print(Fore.GREEN+'█▀█ █▀▀ █▀▀ █░░ ▄▀█ █▀   █▀▄ █▀▀   ▀█▀ █▀▀ ▀▄▀ ▄▀█ █▀   █░█ █▀█ █░░ █▀▄ ▀ █▀▀ █▀▄▀█'.center(170))
    print('█▀▄ ██▄ █▄█ █▄▄ █▀█ ▄█   █▄▀ ██▄   ░█░ ██▄ █░█ █▀█ ▄█   █▀█ █▄█ █▄▄ █▄▀ ░ ██▄ █░▀░█'.center(170))
    print(Fore.RESET)

def reglas(): # Reglas
    print(Fore.LIGHTMAGENTA_EX+"\nNúmero de jugadores:",Fore.RESET+"De 2 a 9")
            
    print(Fore.LIGHTMAGENTA_EX+"\nPreparativos:",Fore.RESET+"Antes de empezar el juego, escojes la mesa en la que te vas a sentar.")
    print(Fore.LIGHTRED_EX+"\nEl Juego:")
            
    print("\nObjetivo")
    print(Fore.RESET+"El objetivo del juego consiste en reunir la mejor mano posible para ganar así el bote (el total de fichas apostadas).")
    print("Una mano es la mejor combinación posible de 5 cartas compuestas de entre las 2 cartas personales que ningún otro jugador puede verlas (las 'Pocket Cards') y las cinco cartas comunes visibles y disponibles para todos (las 'Community Cards').")

    print(Fore.LIGHTRED_EX+"\nDesarrollo del juego")
    print(Fore.RESET+"En la primera ronda, antes de repartirse las cartas de la mesa, cada jugador recibe 2 cartas y se da la opción de hacer una apuesta o retirarse.")
    print("Gracias a estas apuestas, se pueden ganar fichas.\n")
    print("En la segunda ronda, se muestran 3 cartas encima de la mesa y se da la opción de 'Pasar', 'Apostar' o 'Retirarse'.\n")
    print("En la tercera ronda, se muestra una carta más encima de la mesa y se dan las mismas opciones.\n")
    print('Y en la última ronda, se muestra la carta final junto con las mismas opciones anteriores.\n')

    print(Fore.LIGHTRED_EX+"Ganador:"+Fore.RESET)
    print("Después de la última ronda de apuestas se comparan las manos de los jugadores que aún participan en el juego (el 'Showdown').")
    print("Si quedan dos o más jugadores, el jugador con la mejor mano de poker gana la totalidad de la apuesta.")

    manos_poker = input(Fore.LIGHTYELLOW_EX+"\nMostrar manos de poker:"+Fore.RED+" (SI / NO) "+Fore.RESET).upper() # Manos de Poker

    if manos_poker == 'SI':
        os.system('cls')
        print(Fore.LIGHTCYAN_EX+'█░█ ▄▀█ █░░ █▀█ █▀█ █▀▀ █▀   █▀▄ █▀▀   █░░ ▄▀█   █▀▄▀█ ▄▀█ █▄░█ █▀█   █▀▄ █▀▀   █▀█ █▀█ █▄▀ █▀▀ █▀█'.center(170))
        print('▀▄▀ █▀█ █▄▄ █▄█ █▀▄ ██▄ ▄█   █▄▀ ██▄   █▄▄ █▀█   █░▀░█ █▀█ █░▀█ █▄█   █▄▀ ██▄   █▀▀ █▄█ █░█ ██▄ █▀▄'.center(170)+Fore.RESET)

        print("\n",Fore.LIGHTYELLOW_EX+"(Orden: desde la mano más débil hasta la más fuerte)".center(170)+Fore.RESET)

        print("\n",Fore.LIGHTRED_EX+"1.Carta Alta (High Card)"+Fore.RESET) # Carta Alta
        print("La carta más alta gana. En caso de empate la segunda más alta gana. En caso de empate la tercera más alta gana, etc..")
        print("K-♥ | 7-♣ | 5-♥ | 3-♠ | 2-♣")

        print("\n",Fore.LIGHTRED_EX+"2.Pareja (One Pair)"+Fore.RESET) # Pareja
        print("Cualquier pareja de cartas del mismo valor. En el ejemplo se trata de una pareja de 9.")
        print("9-♦ | 9-♥ | 4-♠ | 7-♣ | 3-♣")

        print("\n",Fore.LIGHTRED_EX+"3.Doble Pareja (Two Pair)"+Fore.RESET) # Doble Pareja
        print("Cualquier pareja de cartas del mismo valor más otra pareja de cartas del mismo valor.")
        print("4-♦ | 4-♠ | 8-♣ | 8-♠ | A-♥")

        print("\n",Fore.LIGHTRED_EX+"4.Trio (Three of a Kind)"+Fore.RESET) # Trio
        print("Tres cartas del mismo valor. En el ejemplo un trio de 2.")
        print("2-♥ | 2-♦ | 2-♠ | K-♠ | 10-♦")

        print("\n",Fore.LIGHTRED_EX+"5.Escalera (Straight)"+Fore.RESET) # Escalera
        print("Cinco cartas consecutivas de distintos palos. En el ejemplo: una escalera de 6 a 10.")
        print("6-♠ | 7-♣ | 8-♦ | 9-♦ | 10-♠\n")

        input(Fore.LIGHTYELLOW_EX+"Pulsa (Enter) para Continuar -->"+Fore.RESET)
        os.system('cls')

        print(Fore.LIGHTCYAN_EX+'█░█ ▄▀█ █░░ █▀█ █▀█ █▀▀ █▀   █▀▄ █▀▀   █░░ ▄▀█   █▀▄▀█ ▄▀█ █▄░█ █▀█   █▀▄ █▀▀   █▀█ █▀█ █▄▀ █▀▀ █▀█'.center(170))
        print('▀▄▀ █▀█ █▄▄ █▄█ █▀▄ ██▄ ▄█   █▄▀ ██▄   █▄▄ █▀█   █░▀░█ █▀█ █░▀█ █▄█   █▄▀ ██▄   █▀▀ █▄█ █░█ ██▄ █▀▄'.center(170)+Fore.RESET)

        print("\n",Fore.LIGHTYELLOW_EX+"(Orden: desde la mano más débil hasta la más fuerte)".center(170)+Fore.RESET)

        print("\n",Fore.LIGHTRED_EX+"6.Color (Flush)"+Fore.RESET) # Color
        print("Cinco cartas no consecutivas del mismo color. En el ejemplo: un 'Flush' de rombos.")
        print("Q-♦ | 10-♦ | 7-♦ | 5-♦ | 3-♦")

        print("\n",Fore.LIGHTRED_EX+"7.Full (Full House)"+Fore.RESET) # Full
        print("Un trio más una pareja.")
        print("5-♥ | 5-♣ | 5-♠ | 3-♥ | 3-♠")

        print("\n",Fore.LIGHTRED_EX+"8.Poker (Four of a Kind)"+Fore.RESET) # Poker
        print("Cuatro cartas del mismo valor.")
        print("J-♣ | J-♦ | J-♠ | J-♥ | A-♦")

        print("\n",Fore.LIGHTRED_EX+"9.Escalera de Color (Straight Flush)"+Fore.RESET) # Escalera de Color
        print("Cinco cartas consecutivas del mismo palo.")
        print("4-♥ | 5-♥ | 6-♥ | 7-♥ | 8-♥")

        print("\n",Fore.LIGHTRED_EX+"10.Escalera Real de Color (Royal Flush)"+Fore.RESET) # Escalera Real de Color
        print("Las cinco cartas más altas del mismo palo, desde la 10 hasta el as.")
        print("10-♠ | J-♠ | Q-♠ | K-♠ | A-♠\n")

        input(Fore.LIGHTYELLOW_EX+"Pulsa (Enter) para Salir -->"+Fore.RESET)
        os.system('cls')