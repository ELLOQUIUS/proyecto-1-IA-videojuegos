# Ejecutar archivo con "python -m Corridas.MovKinematicWander.py" en caso de no usar
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# y colocar es punto punto, es decir: from ..Clases.KinematicWander import KinematicWander
# Taambien colocar el archivo "__init__.py" en cada carpeta

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from Clases.KinematicWander import KinematicWander
from Clases.Static import Static
from Clases.SteeringOutput import SteeringOutput
from Clases.Kinematic import Kinematic
from Clases.funciones import movimiento_teclado,rotate_polygon

o3 = Static([50,400],0) # Personaje (wandering)
st3 = SteeringOutput([0,0],0) # Aceleracion relacionada al personaje (wandering)
k3 = KinematicWander(o3,0.4,1) # Wandering del personaje (wandering)
mov_o3 = Kinematic(o3.position,[0,0],0,0) # Movimiento relacionado al personaje

base = 20
altura = 30
arrow = [
    pygame.Vector2(0, -altura),  # Vértice superior
    pygame.Vector2(-base / 2, 0),  # Vértice inferior izquierdo
    pygame.Vector2(base / 2, 0)  # Vértice inferior derecho
]

pygame.init()
ventana = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Kinematic Wandering")

tamaño = 50
fuente = pygame.font.Font(None, 20)
KinematicWanderText = fuente.render('KinematicWander', True, (0, 0, 0))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))

    ki_wandering = k3.getSteering() # Me da un KinematicSteeringOutput. Realiza la busqueda (KinematicWander) del personaje al target

    velocity = 7

    mov_o3.velocity = ki_wandering.velocity
    mov_o3.rotation = ki_wandering.rotation
    mov_o3.update(st3,k3.maxSpeed,2)
    # No se porque esta vez no asigna automaticamente la orientacion a o3 y k3 el 
    # mov_o3 mientras que en los dos casos anteriores si
    k3.character.orientation = mov_o3.orientation # Esto tambien modifica la orientacion de o3

    rotated_arrow3 = rotate_polygon(arrow, k3.character.orientation + 90) # KinematicWander '''

    arrow_points3 = [([k3.character.position[0],k3.character.position[1]] + point) for point in rotated_arrow3] # KinematicWander'''

    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points3) # KinematicWander '''

    ventana.blit(KinematicWanderText, (o3.position[0]-30, o3.position[1]-27))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()