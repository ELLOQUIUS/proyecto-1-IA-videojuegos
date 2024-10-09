from .KinematicSteeringOutput import KinematicSteeringOutput
from .funciones import randomBinomial

class KinematicWander:
    def __init__(self,character, maxSpeed,maxRotation):
        self.character = character # Static
        self.maxSpeed = maxSpeed   # float
        # The maximum rotation speed we’d like, probably should be 
        # smaller than the maximum possible, for a leisurely change 
        # in direction.
        self.maxRotation = maxRotation  # float


    def getSteering(self): # -> KinematicSteeringOutput:
        result = KinematicSteeringOutput([0,0],0)

        # Get velocity from the vector form of the orientation.
        result.velocity[0] = self.maxSpeed * self.character.asVector()[0]
        result.velocity[1] = self.maxSpeed * self.character.asVector()[1]
        
        # Change our orientation randomly.
        result.rotation = randomBinomial() * self.maxRotation

        return result