# Ejecutar archivo con "python -m Corridas.MovPurEvaLWsinPersonaje.py" en caso de no usar
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# y colocar es punto punto, es decir: from ..Clases.Pursue import PursueLW
# Taambien colocar el archivo "__init__.py" en cada carpeta

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from Clases.Pursue import Pursue
from Clases.Evade import Evade
from Clases.LookWhereYoureGoing import LookWhereYoureGoing
from Clases.SteeringOutput import SteeringOutput
from Clases.Kinematic import Kinematic
from Clases.funciones import movimiento_teclado_cambio_velocity,rotate_polygon
import numpy as np
import math

radioINT = 50
radioEXT = 250
o10 = Kinematic([400,400],[0,0],0,0) # Personaje1 (LookWhereAreYouGoing) 
o11 = Kinematic([800,200],[0,0],0,0) # Personaje2 (LookWhereAreYouGoing)

o10fant = Kinematic([800,200],[0,0],0,0) # Target (LookWhereAreYouGoing)
o11fant = Kinematic([400,400],[0,0],0,0) # Target (LookWhereAreYouGoing)

k100 = LookWhereYoureGoing(o10,o11,1,5,0.01,0.9,0.1)
k101 = Pursue(o10,o11fant,0.4,7,radioINT-20,radioEXT,0.1,2.5,o11) # Para hacer la combinacion con pursue
k102 = LookWhereYoureGoing(o11,o10,1,5,0.01,0.9,0.1)
k103 = Evade(o11,o10fant,0.4,1.1,o10) # Para hacer la combinacion con evade

base = 20
altura = 30
arrow = [
    pygame.Vector2(0, -altura),  # Vértice superior
    pygame.Vector2(-base / 2, 0),  # Vértice inferior izquierdo
    pygame.Vector2(base / 2, 0)  # Vértice inferior derecho
]

pygame.init()
ventana = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("PursueEvadeLW")

tamaño = 50
fuente = pygame.font.Font(None, 20)
PursueLWText = fuente.render('PursueLW', True, (0, 0, 0))
EvadeLWText = fuente.render('EvadeLW', True, (0, 0, 0))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))

    lwayg = k100.getSteeringLWYG()
    pursueParaLWYG = k101.getSteeringP()
    lwayg_pursue = SteeringOutput(pursueParaLWYG.linear,lwayg.angular)

    lwayg2 = k102.getSteeringLWYG()
    evadeParaLWYG = k103.getSteeringE()
    lwayg_evade = SteeringOutput(evadeParaLWYG.linear,lwayg2.angular)

    o10.update(lwayg_pursue,6.5,1)
    o11.update(lwayg_evade,2,1)

    rotated_arrow10 = rotate_polygon(arrow, k100.character.orientation + 180) # LookWhereAreYouGoing '''
    rotated_arrow11 = rotate_polygon(arrow, k102.character.orientation + 180) # LookWhereAreYouGoing '''

    arrow_points10 = [([k100.character.position[0],k100.character.position[1]] + point) for point in rotated_arrow10] # LookWhereAreYouGoing'''
    arrow_points11 = [([k102.character.position[0],k102.character.position[1]] + point) for point in rotated_arrow11] # LookWhereAreYouGoing'''

    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points10) # PursueLW '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points11) # EvadeLW '''

    ventana.blit(PursueLWText, (o10.position[0]-20, o10.position[1]-27))
    ventana.blit(EvadeLWText, (o11.position[0]-20, o11.position[1]-27))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()