# Ejecutar archivo con "python -m Corridas.MovSeek.py" en caso de no usar
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# y colocar es punto punto, es decir: from ..Clases.Seek import Seek
# Taambien colocar el archivo "__init__.py" en cada carpeta

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from Clases.Seek import Seek
from Clases.SteeringOutput import SteeringOutput
from Clases.Kinematic import Kinematic
from Clases.funciones import movimiento_teclado,rotate_polygon

o4 = Kinematic([50,400],[0,0],0,0) # Personaje (Seek) 
t4 = Kinematic([950,400],[0,0],0,0) # Target (Seek)
k4 = Seek(o4,t4,0.3) # Busqueda del personaje al target (Seek)

base = 20
altura = 30
arrow = [
    pygame.Vector2(0, -altura),  # Vértice superior
    pygame.Vector2(-base / 2, 0),  # Vértice inferior izquierdo
    pygame.Vector2(base / 2, 0)  # Vértice inferior derecho
]

pygame.init()
ventana = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Dynamic Seek")

tamaño = 50
fuente = pygame.font.Font(None, 20)
SeekText = fuente.render('Seek', True, (0, 0, 0))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))

    seek = k4.getSteering() # Me da un SteeringOutput. Realiza la busqueda (Seek) del personaje al target

    velocity = 7

    o4.update(seek,3,2)

    keys = pygame.key.get_pressed() # Para agarrar las teclas del teclado y mover el objetivo
    movimiento_teclado(keys,t4,velocity,False)

    rotated_arrow4 = rotate_polygon(arrow, k4.character.orientation + 90) # Seek '''

    arrow_points4 = [([k4.character.position[0],k4.character.position[1]] + point) for point in rotated_arrow4] # Seek'''

    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points4) # Seek '''

    pygame.draw.rect(ventana, (255, 100, 10), (t4.position[0]-20, t4.position[1]-20, 40, 40)) # Seek '''

    ventana.blit(SeekText, (o4.position[0]-30, o4.position[1]-27))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()