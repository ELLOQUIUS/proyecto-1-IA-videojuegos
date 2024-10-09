from .Face import Face
from .funciones import randomBinomial
import math

class Wander(Face):
    def __init__(self, character, target, maxAngularAcceleration, maxRotation, targetRadius, slowRadius, timeToTarget, targetF,wanderOffset,wanderRadius,wanderRate,wanderOrientation,maxAcceleration):
        super().__init__(character, target, maxAngularAcceleration, maxRotation, targetRadius, slowRadius, timeToTarget, targetF)
        # The radius and forward offset of the 
        # wander circle.
        self.wanderOffset = wanderOffset # float. distancia del personaje al centro del circulo imaginario
        self.wanderRadius = wanderRadius # float. radio del circulo imaginario
        # The maximum rate at which the wander 
        # orientation can change.
        self.wanderRate = wanderRate # float. que tanto puede cambiar el objetivo del circulo
        # The current orientation of the wander target.
        self.wanderOrientation = wanderOrientation # float. orientacion actual del punto del circulo
        # The maximum acceleration of the character.
        self.maxAcceleration = maxAcceleration # float

        # Again we don’t need a new target.
        # ...Other data is derived from the superclass...

    def getSteeringW(self):# -> SteeringOutput:
        # 1. Calculate the target to delegate to face
        # Update the wander orientation.
        self.wanderOrientation += randomBinomial() * self.wanderRate
        # Calculate the combined target orientation.
        targetOrientation = self.wanderOrientation + self.character.orientation
        # Calculate the center of the wander circle.
        #target = [0,0]
        self.target.position[0] = self.character.position[0] + self.wanderOffset * self.character.asVector()[0]
        self.target.position[1] = self.character.position[1] + self.wanderOffset * self.character.asVector()[1]

        # Calculate the target location.
        radian = math.radians(targetOrientation)
        x = math.cos(radian)
        y = math.sin(radian)
        tarOriVec = [x,y]
        self.target.position[0] += self.wanderRadius * tarOriVec[0]
        self.target.position[1] += self.wanderRadius * tarOriVec[1]

        # 2. Delegate to face.
        result = self.getSteeringF()
        #print(result.angular)

        # 3. Now set the linear acceleration to be at full
        # acceleration in the direction of the orientation.
        result.linear[0] = self.maxAcceleration * self.character.asVector()[0]
        result.linear[1] = self.maxAcceleration * self.character.asVector()[1]

        return result