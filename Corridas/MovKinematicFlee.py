# Ejecutar archivo con "python -m Corridas.MovKinematicFlee.py" en caso de no usar
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# y colocar es punto punto, es decir: from ..Clases.KinematicFlee import KinematicFlee
# Taambien colocar el archivo "__init__.py" en cada carpeta

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from Clases.KinematicFlee import KinematicFlee
from Clases.Static import Static
from Clases.SteeringOutput import SteeringOutput
from Clases.Kinematic import Kinematic
from Clases.funciones import movimiento_teclado,rotate_polygon
import numpy as np

o1 = Static([850,400],0) # Personaje (KinematicFlee)
t1 = Static([950,400],0) # Target  (KinematicFlee)
st1 = SteeringOutput([0,0],0) # Aceleracion relacionada al personaje (KinematicFlee)
k1 = KinematicFlee(o1,t1,1) # Huida del personaje al target  (KinematicFlee)
mov_o1 = Kinematic(o1.position,[0,0],0,0) # Movimiento relacionado al personaje

base = 20
altura = 30
arrow = [
    pygame.Vector2(0, -altura),  # Vértice superior
    pygame.Vector2(-base / 2, 0),  # Vértice inferior izquierdo
    pygame.Vector2(base / 2, 0)  # Vértice inferior derecho
]

pygame.init()
ventana = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Kinematic Flee")

tamaño = 50
fuente = pygame.font.Font(None, 20)
KinematicFleeText = fuente.render('KinematicFlee', True, (0, 0, 0))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))

    kinematicFlee = k1.getSteering() # Me da un KinematicSteeringOutput. Realiza la busqueda (KinematicArrive) del personaje al target

    velocity = 7

    mov_o1.velocity = kinematicFlee.velocity
    mov_o1.rotation = kinematicFlee.rotation

    # Para que no se mueva infinitamente
    direccion = [0,0]
    direccion[0] = o1.position[0] - t1.position[0]
    direccion[1] = o1.position[1] - t1.position[1]

    vector_direccion = np.array(direccion)
    distancia = np.linalg.norm(vector_direccion)

    if distancia < 300:
        mov_o1.update(st1,2,2)

    keys = pygame.key.get_pressed() # Para agarrar las teclas del teclado y mover el objetivo
    movimiento_teclado(keys,t1,velocity,False)

    rotated_arrow1 = rotate_polygon(arrow, k1.character.orientation + 90) # KinematicFlee '''

    arrow_points1 = [([k1.character.position[0],k1.character.position[1]] + point) for point in rotated_arrow1] # KinematicFlee'''

    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points1) # KinematicFlee '''

    pygame.draw.rect(ventana, (255, 100, 10), (t1.position[0]-20, t1.position[1]-20, 40, 40)) # KinematicFlee '''

    ventana.blit(KinematicFleeText, (o1.position[0]-30, o1.position[1]-27))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()