from .Align import Align
from .SteeringOutput import SteeringOutput
from .funciones import radianes_a_grados
import math
import numpy as np

class Face(Align):
    def __init__(self, character, target, maxAngularAcceleration, maxRotation, targetRadius, slowRadius, timeToTarget,targetF):
        super().__init__(character, target, maxAngularAcceleration, maxRotation, targetRadius, slowRadius, timeToTarget)
        # Overrides the Align.target member.
        self.targetF = targetF # Kinematic
    # ... Other data is derived from the superclass ...

    # Implemented as it was in Pursue.
    def getSteeringF(self):# -> SteeringOutput:
        # 1. Calculate the target to delegate to align
        # Work out the direction to target.
        direction = [0,0]
        direction[0] = self.targetF.position[0] - self.character.position[0]
        direction[1] = self.targetF.position[1] - self.character.position[1]

        # Check for a zero direction, and make no change if so.
        vector_direction = np.array(direction)
        distance = np.linalg.norm(vector_direction)

        if distance == 0:
            return SteeringOutput([0,0],0)

        # 2. Delegate to align.
        #self.target = explicitTarget
        self.target.orientation = math.atan2(-direction[0],direction[1]) # atan2 devuelve radianes
        self.target.orientation = radianes_a_grados(self.target.orientation)

        return self.getSteering()