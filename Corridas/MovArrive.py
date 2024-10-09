# Ejecutar archivo con "python -m Corridas.MovArrive.py" en caso de no usar
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# y colocar es punto punto, es decir: from ..Clases.Arrive import Arrive
# Taambien colocar el archivo "__init__.py" en cada carpeta

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from Clases.Arrive import Arrive
from Clases.SteeringOutput import SteeringOutput
from Clases.Kinematic import Kinematic
from Clases.funciones import movimiento_teclado,rotate_polygon
import numpy as np

radioINT = 50
o5 = Kinematic([50,400],[0,0],0,0) # Personaje (Arrive) 
t5 = Kinematic([950,400],[0,0],0,0) # Target (Arrive)
radioEXT = 270
k5 = Arrive(o5,t5,0.8,5,radioINT-25,radioEXT,1)

base = 20
altura = 30
arrow = [
    pygame.Vector2(0, -altura),  # Vértice superior
    pygame.Vector2(-base / 2, 0),  # Vértice inferior izquierdo
    pygame.Vector2(base / 2, 0)  # Vértice inferior derecho
]

pygame.init()
ventana = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Dynamic Arrive")

tamaño = 50
fuente = pygame.font.Font(None, 20)
ArriveText = fuente.render('Arrive', True, (0, 0, 0))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))

    arrive = k5.getSteering() # Me da un SteeringOutput. Realiza la busqueda (Arrive) del personaje al target

    velocity = 7

    direccion = [0,0]
    direccion[0] = o5.position[0] - t5.position[0]
    direccion[1] = o5.position[1] - t5.position[1]

    vector_direccion = np.array(direccion)
    distancia = np.linalg.norm(vector_direccion)

    if distancia >= 25:
        o5.update(arrive,k5.maxSpeed,1)

    keys = pygame.key.get_pressed() # Para agarrar las teclas del teclado y mover el objetivo
    movimiento_teclado(keys,t5,velocity,False)

    rotated_arrow4 = rotate_polygon(arrow, k5.character.orientation + 90) # Arrive '''

    arrow_points4 = [([k5.character.position[0],k5.character.position[1]] + point) for point in rotated_arrow4] # Arrive'''

    pygame.draw.circle(ventana, (0,0,0), (t5.position[0], t5.position[1]), radioEXT)
    pygame.draw.circle(ventana, (255,255,255), (t5.position[0], t5.position[1]), radioEXT-1)
    pygame.draw.circle(ventana, (0,0,0), (t5.position[0], t5.position[1]), radioINT-25)
    pygame.draw.circle(ventana, (255,255,255), (t5.position[0], t5.position[1]), radioINT-25-1)

    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points4) # Arrive '''

    pygame.draw.rect(ventana, (255, 100, 10), (t5.position[0]-20, t5.position[1]-20, 40, 40)) # Arrive '''

    ventana.blit(ArriveText, (o5.position[0]-30, o5.position[1]-27))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()