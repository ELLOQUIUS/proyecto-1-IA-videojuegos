from .SteeringOutput import SteeringOutput
import numpy as np

class VelocityMatch:
    def __init__(self,character,target,maxAcceleration,timeToTarget): 
        self.character = character # Kinematic
        self.target = target   # Kinematic
        self.maxAcceleration = maxAcceleration # float
        self.timeToTarget = timeToTarget # float  0.1

    def getSteering(self):# -> SteeringOutput:
        result = SteeringOutput([0,0],0)

        # Acceleration tries to get to the target velocity.
        result.linear[0] = self.target.velocity[0] - self.character.velocity[0]
        result.linear[1] = self.target.velocity[1] - self.character.velocity[1]
        #print(self.target.velocity,self.character.velocity, result.linear )
        result.linear[0] /= self.timeToTarget
        result.linear[1] /= self.timeToTarget

        # Check if the acceleration is too fast.
        vector_acceleracion = np.array(result.linear)
        acceleracion = np.linalg.norm(vector_acceleracion)

        if acceleracion > self.maxAcceleration:
            temp = np.array(result.linear)
            # Calcular la norma del vector
            norma = np.linalg.norm(temp)
            vector_normalizado = temp / norma

            result.linear[0] = vector_normalizado[0] * self.maxAcceleration
            result.linear[1] = vector_normalizado[1] * self.maxAcceleration

        #print(result.linear)
        result.angular = 0
        return result