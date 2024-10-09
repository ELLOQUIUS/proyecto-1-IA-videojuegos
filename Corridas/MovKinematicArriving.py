# Ejecutar archivo con "python -m Corridas.MovKinematicArriving.py" en caso de no usar
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# y colocar es punto punto, es decir: from ..Clases.KinematicArrive import KinematicArrive
# Taambien colocar el archivo "__init__.py" en cada carpeta

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from Clases.KinematicArrive import KinematicArrive
from Clases.Static import Static
from Clases.SteeringOutput import SteeringOutput
from Clases.Kinematic import Kinematic
from Clases.funciones import movimiento_teclado,rotate_polygon

radioINT = 50
o2 = Static([50,400],0) # Personaje (KinematicArrive)
t2 = Static([950,400],0) # Target (KinematicArrive)
st2 = SteeringOutput([0,0],0) # Aceleracion relacionada al personaje (KinematicArrive)
k2 = KinematicArrive(o2,t2,3,radioINT,100.25) # Busqueda del personaje al target (KinematicArrive)
mov_o2 = Kinematic(o2.position,[0,0],0,0) # Movimiento relacionado al personaje

base = 20
altura = 30
arrow = [
    pygame.Vector2(0, -altura),  # Vértice superior
    pygame.Vector2(-base / 2, 0),  # Vértice inferior izquierdo
    pygame.Vector2(base / 2, 0)  # Vértice inferior derecho
]

pygame.init()
ventana = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Kinematic Arriving")

tamaño = 50
fuente = pygame.font.Font(None, 20)
KinematicArriveText = fuente.render('KinematicArrive', True, (0, 0, 0))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))

    kinematicArrive = k2.getSteering() # Me da un KinematicSteeringOutput. Realiza la busqueda (KinematicArrive) del personaje al target

    velocity = 7

    mov_o2.velocity = kinematicArrive.velocity
    mov_o2.rotation = kinematicArrive.rotation
    mov_o2.update(st2,2,2)

    keys = pygame.key.get_pressed() # Para agarrar las teclas del teclado y mover el objetivo
    movimiento_teclado(keys,t2,velocity,False)

    rotated_arrow2 = rotate_polygon(arrow, k2.character.orientation + 90) # KinematicArrive '''

    arrow_points2 = [([k2.character.position[0],k2.character.position[1]] + point) for point in rotated_arrow2] # KinematicArrive'''

    pygame.draw.circle(ventana, (0,0,0), (t2.position[0], t2.position[1]), radioINT)
    pygame.draw.circle(ventana, (255,255,255), (t2.position[0], t2.position[1]), radioINT-1)

    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points2) # KinematicArrive '''

    pygame.draw.rect(ventana, (255, 100, 10), (t2.position[0]-20, t2.position[1]-20, 40, 40)) # KinematicArrive '''

    ventana.blit(KinematicArriveText, (o2.position[0]-30, o2.position[1]-27))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()