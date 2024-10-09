from .SteeringOutput import SteeringOutput
import numpy as np

class Arrive:
    def __init__(self,character,target,maxAcceleration,maxSpeed,targetRadius,slowRadius,timeToTarget): 
        self.character = character # Kinematic
        self.target = target   # Kinematic
        self.maxAcceleration = maxAcceleration # float
        self.maxSpeed = maxSpeed # float 
        # The radius for arriving at the target.
        self.targetRadius = targetRadius # float 
        # The radius for beginning to slow down.
        self.slowRadius = slowRadius # float 
        # The time over which to achieve target speed.
        self.timeToTarget = timeToTarget # float  0.1

    def getSteering(self): # -> SteeringOutput: 
        result = SteeringOutput([0,0],0) 

        # Get the direction to the target. 
        direction = [0,0]
        # Arrive
        direction[0] = self.target.position[0] - self.character.position[0]
        direction[1] = self.target.position[1] - self.character.position[1]
        # Flee
        #direction[0] = self.character.position[0] - self.target.position[0]
        #direction[1] = self.character.position[1] - self.target.position[1]
        vector_direction = np.array(direction)
        distance = np.linalg.norm(vector_direction)

        # Check if we are there, return no steering.
        #print(distance,self.targetRadius) 
        if distance < self.targetRadius: 
            # Request no steering.
            result = SteeringOutput([0,0],0) # Hace el papel de NULL
            return result
        # If we are outside the slowRadius, then move at max speed.
        if distance > self.slowRadius: 
            targetSpeed = self.maxSpeed 
        # Otherwise calculate a scaled speed. 
        else: 
            targetSpeed = self.maxSpeed * distance / self.slowRadius
            #targetSpeed = self.maxSpeed * (distance - self.targetRadius) / self.slowRadius

        # The target velocity combines speed and direction.
        targetVelocity = direction

        temp = np.array(targetVelocity)
        # Calcular la norma del vector
        norma = np.linalg.norm(temp)
        vector_normalizado = temp / norma

        targetVelocity[0] = vector_normalizado[0] * targetSpeed
        targetVelocity[1] = vector_normalizado[1] * targetSpeed

        # Acceleration tries to get to the target velocity.    
        result.linear[0] = targetVelocity[0] - self.character.velocity[0]
        result.linear[1] = targetVelocity[1] - self.character.velocity[1] 

        result.linear[0] /= self.timeToTarget 
        result.linear[1] /= self.timeToTarget 
        
        # Check if the acceleration is too fast.
        vector_acceleracion = np.array(result.linear)
        acceleracion = np.linalg.norm(vector_acceleracion)

        if acceleracion > self.maxAcceleration:
            temp2 = np.array(result.linear)
            # Calcular la norma del vector
            norma2 = np.linalg.norm(temp2)
            vector_normalizado2 = temp2 / norma2

            result.linear[0] = vector_normalizado2[0] * self.maxAcceleration
            result.linear[1] = vector_normalizado2[1] * self.maxAcceleration
        
        # Esta linea no esta en el algoritmo original, si quiero que cambie la orientacion la descomento
        # self.character.orientation = newOrientation(self.character.orientation,result.linear)
        
        result.angular = 0 
        return result