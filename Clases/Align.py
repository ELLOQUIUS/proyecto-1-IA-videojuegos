from .SteeringOutput import SteeringOutput
from .funciones import grados_a_radianes,mapToRange

class Align:
    def __init__(self,character,target,maxAngularAcceleration,maxRotation,targetRadius,slowRadius,timeToTarget): 
        self.character = character # Kinematic
        self.target = target   # Kinematic
        self.maxAngularAcceleration = maxAngularAcceleration # float
        self.maxRotation = maxRotation # float 
        # The radius for arriving at the target.
        self.targetRadius = targetRadius # float 
        # The radius for beginning to slow down.
        self.slowRadius = slowRadius # float 
        # The time over which to achieve target speed.
        self.timeToTarget = timeToTarget # float  0.1

    def getSteering(self):# -> SteeringOutput:
        result = SteeringOutput([0,0],0)

        # Get the naive direction to the target.
        tarOriRad = grados_a_radianes(self.target.orientation) # Hago esto porque la orientacion normal esta en grados, no radianes
        chaOriRad = grados_a_radianes(self.character.orientation)
        # Align
        rotation = tarOriRad - chaOriRad
        # Not Align
        #rotation = chaOriRad - tarOriRad
        # Map the result to the (-pi, pi) interval.
        rotation = mapToRange(rotation)
        rotationSize = abs(rotation)

        # Check if we are there, return no steering.
        if rotationSize < self.targetRadius:
            result = SteeringOutput([0,0],0)
            return result
        # If we are outside the slowRadius, then 
        # use maximum rotation.
        if rotationSize > self.slowRadius:
            targetRotation = self.maxRotation
        # Otherwise calculate a scaled rotation.
        else:
            targetRotation = self.maxRotation * rotationSize / self.slowRadius

        # The final target rotation combines speed (already in the
        # variable) and direction.
        targetRotation *= rotation / rotationSize
        
        # Acceleration tries to get to the target rotation.
        result.angular = targetRotation - self.character.rotation
        result.angular /= self.timeToTarget
        
        # Check if the acceleration is too great.
        angularAcceleration = abs(result.angular)
        if angularAcceleration > self.maxAngularAcceleration:
            result.angular /= angularAcceleration
            result.angular *= self.maxAngularAcceleration

        result.linear = [0,0]
        return result