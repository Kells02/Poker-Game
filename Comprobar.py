from collections import defaultdict
from colorama import Fore
import musica

def comprobar(dic,baraja_mesa,fichas_apostadas,retirados): # Comprobar
    orden_de_valores = {1:'Carta Alta', 2:'Pareja', 3:'Doble Pareja', 4:'Trio', 5:'Escalera', 6:'Color', 7:'Full House', 8:'Poker', 9:'Escalera de Color', 10:'escalera Real'}
    orden_valor_cartas = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}
    baraja_mesa_copia = [] # Para reemplazar los valores
    
    for x in baraja_mesa:
        baraja_mesa_copia.append(x)
    
    nombres = list(dic.keys())
    cartas = list(dic.values())

    comprobar_mano(baraja_mesa,orden_valor_cartas) # Llamo a la función 'comprobar_mano'
    resultados(nombres,baraja_mesa,cartas,dic,baraja_mesa_copia,orden_valor_cartas) # Llamo a la función 'resultados'
    ganador(nombres,dic,orden_de_valores,fichas_apostadas,retirados) # Llamo a la función 'ganador'

# ------------------- Escalera Real ---------------------------
def escalera_real(baraja_mesa): # Escalera Real
    if color(baraja_mesa) and str(baraja_mesa).count("T") and str(baraja_mesa).count("A"): # Si es color y contiene la 'T=10' y el 'AS'
        return True

# ------------------- Escalera de Color ---------------------------
def escalera_color(baraja_mesa,orden_valor_cartas): # Escalera de color
    if color(baraja_mesa) and escalera(baraja_mesa,orden_valor_cartas): # Si es color y escalera
        return True

# ------------------- Poker ---------------------------
def poker(baraja_mesa): # Poker
    valores = [i[0] for i in baraja_mesa] # Mira solo los números
    numero_valores = defaultdict(lambda:0)
    for valor in valores:
        numero_valores[valor]+=1 # Aumenta el valor de la key
    if sorted(numero_valores.values()) == [1,4]: # Si hay 4 cartas del mismo número es POKER
        return True

# ------------------- Full House ---------------------------
def full_house(baraja_mesa): # Full House
    valores = [i[0] for i in baraja_mesa] # Mirar solo los números
    numero_valores = defaultdict(lambda:0) # Diccionario
    for valor in valores:
        numero_valores[valor]+=1 # Aumenta el valor de la key
    if sorted(numero_valores.values()) == [2,3]: # Si hay un trio y una pareja
        return True

# ------------------- Color ---------------------------
def color(baraja_mesa): # Color
    simbolos = [h[1] for h in baraja_mesa] # Deben de tener el mismo palo --> Mirar el símbolo
    cont = 0
    for x in range(len(simbolos)):
        if x < len(simbolos) != 5:
            if simbolos[x] == simbolos[x+1]:
                cont += 1
        else:
            if simbolos[x] == simbolos[x-1]:
                cont += 1
    if cont == 5: # Si hay 5 cartas con el mismo valor
        return True

# ------------------- Escalera ---------------------------
def escalera(baraja_mesa,orden_valor_cartas): # Escalera
    valores = [i[0] for i in baraja_mesa]
    numero_valores = defaultdict(lambda:0)
    for valor in valores:
        numero_valores[valor] += 1
    rango_valores = [orden_valor_cartas[i] for i in valores]
    distancia_valores = max(rango_valores) - min(rango_valores)
    if len(set(numero_valores.values())) == 1 and (distancia_valores==4): # Si la distancia de los valores es de 4 y van de 1 en 1
        return True

# ------------------- Trio ---------------------------
def trio(baraja_mesa): # Trio
    values = [i[0] for i in baraja_mesa] # Mira solo los números
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1 # Aumenta el valor de la key
    if set(value_counts.values()) == set([3,1]): # Si hay 3 cartas del mismo valor
        return True

# ------------------- Doble Pareja ---------------------------
def doble_pareja(baraja_mesa): # Doble Pareja
    values = [i[0] for i in baraja_mesa] # Mira solo los números
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1  # Aumenta el valor de la key
    if sorted(value_counts.values())==[1,2,2]: # Si hay 2 parejas
        return True

# ------------------- Pareja ---------------------------
def pareja(baraja_mesa): # Pareja
    values = [i[0] for i in baraja_mesa] # Mira solo los números
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1 # Aumenta el valor de la key
    if 2 in value_counts.values(): # Si hay 1 pareja
        return True

# ------------------- Comprobar Mano ---------------------------
def comprobar_mano(baraja_mesa,orden_valor_cartas):
    if escalera_real(baraja_mesa):
        return 10 # Devuelve 10, si es escalera real
    elif escalera_color(baraja_mesa,orden_valor_cartas):
        return 9 # Devuelve 9, si es escalera de color
    elif poker(baraja_mesa):
        return 8 # Devuelve 8, si es poker
    elif full_house(baraja_mesa):
        return 7 # Devuelve 7, si es full house
    elif color(baraja_mesa):
        return 6 # Devuelve 6, si es color
    elif escalera(baraja_mesa,orden_valor_cartas):
        return 5 # Devuelve 5, si es escalera
    elif trio(baraja_mesa):
        return 4 # Devuelve 4, si es trio
    elif doble_pareja(baraja_mesa):
        return 3 # Devuelve 3, si es doble pareja
    elif pareja(baraja_mesa):
        return 2 # Devuelve 2, si es pareja
    else:
        return 1 # Devuelve 1 si no es ningúna de las anteriores (Carta Alta)

def resultados(nombres,baraja_mesa,cartas,dic,baraja_mesa_copia,orden_valor_cartas): # Comprobar todas las posibilidades de tener algo con las cartas de la mesa y la de los jugadores
    # He hecho lo siguiente; Las 'x' són las cartas de la mesa y las 'y' són las cartas de cada jugador.
    # y y x x x
    # x y y x x
    # x x y y x
    # x x x y y

    valor1 = 0
    valor2 = 1
    valor_copiar = 0
    lista_final = []
    
    for x in range(len(nombres)):
        lista_final = []
        for y in range(len(baraja_mesa)-1):
            if valor2 < 5:
                baraja_mesa[valor1] = cartas[x][0][0]
                baraja_mesa[valor2] = cartas[x][0][1]
                
                valor1 += 1
                valor2 += 1
        
                resultados = comprobar_mano(baraja_mesa,orden_valor_cartas)
                lista_final.append(resultados) # Añado en la lista el resultado de la comprobación
                baraja_mesa[valor1-2] = baraja_mesa_copia[valor_copiar] # Reemplazo las cartas
                valor_copiar += 1
        
        valor1 = 0
        valor2 = 1
        valor_copiar = 0

        lista_final.sort(reverse=True) # Ordenar de mayor a menor
        dic[nombres[x]].append(lista_final[0]) # Añado el mejor resultado

def ganador(nombres,dic,orden_de_valores,fichas_apostadas,retirados): # Compruebo el ganador de la partida
    lista = []
    nombre_ganador = ''

    for x in range(len(nombres)):
        if nombres[x] not in retirados:
            lista.append(dic[nombres[x]][2]) # Añado a la lista los resultados de los jugadores
    
    lista.sort(reverse=True) # Invierto la lista

    for x in nombres:
        if x not in retirados: # Si el jugador no esta retirado
            if dic[x][2] == lista[0]: # Si el jugador és quien tiene el resultado más alto
                nombre_ganador = x

    valor_mano = orden_de_valores[lista[0]]
    
    #musica.ganar() # Música ganador

    print(Fore.GREEN+'███████╗███╗░░██╗██╗░░██╗░█████╗░██████╗░░█████╗░██████╗░██╗░░░██╗███████╗███╗░░██╗░█████╗░██╗'.rjust(135))
    print('██╔════╝████╗░██║██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝████╗░██║██╔══██╗██║'.rjust(135))
    print('█████╗░░██╔██╗██║███████║██║░░██║██████╔╝███████║██████╦╝██║░░░██║█████╗░░██╔██╗██║███████║██║'.rjust(135))
    print('██╔══╝░░██║╚████║██╔══██║██║░░██║██╔══██╗██╔══██║██╔══██╗██║░░░██║██╔══╝░░██║╚████║██╔══██║╚═╝'.rjust(135))
    print('███████╗██║░╚███║██║░░██║╚█████╔╝██║░░██║██║░░██║██████╦╝╚██████╔╝███████╗██║░╚███║██║░░██║██╗'.rjust(135))
    print('╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝\n'.rjust(135))
    print('\n',Fore.YELLOW+f'El ganador es {nombre_ganador} con {valor_mano}'.rjust(100))
    print(f'Ha ganado un total de {fichas_apostadas} fichas!'.rjust(100)+Fore.RESET)


def retirados(jugadores_IA,retirados,fichas_apostadas): # Ha ganado por que se han retirado
    #musica.ganar() # Música ganador

    for x in jugadores_IA:
        if not x in retirados:
            print(Fore.GREEN+'███████╗███╗░░██╗██╗░░██╗░█████╗░██████╗░░█████╗░██████╗░██╗░░░██╗███████╗███╗░░██╗░█████╗░██╗'.rjust(135))
            print('██╔════╝████╗░██║██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝████╗░██║██╔══██╗██║'.rjust(135))
            print('█████╗░░██╔██╗██║███████║██║░░██║██████╔╝███████║██████╦╝██║░░░██║█████╗░░██╔██╗██║███████║██║'.rjust(135))
            print('██╔══╝░░██║╚████║██╔══██║██║░░██║██╔══██╗██╔══██║██╔══██╗██║░░░██║██╔══╝░░██║╚████║██╔══██║╚═╝'.rjust(135))
            print('███████╗██║░╚███║██║░░██║╚█████╔╝██║░░██║██║░░██║██████╦╝╚██████╔╝███████╗██║░╚███║██║░░██║██╗'.rjust(135))
            print('╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝\n'.rjust(135))
            print('\n',Fore.YELLOW+f'El ganador es {x} ya que los demás jugadores se han retirado'.rjust(120))
            print(f'Ha ganado un total de {fichas_apostadas} fichas!'.rjust(110)+Fore.RESET)