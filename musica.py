import pygame
import os

def menu(): # Música menu
    path = os.path.dirname(os.path.realpath(__file__)).replace("\\",'/') # Path en el que se encuentra el archivo
    path1 = path[0:3]
    
    for r, d, f in os.walk(path1): # Encontrar ruta del archivo mp3
        for files in f:
            if files == "menu.mp3":
                carpeta = os.path.join(r,files)

    pygame.init()
    pygame.mixer.init()
    sonido_fondo = pygame.mixer.Sound(carpeta) 
    pygame.mixer.Sound.play(sonido_fondo, -1) # Con -1 indicamos que queremos que se repita indefinidamente

def partida(): # Música partida
    pygame.mixer.stop() # Paramos música
    path = os.path.dirname(os.path.realpath(__file__)).replace("\\",'/')
    path1 = path[0:3]
    
    for r, d, f in os.walk(path1): # Encontrar ruta del archivo mp3
        for files in f:
            if files == "musica2.mp3":
                carpeta = os.path.join(r,files)

    musica = pygame.mixer.Sound(carpeta)
    pygame.mixer.Sound.play(musica, -1) # Repoducimos música

def ganar(): # Música ganador
    pygame.mixer.stop() # Paramos música
    path = os.path.dirname(os.path.realpath(__file__)).replace("\\",'/')
    path1 = path[0:3]
    
    for r, d, f in os.walk(path1): # Encontrar ruta del archivo mp3
        for files in f:
            if files == "dinero.mp3":
                carpeta = os.path.join(r,files)

    musica = pygame.mixer.Sound(carpeta)
    pygame.mixer.Sound.play(musica) # Reproducimos música