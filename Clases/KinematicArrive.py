from .KinematicSteeringOutput import KinematicSteeringOutput
from .funciones import newOrientation
import numpy as np

class KinematicArrive:
    def __init__(self,character, target, maxSpeed, radius, timeToTarget):
        self.character = character # Static
        self.target = target       # Static
        self.maxSpeed = maxSpeed   # float
        self.radius = radius   # float
        self.timeToTarget = timeToTarget   # float 0.25

    def getSteering(self): #-> KinematicSteeringOutput
        result = KinematicSteeringOutput([0,0],0)

        # Get the direction to the target.
        result.velocity[0] = self.target.position[0] - self.character.position[0]
        result.velocity[1] = self.target.position[1] - self.character.position[1]

        # Check if we’re within radius.
        vector_velocidad = np.array(result.velocity) # Normalizamos para sacar la rapidez
        rapidez = np.linalg.norm(vector_velocidad)
        if rapidez < self.radius:
            # Request no steering.
            result = KinematicSteeringOutput([0,0],0) # Hace el papel de NULL
            return result

        # We need to move to our target, we’d like
        # to get there in timeToTarget seconds.
        result.velocity[0] /= self.timeToTarget
        result.velocity[1] /= self.timeToTarget

        vector_velocidad = np.array(result.velocity)
        rapidez = np.linalg.norm(vector_velocidad)

        # If this is too fast, clip it to the max 
        # speed.
        if rapidez > self.maxSpeed:
            temp = np.array(result.velocity)
            # Calcular la norma del vector
            norma = np.linalg.norm(temp)
            # Normalizar el vector
            vector_normalizado = temp / norma
            result.velocity = vector_normalizado * self.maxSpeed

        # Face in the direction we want to move.
        self.character.orientation = newOrientation(self.character.orientation,result.velocity)
        result.rotation = 0
        return result