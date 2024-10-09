# Ejecutar archivo con "python -m Corridas.MovWander.py" en caso de no usar
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# y colocar es punto punto, es decir: from ..Clases.Wander import Wander
# Taambien colocar el archivo "__init__.py" en cada carpeta

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from Clases.Wander import Wander
from Clases.SteeringOutput import SteeringOutput
from Clases.Kinematic import Kinematic
from Clases.funciones import movimiento_teclado_cambio_velocity,rotate_polygon
import numpy as np
import math

o111 = Kinematic([150,100],[0,0],0,0) # Personaje (Wandering) 
o112 = Kinematic([150,200],[0,0],0,0) # Personaje (Wandering) 
o113 = Kinematic([150,300],[0,0],0,0) # Personaje (Wandering) 
o114 = Kinematic([150,400],[0,0],0,0) # Personaje (Wandering) 
o115 = Kinematic([150,500],[0,0],0,0) # Personaje (Wandering) 

t111 = Kinematic([250,100],[0,0],0,0) # Target (Wandering)
t11F1 = t111 # TargetF (Wandering). En este caso lo hago asi ya que no tengo un target que yo controle manualmente
t112 = Kinematic([250,200],[0,0],0,0) # Target (Wandering)
t11F2 = t112 # TargetF (Wandering). En este caso lo hago asi ya que no tengo un target que yo controle manualmente
t113 = Kinematic([250,300],[0,0],0,0) # Target (Wandering)
t11F3 = t113 # TargetF (Wandering). En este caso lo hago asi ya que no tengo un target que yo controle manualmente
t114 = Kinematic([250,400],[0,0],0,0) # Target (Wandering)
t11F4 = t114 # TargetF (Wandering). En este caso lo hago asi ya que no tengo un target que yo controle manualmente
t115 = Kinematic([250,500],[0,0],0,0) # Target (Wandering)
t11F5 = t115 # TargetF (Wandering). En este caso lo hago asi ya que no tengo un target que yo controle manualmente

k111 = Wander(o111,t111,0.05,0.1,0.01,0.5,1,t11F1,0,50,3,90,0.1)
k112 = Wander(o112,t112,0.05,0.1,0.01,0.5,1,t11F2,0,50,3,90,0.1)
k113 = Wander(o113,t113,0.05,0.1,0.01,0.5,1,t11F3,0,50,3,90,0.1)
k114 = Wander(o114,t114,0.05,0.1,0.01,0.5,1,t11F4,0,50,3,90,0.1)
k115 = Wander(o115,t115,0.05,0.1,0.01,0.5,1,t11F5,0,50,3,90,0.1)

base = 20
altura = 30
arrow = [
    pygame.Vector2(0, -altura),  # Vértice superior
    pygame.Vector2(-base / 2, 0),  # Vértice inferior izquierdo
    pygame.Vector2(base / 2, 0)  # Vértice inferior derecho
]

pygame.init()
ventana = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Wander")

tamaño = 50
fuente = pygame.font.Font(None, 20)
WanderText = fuente.render('Wander', True, (0, 0, 0))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))

    wandering1 = k111.getSteeringW() # Me da un SteeringOutput. Realiza Wander del personaje al target
    wandering2 = k112.getSteeringW() # Me da un SteeringOutput. Realiza Wander del personaje al target
    wandering3 = k113.getSteeringW() # Me da un SteeringOutput. Realiza Wander del personaje al target
    wandering4 = k114.getSteeringW() # Me da un SteeringOutput. Realiza Wander del personaje al target
    wandering5 = k115.getSteeringW() # Me da un SteeringOutput. Realiza Wander del personaje al target

    velocity = 7

    o111.update(wandering1,0.4,1)
    o112.update(wandering2,0.4,1)
    o113.update(wandering3,0.4,1)
    o114.update(wandering4,0.4,1)
    o115.update(wandering5,0.4,1)

    rotated_arrow111 = rotate_polygon(arrow, k111.character.orientation + 90) # Wander '''
    rotated_arrow112 = rotate_polygon(arrow, k112.character.orientation + 90) # Wander '''
    rotated_arrow113 = rotate_polygon(arrow, k113.character.orientation + 90) # Wander '''
    rotated_arrow114 = rotate_polygon(arrow, k114.character.orientation + 90) # Wander '''
    rotated_arrow115 = rotate_polygon(arrow, k115.character.orientation + 90) # Wander '''

    arrow_points111 = [([k111.character.position[0],k111.character.position[1]] + point) for point in rotated_arrow111] # Wander'''
    arrow_points112 = [([k112.character.position[0],k112.character.position[1]] + point) for point in rotated_arrow112] # Wander'''
    arrow_points113 = [([k113.character.position[0],k113.character.position[1]] + point) for point in rotated_arrow113] # Wander'''
    arrow_points114 = [([k114.character.position[0],k114.character.position[1]] + point) for point in rotated_arrow114] # Wander'''
    arrow_points115 = [([k115.character.position[0],k115.character.position[1]] + point) for point in rotated_arrow115] # Wander'''

    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points111) # Wander '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points112) # Wander '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points113) # Wander '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points114) # Wander '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points115) # Wander '''

    ventana.blit(WanderText, (o111.position[0]-30, o111.position[1]-27))
    ventana.blit(WanderText, (o112.position[0]-30, o112.position[1]-27))
    ventana.blit(WanderText, (o113.position[0]-30, o113.position[1]-27))
    ventana.blit(WanderText, (o114.position[0]-30, o114.position[1]-27))
    ventana.blit(WanderText, (o115.position[0]-30, o115.position[1]-27))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()