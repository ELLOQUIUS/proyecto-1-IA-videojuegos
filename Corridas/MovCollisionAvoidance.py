# Ejecutar archivo con "python -m Corridas.MovCollisionAvoidance.py" en caso de no usar
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# y colocar es punto punto, es decir: from ..Clases.CollisionAvoidance import CollisionAvoidance
# Taambien colocar el archivo "__init__.py" en cada carpeta

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from Clases.CollisionAvoidance import CollisionAvoidance
from Clases.Wander import Wander
from Clases.SteeringOutput import SteeringOutput
from Clases.Kinematic import Kinematic
from Clases.funciones import movimiento_teclado_cambio_velocity,rotate_polygon
import numpy as np
import math

o1 = Kinematic([150,100],[0,0],0,0) # Personaje (Wandering) 
o2 = Kinematic([200,200],[0,0],0,0) # Personaje (Wandering) 
o3 = Kinematic([250,300],[0,0],0,0) # Personaje (Wandering) 
o4 = Kinematic([300,400],[0,0],0,0) # Personaje (Wandering) 
o5 = Kinematic([350,500],[0,0],0,0) # Personaje (Wandering)
o6 = Kinematic([850,100],[0,0],180,0) # Personaje (Wandering) 
o7 = Kinematic([800,200],[0,0],180,0) # Personaje (Wandering) 
o8 = Kinematic([750,300],[0,0],180,0) # Personaje (Wandering) 
o9 = Kinematic([700,400],[0,0],180,0) # Personaje (Wandering) 
o10 = Kinematic([650,500],[0,0],180,0) # Personaje (Wandering) 

t1 = Kinematic([250,100],[0,0],0,0) # Target (Wandering)
tF1 = t1 # TargetF (Wandering). En este caso lo hago asi ya que no tengo un target que yo controle manualmente
t2 = Kinematic([250,200],[0,0],0,0) # Target (Wandering)
tF2 = t2 # TargetF (Wandering). En este caso lo hago asi ya que no tengo un target que yo controle manualmente
t3 = Kinematic([250,300],[0,0],0,0) # Target (Wandering)
tF3 = t3 # TargetF (Wandering). En este caso lo hago asi ya que no tengo un target que yo controle manualmente
t4 = Kinematic([250,400],[0,0],0,0) # Target (Wandering)
tF4 = t4 # TargetF (Wandering). En este caso lo hago asi ya que no tengo un target que yo controle manualmente
t5 = Kinematic([250,500],[0,0],0,0) # Target (Wandering)
tF5 = t5 # TargetF (Wandering). En este caso lo hago asi ya que no tengo un target que yo controle manualmente
t6 = Kinematic([750,100],[0,0],0,0) # Target (Wandering)
tF6 = t6 # TargetF (Wandering). En este caso lo hago asi ya que no tengo un target que yo controle manualmente
t7 = Kinematic([750,200],[0,0],0,0) # Target (Wandering)
tF7 = t7 # TargetF (Wandering). En este caso lo hago asi ya que no tengo un target que yo controle manualmente
t8 = Kinematic([750,300],[0,0],0,0) # Target (Wandering)
tF8 = t8 # TargetF (Wandering). En este caso lo hago asi ya que no tengo un target que yo controle manualmente
t9 = Kinematic([750,400],[0,0],0,0) # Target (Wandering)
tF9 = t9 # TargetF (Wandering). En este caso lo hago asi ya que no tengo un target que yo controle manualmente
t10 = Kinematic([750,500],[0,0],0,0) # Target (Wandering)
tF10 = t10 # TargetF (Wandering). En este caso lo hago asi ya que no tengo un target que yo controle manualmente

k1 = Wander(o1,t1,0.05,0.1,0.01,0.5,1,tF1,0,50,3,90,0.2)
k2 = Wander(o2,t2,0.05,0.1,0.01,0.5,1,tF2,0,50,3,90,0.2)
k3 = Wander(o3,t3,0.05,0.1,0.01,0.5,1,tF3,0,50,3,90,0.2)
k4 = Wander(o4,t4,0.05,0.1,0.01,0.5,1,tF4,0,50,3,90,0.2)
k5 = Wander(o5,t5,0.05,0.1,0.01,0.5,1,tF5,0,50,3,90,0.2)
k6 = Wander(o6,t6,0.05,0.1,0.01,0.5,1,tF6,0,50,3,270,0.2)
k7 = Wander(o7,t7,0.05,0.1,0.01,0.5,1,tF7,0,50,3,270,0.2)
k8 = Wander(o8,t8,0.05,0.1,0.01,0.5,1,tF8,0,50,3,270,0.2)
k9 = Wander(o9,t9,0.05,0.1,0.01,0.5,1,tF9,0,50,3,270,0.2)
k10 = Wander(o10,t10,0.05,0.1,0.01,0.5,1,tF10,0,50,3,270,0.2)

radioINT = 70
maxAC = 0.15
k1CA = CollisionAvoidance(o1,maxAC,[o2,o3,o4,o5,o6,o7,o8,o9,o10],radioINT)
k2CA = CollisionAvoidance(o2,maxAC,[o1,o3,o4,o5,o6,o7,o8,o9,o10],radioINT)
k3CA = CollisionAvoidance(o3,maxAC,[o2,o1,o4,o5,o6,o7,o8,o9,o10],radioINT)
k4CA = CollisionAvoidance(o4,maxAC,[o2,o3,o1,o5,o6,o7,o8,o9,o10],radioINT)
k5CA = CollisionAvoidance(o5,maxAC,[o2,o3,o4,o1,o6,o7,o8,o9,o10],radioINT)
k6CA = CollisionAvoidance(o6,maxAC,[o2,o3,o4,o5,o1,o7,o8,o9,o10],radioINT)
k7CA = CollisionAvoidance(o7,maxAC,[o2,o3,o4,o5,o6,o1,o8,o9,o10],radioINT)
k8CA = CollisionAvoidance(o8,maxAC,[o2,o3,o4,o5,o6,o7,o1,o9,o10],radioINT)
k9CA = CollisionAvoidance(o9,maxAC,[o2,o3,o4,o5,o6,o7,o8,o1,o10],radioINT)
k10CA = CollisionAvoidance(o10,maxAC,[o2,o3,o4,o5,o6,o7,o8,o9,o1],radioINT)

base = 20
altura = 30
arrow = [
    pygame.Vector2(0, -altura),  # Vértice superior
    pygame.Vector2(-base / 2, 0),  # Vértice inferior izquierdo
    pygame.Vector2(base / 2, 0)  # Vértice inferior derecho
]

pygame.init()
ventana = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Wander")

tamaño = 50
fuente = pygame.font.Font(None, 20)
WanderText = fuente.render('Wander', True, (0, 0, 0))

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))

    wandering1 = k1.getSteeringW() # Me da un SteeringOutput. Realiza Wander del personaje al target
    wandering2 = k2.getSteeringW() # Me da un SteeringOutput. Realiza Wander del personaje al target
    wandering3 = k3.getSteeringW() # Me da un SteeringOutput. Realiza Wander del personaje al target
    wandering4 = k4.getSteeringW() # Me da un SteeringOutput. Realiza Wander del personaje al target
    wandering5 = k5.getSteeringW() # Me da un SteeringOutput. Realiza Wander del personaje al target
    wandering6 = k6.getSteeringW() # Me da un SteeringOutput. Realiza Wander del personaje al target
    wandering7 = k7.getSteeringW() # Me da un SteeringOutput. Realiza Wander del personaje al target
    wandering8 = k8.getSteeringW() # Me da un SteeringOutput. Realiza Wander del personaje al target
    wandering9 = k9.getSteeringW() # Me da un SteeringOutput. Realiza Wander del personaje al target
    wandering10 = k10.getSteeringW() # Me da un SteeringOutput. Realiza Wander del personaje al target

    coll_avoid1 = k1CA.getSteering()
    coll_avoid2 = k2CA.getSteering() 
    coll_avoid3 = k3CA.getSteering() 
    coll_avoid4 = k4CA.getSteering() 
    coll_avoid5 = k5CA.getSteering() 
    coll_avoid6 = k6CA.getSteering() 
    coll_avoid7 = k7CA.getSteering() 
    coll_avoid8 = k8CA.getSteering() 
    coll_avoid9 = k9CA.getSteering() 
    coll_avoid10 = k10CA.getSteering() 

    wan_coll1 = SteeringOutput([0,0],0)
    wan_coll2 = SteeringOutput([0,0],0)
    wan_coll3 = SteeringOutput([0,0],0)
    wan_coll4 = SteeringOutput([0,0],0)
    wan_coll5 = SteeringOutput([0,0],0)
    wan_coll6 = SteeringOutput([0,0],0)
    wan_coll7 = SteeringOutput([0,0],0)
    wan_coll8 = SteeringOutput([0,0],0)
    wan_coll9 = SteeringOutput([0,0],0)
    wan_coll10 = SteeringOutput([0,0],0)

    print(wandering1.linear,coll_avoid1.linear)

    coef = 3.3
    wan_coll1.linear[0] = 2*wandering1.linear[0] - coef*coll_avoid1.linear[0]
    wan_coll1.linear[1] = 2*wandering1.linear[1] - coef*coll_avoid1.linear[1]
    wan_coll1.angular = wandering1.angular + coll_avoid1.angular

    wan_coll2.linear[0] = 2*wandering2.linear[0] - coef*coll_avoid2.linear[0]
    wan_coll2.linear[1] = 2*wandering2.linear[1] - coef*coll_avoid2.linear[1]
    wan_coll2.angular = wandering2.angular + coll_avoid2.angular

    wan_coll3.linear[0] = 2*wandering3.linear[0] - coef*coll_avoid3.linear[0]
    wan_coll3.linear[1] = 2*wandering3.linear[1] - coef*coll_avoid3.linear[1]
    wan_coll3.angular = wandering3.angular + coll_avoid3.angular

    wan_coll4.linear[0] = 2*wandering4.linear[0] - coef*coll_avoid4.linear[0]
    wan_coll4.linear[1] = 2*wandering4.linear[1] - coef*coll_avoid4.linear[1]
    wan_coll4.angular = wandering4.angular + coll_avoid4.angular

    wan_coll5.linear[0] = 2*wandering5.linear[0] - coef*coll_avoid5.linear[0]
    wan_coll5.linear[1] = 2*wandering5.linear[1] - coef*coll_avoid5.linear[1]
    wan_coll5.angular = wandering5.angular + coll_avoid5.angular

    wan_coll6.linear[0] = 2*wandering6.linear[0] - coef*coll_avoid6.linear[0]
    wan_coll6.linear[1] = 2*wandering6.linear[1] - coef*coll_avoid6.linear[1]
    wan_coll6.angular = wandering6.angular + coll_avoid6.angular

    wan_coll7.linear[0] = 2*wandering7.linear[0] - coef*coll_avoid7.linear[0]
    wan_coll7.linear[1] = 2*wandering7.linear[1] - coef*coll_avoid7.linear[1]
    wan_coll7.angular = wandering7.angular + coll_avoid7.angular

    wan_coll8.linear[0] = 2*wandering8.linear[0] - coef*coll_avoid8.linear[0]
    wan_coll8.linear[1] = 2*wandering8.linear[1] - coef*coll_avoid8.linear[1]
    wan_coll8.angular = wandering8.angular + coll_avoid8.angular

    wan_coll9.linear[0] = 2*wandering9.linear[0] - coef*coll_avoid9.linear[0]
    wan_coll9.linear[1] = 2*wandering9.linear[1] - coef*coll_avoid9.linear[1]
    wan_coll9.angular = wandering9.angular + coll_avoid9.angular

    wan_coll10.linear[0] = 2*wandering10.linear[0] - coef*coll_avoid10.linear[0]
    wan_coll10.linear[1] = 2*wandering10.linear[1] - coef*coll_avoid10.linear[1]
    wan_coll10.angular = wandering10.angular + coll_avoid10.angular

    velocity = 7
    maxVEL = 0.55
    o1.update(wan_coll1,maxVEL,1)
    o2.update(wan_coll2,maxVEL,1)
    o3.update(wan_coll3,maxVEL,1)
    o4.update(wan_coll4,maxVEL,1)
    o5.update(wan_coll5,maxVEL,1)
    o6.update(wan_coll6,maxVEL,1)
    o7.update(wan_coll7,maxVEL,1)
    o8.update(wan_coll8,maxVEL,1)
    o9.update(wan_coll9,maxVEL,1)
    o10.update(wan_coll10,maxVEL,1)

    rotated_arrow1 = rotate_polygon(arrow, k1.character.orientation + 90) # Wander '''
    rotated_arrow2 = rotate_polygon(arrow, k2.character.orientation + 90) # Wander '''
    rotated_arrow3 = rotate_polygon(arrow, k3.character.orientation + 90) # Wander '''
    rotated_arrow4 = rotate_polygon(arrow, k4.character.orientation + 90) # Wander '''
    rotated_arrow5 = rotate_polygon(arrow, k5.character.orientation + 90) # Wander '''
    rotated_arrow6 = rotate_polygon(arrow, k6.character.orientation - 270) # Wander '''
    rotated_arrow7 = rotate_polygon(arrow, k7.character.orientation - 270) # Wander '''
    rotated_arrow8 = rotate_polygon(arrow, k8.character.orientation - 270) # Wander '''
    rotated_arrow9 = rotate_polygon(arrow, k9.character.orientation - 270) # Wander '''
    rotated_arrow10 = rotate_polygon(arrow, k10.character.orientation - 270) # Wander '''

    arrow_points1 = [([k1.character.position[0],k1.character.position[1]] + point) for point in rotated_arrow1] # Wander'''
    arrow_points2 = [([k2.character.position[0],k2.character.position[1]] + point) for point in rotated_arrow2] # Wander'''
    arrow_points3 = [([k3.character.position[0],k3.character.position[1]] + point) for point in rotated_arrow3] # Wander'''
    arrow_points4 = [([k4.character.position[0],k4.character.position[1]] + point) for point in rotated_arrow4] # Wander'''
    arrow_points5 = [([k5.character.position[0],k5.character.position[1]] + point) for point in rotated_arrow5] # Wander'''
    arrow_points6 = [([k6.character.position[0],k6.character.position[1]] + point) for point in rotated_arrow6] # Wander'''
    arrow_points7 = [([k7.character.position[0],k7.character.position[1]] + point) for point in rotated_arrow7] # Wander'''
    arrow_points8 = [([k8.character.position[0],k8.character.position[1]] + point) for point in rotated_arrow8] # Wander'''
    arrow_points9 = [([k9.character.position[0],k9.character.position[1]] + point) for point in rotated_arrow9] # Wander'''
    arrow_points10 = [([k10.character.position[0],k10.character.position[1]] + point) for point in rotated_arrow10] # Wander'''

    pygame.draw.circle(ventana, (0,0,0), (o1.position[0], o1.position[1]), radioINT)
    pygame.draw.circle(ventana, (255,255,255), (o1.position[0], o1.position[1]), radioINT-1)
    pygame.draw.circle(ventana, (0,0,0), (o2.position[0], o2.position[1]), radioINT)
    pygame.draw.circle(ventana, (255,255,255), (o2.position[0], o2.position[1]), radioINT-1)
    pygame.draw.circle(ventana, (0,0,0), (o3.position[0], o3.position[1]), radioINT)
    pygame.draw.circle(ventana, (255,255,255), (o3.position[0], o3.position[1]), radioINT-1)
    pygame.draw.circle(ventana, (0,0,0), (o4.position[0], o4.position[1]), radioINT)
    pygame.draw.circle(ventana, (255,255,255), (o4.position[0], o4.position[1]), radioINT-1)
    pygame.draw.circle(ventana, (0,0,0), (o5.position[0], o5.position[1]), radioINT)
    pygame.draw.circle(ventana, (255,255,255), (o5.position[0], o5.position[1]), radioINT-1)
    pygame.draw.circle(ventana, (0,0,0), (o6.position[0], o6.position[1]), radioINT)
    pygame.draw.circle(ventana, (255,255,255), (o6.position[0], o6.position[1]), radioINT-1)
    pygame.draw.circle(ventana, (0,0,0), (o7.position[0], o7.position[1]), radioINT)
    pygame.draw.circle(ventana, (255,255,255), (o7.position[0], o7.position[1]), radioINT-1)
    pygame.draw.circle(ventana, (0,0,0), (o8.position[0], o8.position[1]), radioINT)
    pygame.draw.circle(ventana, (255,255,255), (o8.position[0], o8.position[1]), radioINT-1)
    pygame.draw.circle(ventana, (0,0,0), (o9.position[0], o9.position[1]), radioINT)
    pygame.draw.circle(ventana, (255,255,255), (o9.position[0], o9.position[1]), radioINT-1)
    pygame.draw.circle(ventana, (0,0,0), (o10.position[0], o10.position[1]), radioINT)
    pygame.draw.circle(ventana, (255,255,255), (o10.position[0], o10.position[1]), radioINT-1)

    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points1) # Wander '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points2) # Wander '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points3) # Wander '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points4) # Wander '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points5) # Wander '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points6) # Wander '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points7) # Wander '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points8) # Wander '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points9) # Wander '''
    pygame.draw.polygon(ventana, (0, 0, 255), arrow_points10) # Wander '''

    ventana.blit(WanderText, (o1.position[0]-30, o1.position[1]-27))
    ventana.blit(WanderText, (o2.position[0]-30, o2.position[1]-27))
    ventana.blit(WanderText, (o3.position[0]-30, o3.position[1]-27))
    ventana.blit(WanderText, (o4.position[0]-30, o4.position[1]-27))
    ventana.blit(WanderText, (o5.position[0]-30, o5.position[1]-27))
    ventana.blit(WanderText, (o6.position[0]-30, o6.position[1]-27))
    ventana.blit(WanderText, (o7.position[0]-30, o7.position[1]-27))
    ventana.blit(WanderText, (o8.position[0]-30, o8.position[1]-27))
    ventana.blit(WanderText, (o9.position[0]-30, o9.position[1]-27))
    ventana.blit(WanderText, (o10.position[0]-30, o10.position[1]-27))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()