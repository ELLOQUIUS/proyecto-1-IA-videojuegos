# Ejecutar archivo con "python -m Corridas.MovSeparation.py" en caso de no usar
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# y colocar es punto punto, es decir: from ..Clases.Separation import Separation
# Taambien colocar el archivo "__init__.py" en cada carpeta

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from Clases.Separation import Separation
from Clases.VelocityMatch import VelocityMatch
from Clases.SteeringOutput import SteeringOutput
from Clases.Kinematic import Kinematic
from Clases.funciones import movimiento_teclado_cambio_velocity,rotate_polygon
from Clases.funciones import desacelerar
import numpy as np
import math

o121 = Kinematic([500,401],[0,0],0,0) # Personaje
o122 = Kinematic([500,404],[0,0],0,0) # Personaje
o123 = Kinematic([506,401],[0,0],0,0) # Personaje
o124 = Kinematic([501,400],[0,0],0,0) # Personaje
o125 = Kinematic([512,400],[0,0],0,0) # Personaje
o126 = Kinematic([511,396],[0,0],0,0) # Personaje
o127 = Kinematic([516,390],[0,0],0,0) # Personaje
o128 = Kinematic([496,400],[0,0],0,0) # Personaje
o129 = Kinematic([478,410],[0,0],0,0) # Personaje
o1210 = Kinematic([501,409],[0,0],0,0) # Personaje

t12 = Kinematic([650,400],[0,0],0,0) # Target 

k121V = VelocityMatch(o121,t12,0.2,1) 
k122V = VelocityMatch(o122,t12,0.4,1) 
k123V = VelocityMatch(o123,t12,0.45,1)
k124V = VelocityMatch(o124,t12,0.3,1)
k125V = VelocityMatch(o125,t12,0.19,1)
k126V = VelocityMatch(o126,t12,0.49,1)
k127V = VelocityMatch(o127,t12,0.19,1)
k128V = VelocityMatch(o128,t12,0.22,1)
k129V = VelocityMatch(o129,t12,0.37,1)
k1210V = VelocityMatch(o1210,t12,0.44,1)

k121S = Separation(o121,0.08,[o122,o123,o124,o125,o126,o127,o128,o129,o1210,t12],75,100) 
k122S = Separation(o122,0.044,[o121,o123,o124,o125,o126,o127,o128,o129,o1210,t12],75,100) 
k123S = Separation(o123,0.03,[o121,o122,o124,o125,o126,o127,o128,o129,o1210,t12],75,100) 
k124S = Separation(o124,0.03,[o121,o122,o123,o125,o126,o127,o128,o129,o1210,t12],75,100) 
k125S = Separation(o125,0.08,[o121,o122,o123,o124,o126,o127,o128,o129,o1210,t12],75,100) 
k126S = Separation(o126,0.05,[o121,o122,o123,o124,o125,o127,o128,o129,o1210,t12],75,100) 
k127S = Separation(o127,0.06,[o121,o122,o123,o124,o125,o126,o128,o129,o1210,t12],75,100) 
k128S = Separation(o128,0.077,[o121,o122,o123,o124,o125,o126,o127,o129,o1210,t12],75,100) 
k129S = Separation(o129,0.052,[o121,o122,o123,o124,o125,o126,o127,o128,o1210,t12],75,100) 
k1210S = Separation(o1210,0.034,[o121,o122,o123,o124,o125,o126,o127,o128,o129,t12],75,100) 

base = 20
altura = 30
arrow = [
    pygame.Vector2(0, -altura),  # Vértice superior
    pygame.Vector2(-base / 2, 0),  # Vértice inferior izquierdo
    pygame.Vector2(base / 2, 0)  # Vértice inferior derecho
]

pygame.init()
ventana = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Separation with Velocity Matching")

fuente = pygame.font.Font(None, 20)
SeparationText = fuente.render('', True, (0, 0, 0))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))

    velocitymatch1 = k121V.getSteering()
    velocitymatch2 = k122V.getSteering()
    velocitymatch3 = k123V.getSteering()
    velocitymatch4 = k124V.getSteering()
    velocitymatch5 = k125V.getSteering()
    velocitymatch6 = k126V.getSteering()
    velocitymatch7 = k127V.getSteering()
    velocitymatch8 = k128V.getSteering()
    velocitymatch9 = k129V.getSteering()
    velocitymatch10 = k1210V.getSteering()
    
    separation1 = k121S.getSteering()
    separation2 = k122S.getSteering()
    separation3 = k123S.getSteering()
    separation4 = k124S.getSteering()
    separation5 = k125S.getSteering()
    separation6 = k126S.getSteering()
    separation7 = k127S.getSteering()
    separation8 = k128S.getSteering()
    separation9 = k129S.getSteering()
    separation10 = k1210S.getSteering()

    vel_sep1 = SteeringOutput([0,0],0)
    vel_sep2 = SteeringOutput([0,0],0)
    vel_sep3 = SteeringOutput([0,0],0)
    vel_sep4 = SteeringOutput([0,0],0)
    vel_sep5 = SteeringOutput([0,0],0)
    vel_sep6 = SteeringOutput([0,0],0)
    vel_sep7 = SteeringOutput([0,0],0)
    vel_sep8 = SteeringOutput([0,0],0)
    vel_sep9 = SteeringOutput([0,0],0)
    vel_sep10 = SteeringOutput([0,0],0)

    vel_sep1.linear[0] = velocitymatch1.linear[0] + separation1.linear[0]
    vel_sep1.linear[1] = velocitymatch1.linear[1] + separation1.linear[1]
    vel_sep1.angular = velocitymatch1.angular + separation1.angular

    vel_sep2.linear[0] = velocitymatch2.linear[0] + separation2.linear[0]
    vel_sep2.linear[1] = velocitymatch2.linear[1] + separation2.linear[1]
    vel_sep2.angular = velocitymatch2.angular + separation2.angular

    vel_sep3.linear[0] = velocitymatch3.linear[0] + separation3.linear[0]
    vel_sep3.linear[1] = velocitymatch3.linear[1] + separation3.linear[1]
    vel_sep3.angular = velocitymatch3.angular + separation3.angular

    vel_sep4.linear[0] = velocitymatch4.linear[0] + separation4.linear[0]
    vel_sep4.linear[1] = velocitymatch4.linear[1] + separation4.linear[1]
    vel_sep4.angular = velocitymatch4.angular + separation4.angular

    vel_sep5.linear[0] = velocitymatch5.linear[0] + separation5.linear[0]
    vel_sep5.linear[1] = velocitymatch5.linear[1] + separation5.linear[1]
    vel_sep5.angular = velocitymatch5.angular + separation5.angular

    vel_sep6.linear[0] = velocitymatch6.linear[0] + separation6.linear[0]
    vel_sep6.linear[1] = velocitymatch6.linear[1] + separation6.linear[1]
    vel_sep6.angular = velocitymatch6.angular + separation6.angular

    vel_sep7.linear[0] = velocitymatch7.linear[0] + separation7.linear[0]
    vel_sep7.linear[1] = velocitymatch7.linear[1] + separation7.linear[1]
    vel_sep7.angular = velocitymatch7.angular + separation7.angular

    vel_sep8.linear[0] = velocitymatch8.linear[0] + separation8.linear[0]
    vel_sep8.linear[1] = velocitymatch8.linear[1] + separation8.linear[1]
    vel_sep8.angular = velocitymatch8.angular + separation8.angular

    vel_sep9.linear[0] = velocitymatch9.linear[0] + separation9.linear[0]
    vel_sep9.linear[1] = velocitymatch9.linear[1] + separation9.linear[1]
    vel_sep9.angular = velocitymatch9.angular + separation9.angular

    vel_sep10.linear[0] = velocitymatch10.linear[0] + separation10.linear[0]
    vel_sep10.linear[1] = velocitymatch10.linear[1] + separation10.linear[1]
    vel_sep10.angular = velocitymatch10.angular + separation10.angular

    velocity = 4

    o121.update(vel_sep1,math.sqrt(velocity*velocity + velocity*velocity),1)
    o122.update(vel_sep2,math.sqrt(velocity*velocity + velocity*velocity),1)
    o123.update(vel_sep3,math.sqrt(velocity*velocity + velocity*velocity),1)
    o124.update(vel_sep4,math.sqrt(velocity*velocity + velocity*velocity),1)
    o125.update(vel_sep5,math.sqrt(velocity*velocity + velocity*velocity),1)
    o126.update(vel_sep6,math.sqrt(velocity*velocity + velocity*velocity),1)
    o127.update(vel_sep7,math.sqrt(velocity*velocity + velocity*velocity),1)
    o128.update(vel_sep8,math.sqrt(velocity*velocity + velocity*velocity),1)
    o129.update(vel_sep9,math.sqrt(velocity*velocity + velocity*velocity),1)
    o1210.update(vel_sep10,math.sqrt(velocity*velocity + velocity*velocity),1)

    '''newod121 = Kinematic([0,0],[0,0],0,0)
    newod122 = Kinematic([0,0],[0,0],0,0)
    newod123 = Kinematic([0,0],[0,0],0,0)
    newod124 = Kinematic([0,0],[0,0],0,0)
    newod125 = Kinematic([0,0],[0,0],0,0)
    newod126 = Kinematic([0,0],[0,0],0,0)
    newod127 = Kinematic([0,0],[0,0],0,0)
    newod128 = Kinematic([0,0],[0,0],0,0)
    newod129 = Kinematic([0,0],[0,0],0,0)
    newod1210 = Kinematic([0,0],[0,0],0,0)
    if vel_sep1.linear[0] == 0 and vel_sep1.linear[1] == 0:
        newod121 = desacelerar(o121,0.06)
        o121.velocity[0] = newod121.velocity[0];o121.velocity[1] = newod121.velocity[1]
    if vel_sep2.linear[0] == 0 and vel_sep2.linear[1] == 0:
        newod122 = desacelerar(o122,0.06)
        o122.velocity[0] = newod122.velocity[0];o122.velocity[1] = newod122.velocity[1]
    if vel_sep3.linear[0] == 0 and vel_sep3.linear[1] == 0:
        newod123 = desacelerar(o123,0.06)
        o123.velocity[0] = newod123.velocity[0];o123.velocity[1] = newod123.velocity[1]
    if vel_sep4.linear[0] == 0 and vel_sep4.linear[1] == 0:
        newod124 = desacelerar(o124,0.06)
        o124.velocity[0] = newod124.velocity[0];o124.velocity[1] = newod124.velocity[1]
    if vel_sep5.linear[0] == 0 and vel_sep5.linear[1] == 0:
        newod125 = desacelerar(o125,0.06)
        o125.velocity[0] = newod125.velocity[0];o125.velocity[1] = newod125.velocity[1]
    if vel_sep6.linear[0] == 0 and vel_sep6.linear[1] == 0:
        newod126 = desacelerar(o126,0.06)
        o126.velocity[0] = newod126.velocity[0];o126.velocity[1] = newod126.velocity[1]
    if vel_sep7.linear[0] == 0 and vel_sep7.linear[1] == 0:
        newod127 = desacelerar(o127,0.06)
        o127.velocity[0] = newod127.velocity[0];o127.velocity[1] = newod127.velocity[1]
    if vel_sep8.linear[0] == 0 and vel_sep8.linear[1] == 0:
        newod128 = desacelerar(o128,0.06)
        o128.velocity[0] = newod128.velocity[0];o128.velocity[1] = newod128.velocity[1]
    if vel_sep9.linear[0] == 0 and vel_sep9.linear[1] == 0:
        newod129 = desacelerar(o129,0.06)
        o129.velocity[0] = newod129.velocity[0];o129.velocity[1] = newod129.velocity[1]
    if vel_sep10.linear[0] == 0 and vel_sep10.linear[1] == 0:
        newod1210 = desacelerar(o1210,0.06)
        o1210.velocity[0] = newod1210.velocity[0];o1210.velocity[1] = newod1210.velocity[1]
'''
    keys = pygame.key.get_pressed() # Para agarrar las teclas del teclado y mover el objetivo
    movimiento_teclado_cambio_velocity(keys,t12,velocity,False)

    t12.position[0] += t12.velocity[0]
    t12.position[1] += t12.velocity[1]

    rotated_arrow121 = rotate_polygon(arrow, k121S.character.orientation + 90) # Separation '''
    rotated_arrow122 = rotate_polygon(arrow, k122S.character.orientation + 90) # Separation '''
    rotated_arrow123 = rotate_polygon(arrow, k123S.character.orientation + 90) # Separation '''
    rotated_arrow124 = rotate_polygon(arrow, k124S.character.orientation + 90) # Separation '''
    rotated_arrow125 = rotate_polygon(arrow, k125S.character.orientation + 90) # Separation '''
    rotated_arrow126 = rotate_polygon(arrow, k126S.character.orientation + 90) # Separation '''
    rotated_arrow127 = rotate_polygon(arrow, k127S.character.orientation + 90) # Separation '''
    rotated_arrow128 = rotate_polygon(arrow, k128S.character.orientation + 90) # Separation '''
    rotated_arrow129 = rotate_polygon(arrow, k129S.character.orientation + 90) # Separation '''
    rotated_arrow1210 = rotate_polygon(arrow, k1210S.character.orientation + 90) # Separation '''

    arrow_points121 = [([k121V.character.position[0],k121V.character.position[1]] + point) for point in rotated_arrow121] # Separation'''
    arrow_points122 = [([k122V.character.position[0],k122V.character.position[1]] + point) for point in rotated_arrow122] # Separation'''
    arrow_points123 = [([k123V.character.position[0],k123V.character.position[1]] + point) for point in rotated_arrow123] # Separation'''
    arrow_points124 = [([k124V.character.position[0],k124V.character.position[1]] + point) for point in rotated_arrow124] # Separation'''
    arrow_points125 = [([k125V.character.position[0],k125V.character.position[1]] + point) for point in rotated_arrow125] # Separation'''
    arrow_points126 = [([k126V.character.position[0],k126V.character.position[1]] + point) for point in rotated_arrow126] # Separation'''
    arrow_points127 = [([k127V.character.position[0],k127V.character.position[1]] + point) for point in rotated_arrow127] # Separation'''
    arrow_points128 = [([k128V.character.position[0],k128V.character.position[1]] + point) for point in rotated_arrow128] # Separation'''
    arrow_points129 = [([k129V.character.position[0],k129V.character.position[1]] + point) for point in rotated_arrow129] # Separation'''
    arrow_points1210 = [([k1210V.character.position[0],k1210V.character.position[1]] + point) for point in rotated_arrow1210] # Separation'''

    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points121) # Separation '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points122) # Separation '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points123) # Separation '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points124) # Separation '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points125) # Separation '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points126) # Separation '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points127) # Separation '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points128) # Separation '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points129) # Separation '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points1210) # Separation '''

    pygame.draw.rect(ventana, (255, 100, 10), (t12.position[0]-20, t12.position[1]-20, 40, 40)) # Separation '''

    ventana.blit(SeparationText, (o121.position[0]-30, o121.position[1]-27))
    ventana.blit(SeparationText, (o122.position[0]-30, o122.position[1]-27))
    ventana.blit(SeparationText, (o123.position[0]-30, o123.position[1]-27))
    ventana.blit(SeparationText, (o124.position[0]-30, o124.position[1]-27))
    ventana.blit(SeparationText, (o125.position[0]-30, o125.position[1]-27))
    ventana.blit(SeparationText, (o126.position[0]-30, o126.position[1]-27))
    ventana.blit(SeparationText, (o127.position[0]-30, o127.position[1]-27))
    ventana.blit(SeparationText, (o128.position[0]-30, o128.position[1]-27))
    ventana.blit(SeparationText, (o129.position[0]-30, o129.position[1]-27))
    ventana.blit(SeparationText, (o1210.position[0]-30, o1210.position[1]-27))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()