# Ejecutar archivo con "python -m Corridas.MovVelocityMatch.py" en caso de no usar
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# y colocar es punto punto, es decir: from ..Clases.VelocityMatch import VelocityMatch
# Taambien colocar el archivo "__init__.py" en cada carpeta

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from Clases.VelocityMatch import VelocityMatch
from Clases.SteeringOutput import SteeringOutput
from Clases.Kinematic import Kinematic
from Clases.funciones import movimiento_teclado_cambio_velocity,rotate_polygon
import numpy as np
import math

o7 = Kinematic([500,400],[0,0],0,0) # Personaje (Velocity Match) 
t7 = Kinematic([650,400],[0,0],0,0) # Target (Velocity Match)
k7 = VelocityMatch(o7,t7,0.5,1) # Alineacion de velocidad del personaje al target (Velocity Match)

base = 20
altura = 30
arrow = [
    pygame.Vector2(0, -altura),  # Vértice superior
    pygame.Vector2(-base / 2, 0),  # Vértice inferior izquierdo
    pygame.Vector2(base / 2, 0)  # Vértice inferior derecho
]

pygame.init()
ventana = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("VelocityMatch")

tamaño = 50
fuente = pygame.font.Font(None, 20)
VelocityMatchText = fuente.render('VelocityMatch', True, (0, 0, 0))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))

    velocityMatch = k7.getSteering() # Me da un SteeringOutput. Realiza VelocityMatch del personaje al target

    velocity = 7

    o7.update(velocityMatch,math.sqrt(velocity*velocity + velocity*velocity),1)

    keys = pygame.key.get_pressed() # Para agarrar las teclas del teclado y mover el objetivo
    movimiento_teclado_cambio_velocity(keys,t7,velocity,False)

    t7.position[0] += t7.velocity[0]
    t7.position[1] += t7.velocity[1]


    rotated_arrow7 = rotate_polygon(arrow, k7.character.orientation + 90) # VelocityMatch '''

    arrow_points7 = [([k7.character.position[0],k7.character.position[1]] + point) for point in rotated_arrow7] # VelocityMatch'''

    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points7) # VelocityMatch '''

    pygame.draw.rect(ventana, (255, 100, 10), (t7.position[0]-20, t7.position[1]-20, 40, 40)) # VelocityMatch '''

    ventana.blit(VelocityMatchText, (o7.position[0]-30, o7.position[1]-27))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()