import math
import numpy as np
import random
import pygame
from .Kinematic import Kinematic

def newOrientation(current, velocity): # -> float
    # Make sure we have a velocity.
    vector_velocidad = np.array(velocity)
    rapidez = np.linalg.norm(vector_velocidad)
    if rapidez > 0:
        # Calculate orientation from the velocity.
        #return math.atan2(-velocity[0], velocity[1])
        return math.degrees(math.atan2(velocity[1], velocity[0]))

    # Otherwise use the current orientation.
    else:
        return current

def randomBinomial():
    return 2 * random.random() - 1

def mapToRange(angle):# -> float:
	return (angle + math.pi) % (2 * math.pi) - math.pi

def grados_a_radianes(grados):
    return grados * math.pi / 180

def radianes_a_grados(radianes):
    return radianes * (180 / math.pi)

def rotate_polygon(polygon, angle):
    return [point.rotate(angle) for point in polygon]

def calculate_angle(pos1, pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    angle = math.degrees(math.atan2(dy, dx))
    return angle

def movimiento_teclado(keys,target,velocityT,rot):
    if keys[pygame.K_a]: # Escribo "pygame.K_(tecla)" para capturar la tecla que quiero
        target.position[0] -= velocityT
        if rot:
            target.orientation = 180
    if keys[pygame.K_d]:
        target.position[0] += velocityT
        if rot:
            target.orientation = 0
    if keys[pygame.K_w]:
        target.position[1] -= velocityT
        if rot:
            target.orientation = -90
    if keys[pygame.K_s]:
        target.position[1] += velocityT
        if rot:
            target.orientation = 90
    if keys[pygame.K_a] and keys[pygame.K_w] and rot:
        target.orientation = -135
    if keys[pygame.K_a] and keys[pygame.K_s] and rot:
        target.orientation = 135
    if keys[pygame.K_w] and keys[pygame.K_d] and rot:
        target.orientation = -45
    if keys[pygame.K_s] and keys[pygame.K_d] and rot:
        target.orientation = 45

def movimiento_teclado_cambio_velocity(keys,target,velocityT,rot):
    banda = False
    bandw = False
    bands = False
    bandd = False
    if keys[pygame.K_a]: # Escribo "pygame.K_(tecla)" para capturar la tecla que quiero
        banda = True
        target.velocity[0] = -velocityT;
        #target.position[0] -= velocityT
        if rot:
            target.orientation = 180
    if keys[pygame.K_d]:
        bandd = True
        target.velocity[0] = velocityT;
        #target.position[0] += velocityT
        if rot:
            target.orientation = 0
    if keys[pygame.K_w]:
        bandw = True
        target.velocity[1] = -velocityT;
        #target.position[1] -= velocityT
        if rot:
            target.orientation = -90
    if keys[pygame.K_s]:
        bands = True
        target.velocity[1] = velocityT;
        #target.position[1] += velocityT
        if rot:
            target.orientation = 90
    if keys[pygame.K_a] and keys[pygame.K_w] and rot:
        target.orientation = -135
    if keys[pygame.K_a] and keys[pygame.K_s] and rot:
        target.orientation = 135
    if keys[pygame.K_w] and keys[pygame.K_d] and rot:
        target.orientation = -45
    if keys[pygame.K_s] and keys[pygame.K_d] and rot:
        target.orientation = 45

    if not banda and not bandd:
        target.velocity[0] = 0
    if not bandw and not bands:
        target.velocity[1] = 0

def desacelerar(personaje, factor_desaceleracion):
    result = Kinematic([personaje.position[0],personaje.position[1]],[personaje.velocity[0],personaje.velocity[1]],personaje.orientation,personaje.rotation)
    
    if result.velocity[0] > 0:
        result.velocity[0] -= factor_desaceleracion
        if result.velocity[0] < 0:
            result.velocity[0] = 0
    if result.velocity[0] < 0:
        result.velocity[0] += factor_desaceleracion
        if result.velocity[0] > 0:
            result.velocity[0] = 0
    if result.velocity[1] > 0:
        result.velocity[1] -= factor_desaceleracion
        if result.velocity[1] < 0:
            result.velocity[1] = 0
    if result.velocity[1] < 0:
        result.velocity[1] += factor_desaceleracion
        if result.velocity[1] > 0:
            result.velocity[1] = 0

    return result
       
    