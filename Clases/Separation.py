from .SteeringOutput import SteeringOutput
import numpy as np

class Separation:
    def __init__(self,character,maxAcceleration,targets,threshold,decayCoefficient):
        
        self.character = character# Kinematic
        self.maxAcceleration = maxAcceleration # float

        # A list of potential targets.
        self.targets = targets # Kinematic[]

        # The threshold to take action.
        self.threshold = threshold #float

        # The constant coefficient of decay for 
        # the inverse square law.
        self.decayCoefficient = decayCoefficient # float

    def getSteering(self): # -> SteeringOutput:
        result = SteeringOutput([0,0],0)
        # Loop through each target.
        direction = [0,0]
        for target in self.targets:
            # Check if the target is close.
            direction[0] = target.position[0] - self.character.position[0]
            direction[1] = target.position[1] - self.character.position[1]

            vector_direccion = np.array(direction)
            distance = np.linalg.norm(vector_direccion)

            #print(distance,self.threshold)

            if distance < self.threshold:
                # Calculate the strength of repulsion
                # (here using the inverse square law).
                if distance == 0:
                    distance = 0.0001
                strength = min(self.decayCoefficient / (distance * distance),self.maxAcceleration)
                
                vector_normalizado = [0,0]
                vector_normalizado[0] = vector_direccion[0] / distance
                vector_normalizado[1] = vector_direccion[1] / distance

                result.linear[0] -= strength * vector_normalizado[0]
                result.linear[1] -= strength * vector_normalizado[1]
        return result