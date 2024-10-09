from .Align import Align
from .SteeringOutput import SteeringOutput
from .funciones import radianes_a_grados
import numpy as np
import math

class LookWhereYoureGoing(Align):
    # No need for an overridden target member, we have
    # no explicit target to set.
    # ... Other data is derived from the superclass ...
    def __init__(self, character, target, maxAngularAcceleration, maxRotation, targetRadius, slowRadius, timeToTarget):
        super().__init__(character, target, maxAngularAcceleration, maxRotation, targetRadius, slowRadius, timeToTarget)
    
    def getSteeringLWYG(self): # -> SteeringOutput:
        # 1. Calculate the target to delegate to align
        # Check for a zero direction, and make no change if so.
        velocity = [0,0]
        velocity[0] = self.character.velocity[0]
        velocity[1] = self.character.velocity[1]

        vector_velocidad = np.array(velocity)
        speed = np.linalg.norm(vector_velocidad)

        if speed == 0:
            return SteeringOutput([0,0],0)

        # Otherwise set the target based on the velocity.
        self.target.orientation = math.atan2(-velocity[0], velocity[1])
        self.target.orientation = radianes_a_grados(self.target.orientation)

        # 2. Delegate to align.
        return self.getSteering()