from .KinematicSteeringOutput import KinematicSteeringOutput
from .funciones import newOrientation
import numpy as np

class KinematicFlee:
    def __init__(self,character, target, maxSpeed):
        self.character = character # Static
        self.target = target       # Static
        self.maxSpeed = maxSpeed   # float

    def getSteering(self): # -> KinematicSteeringOutput
        result = KinematicSteeringOutput([0,0],0) # Valores por defecto

        # Get the direction to the target. Para las posiciones x y y

        # Huir
        result.velocity[0] = self.character.position[0] - self.target.position[0]
        result.velocity[1] = self.character.position[1] - self.target.position[1]

        # The velocity is along this direction, at full speed. Normalizamos
        #result.velocity.normalize() -> Para esto hago lo siguiente
        temp = np.array(result.velocity)
        # Calcular la norma del vector
        norma = np.linalg.norm(temp)
        # El if es para el caso cuando temp = [0,0] y por tanto su norma es 0 con lo
        # cual no puedo dividir entre 0
        if temp[0] == 0 and temp[1] == 0:
            vector_normalizado = np.array([0,0])
        else:
            vector_normalizado = temp / norma
        # Normalizar el vector
        result.velocity = vector_normalizado * self.maxSpeed

        # Face in the direction we want to move.
        self.character.orientation = newOrientation(self.character.orientation,result.velocity)
        result.rotation = 0
        return result