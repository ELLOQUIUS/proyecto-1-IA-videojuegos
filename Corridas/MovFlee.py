# Ejecutar archivo con "python -m Corridas.MovFlee.py" en caso de no usar
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# y colocar es punto punto, es decir: from ..Clases.Flee import Flee
# Taambien colocar el archivo "__init__.py" en cada carpeta

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from Clases.Flee import Flee
from Clases.SteeringOutput import SteeringOutput
from Clases.Kinematic import Kinematic
from Clases.funciones import movimiento_teclado,rotate_polygon
import numpy as np

o4 = Kinematic([850,400],[0,0],0,0) # Personaje (Flee) 
t4 = Kinematic([950,400],[0,0],0,0) # Target (Flee)
k4 = Flee(o4,t4,0.3) # Busqueda del personaje al target (Flee)

base = 20
altura = 30
arrow = [
    pygame.Vector2(0, -altura),  # Vértice superior
    pygame.Vector2(-base / 2, 0),  # Vértice inferior izquierdo
    pygame.Vector2(base / 2, 0)  # Vértice inferior derecho
]

pygame.init()
ventana = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Dynamic Flee")

tamaño = 50
fuente = pygame.font.Font(None, 20)
FleeText = fuente.render('Flee', True, (0, 0, 0))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))

    Flee = k4.getSteering() # Me da un SteeringOutput. Realiza la huida (Flee) del personaje al target

    velocity = 7

    # Para que no se mueva infinitamente
    direccion = [0,0]
    direccion[0] = o4.position[0] - t4.position[0]
    direccion[1] = o4.position[1] - t4.position[1]

    vector_direccion = np.array(direccion)
    distancia = np.linalg.norm(vector_direccion)

    if distancia < 300:
        o4.update(Flee,1.8,2)

    keys = pygame.key.get_pressed() # Para agarrar las teclas del teclado y mover el objetivo
    movimiento_teclado(keys,t4,velocity,False)

    rotated_arrow4 = rotate_polygon(arrow, k4.character.orientation + 90) # Flee '''

    arrow_points4 = [([k4.character.position[0],k4.character.position[1]] + point) for point in rotated_arrow4] # Flee'''

    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points4) # Flee '''

    pygame.draw.rect(ventana, (255, 100, 10), (t4.position[0]-20, t4.position[1]-20, 40, 40)) # Flee '''

    ventana.blit(FleeText, (o4.position[0]-30, o4.position[1]-27))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()