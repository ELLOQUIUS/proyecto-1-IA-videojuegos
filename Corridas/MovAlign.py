# Ejecutar archivo con "python -m Corridas.MovAlign.py" en caso de no usar
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# y colocar es punto punto, es decir: from ..Clases.Align import Align
# Taambien colocar el archivo "__init__.py" en cada carpeta

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from Clases.Align import Align
from Clases.SteeringOutput import SteeringOutput
from Clases.Kinematic import Kinematic
from Clases.funciones import movimiento_teclado,rotate_polygon
import numpy as np

o6 = Kinematic([500,400],[0,0],0,0) # Personaje (Align) 
t6 = Kinematic([560,400],[0,0],0,0) # Target (Align)
k6 = Align(o6,t6,0.8,3,0.01,0.9,1) # Alineacion del personaje al target (Align)

base = 20
altura = 30
arrow = [
    pygame.Vector2(0, -altura),  # Vértice superior
    pygame.Vector2(-base / 2, 0),  # Vértice inferior izquierdo
    pygame.Vector2(base / 2, 0)  # Vértice inferior derecho
]

pygame.init()
ventana = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Align")

tamaño = 50
fuente = pygame.font.Font(None, 20)
AlignText = fuente.render('Align', True, (0, 0, 0))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))

    align = k6.getSteering() # Me da un SteeringOutput. Realiza la alineacion del personaje al objetivo

    velocity = 7

    o6.update(align,0,2)

    keys = pygame.key.get_pressed() # Para agarrar las teclas del teclado y mover el objetivo
    movimiento_teclado(keys,t6,0,True) # Pongo velocity 0 para que el objetivo no se mueva

    rotated_arrow6 = rotate_polygon(arrow, k6.character.orientation + 90) # Align '''
    rotated_target6 = rotate_polygon(arrow, k6.target.orientation + 90) # Align '''

    arrow_points6 = [([k6.character.position[0],k6.character.position[1]] + point) for point in rotated_arrow6] # Align'''
    target_point6 = [([k6.target.position[0],k6.target.position[1]] + point) for point in rotated_target6] # Align'''

    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points6) # Align '''

    pygame.draw.polygon(ventana, (0, 0, 255), target_point6) # Align ''''

    ventana.blit(AlignText, (o6.position[0]-20, o6.position[1]-45))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()