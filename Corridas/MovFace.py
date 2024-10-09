# Ejecutar archivo con "python -m Corridas.MovFace.py" en caso de no usar
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# y colocar es punto punto, es decir: from ..Clases.Face import Face
# Taambien colocar el archivo "__init__.py" en cada carpeta

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from Clases.Face import Face
from Clases.SteeringOutput import SteeringOutput
from Clases.Kinematic import Kinematic
from Clases.funciones import movimiento_teclado_cambio_velocity,rotate_polygon
import numpy as np
import math

o91 = Kinematic([550,250],[0,0],0,0) # Personaje (Face)
o92 = Kinematic([450,320],[0,0],0,0) # Personaje (Face)
o93 = Kinematic([650,320],[0,0],0,0) # Personaje (Face)
o94 = Kinematic([480,430],[0,0],0,0) # Personaje (Face)
o95 = Kinematic([620,430],[0,0],0,0) # Personaje (Face)

t9 = Kinematic([550,350],[0,0],0,0) # Target (Face)
t9F = Kinematic([550,350],[0,0],0,0) # TargetF (Face)

k91 = Face(o91,t9,0.8,3,0.01,0.9,2,t9F)
k92 = Face(o92,t9,0.8,3,0.01,0.9,2,t9F)
k93 = Face(o93,t9,0.8,3,0.01,0.9,2,t9F)
k94 = Face(o94,t9,0.8,3,0.01,0.9,2,t9F)
k95 = Face(o95,t9,0.8,3,0.01,0.9,2,t9F)

base = 20
altura = 30
arrow = [
    pygame.Vector2(0, -altura),  # Vértice superior
    pygame.Vector2(-base / 2, 0),  # Vértice inferior izquierdo
    pygame.Vector2(base / 2, 0)  # Vértice inferior derecho
]

pygame.init()
ventana = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Face")

tamaño = 50
fuente = pygame.font.Font(None, 20)
FaceText = fuente.render('Face', True, (0, 0, 0))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))

    face1 = k91.getSteeringF()
    face2 = k92.getSteeringF() 
    face3 = k93.getSteeringF() 
    face4 = k94.getSteeringF()
    face5 = k95.getSteeringF()

    velocity = 7

    o91.update(face1,0,2)
    o92.update(face2,0,2)
    o93.update(face3,0,2)
    o94.update(face4,0,2)
    o95.update(face5,0,2)

    keys = pygame.key.get_pressed() # Para agarrar las teclas del teclado y mover el objetivo
    movimiento_teclado_cambio_velocity(keys,t9,velocity,True) 
    movimiento_teclado_cambio_velocity(keys,t9F,velocity,True)

    t9.position[0] += t9.velocity[0]
    t9.position[1] += t9.velocity[1]
    t9F.position[0] += t9F.velocity[0]
    t9F.position[1] += t9F.velocity[1]


    rotated_arrow91 = rotate_polygon(arrow, k91.character.orientation + 180) # Face '''
    rotated_arrow92 = rotate_polygon(arrow, k92.character.orientation + 180) # Face '''
    rotated_arrow93 = rotate_polygon(arrow, k93.character.orientation + 180) # Face '''
    rotated_arrow94 = rotate_polygon(arrow, k94.character.orientation + 180) # Face '''
    rotated_arrow95 = rotate_polygon(arrow, k95.character.orientation + 180) # Face '''

    arrow_points91 = [([k91.character.position[0],k91.character.position[1]] + point) for point in rotated_arrow91] # Face'''
    arrow_points92 = [([k92.character.position[0],k92.character.position[1]] + point) for point in rotated_arrow92] # Face'''
    arrow_points93 = [([k93.character.position[0],k93.character.position[1]] + point) for point in rotated_arrow93] # Face'''
    arrow_points94 = [([k94.character.position[0],k94.character.position[1]] + point) for point in rotated_arrow94] # Face'''
    arrow_points95 = [([k95.character.position[0],k95.character.position[1]] + point) for point in rotated_arrow95] # Face'''

    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points91) # Face '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points92) # Face '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points93) # Face '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points94) # Face '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points95) # Face '''

    pygame.draw.rect(ventana, (255, 100, 10), (t9.position[0]-20, t9.position[1]-20, 40, 40)) # Face '''

    ventana.blit(FaceText, (o91.position[0]-30, o91.position[1]-27))
    ventana.blit(FaceText, (o92.position[0]-30, o92.position[1]-27))
    ventana.blit(FaceText, (o93.position[0]-30, o93.position[1]-27))
    ventana.blit(FaceText, (o94.position[0]-30, o94.position[1]-27))
    ventana.blit(FaceText, (o95.position[0]-30, o94.position[1]-27))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()