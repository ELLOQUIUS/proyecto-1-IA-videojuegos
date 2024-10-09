from .SteeringOutput import SteeringOutput
from .Kinematic import Kinematic
import numpy as np

class CollisionAvoidance:
    def __init__(self,character,maxAcceleration,targets,radius): 
        self.character = character # Kinematic
        self.maxAcceleration = maxAcceleration # float
        # A list of potential targets.
        self.targets = targets # Kinematic[]
        # The collision radius of a character (assuming 
        # all characters have the same radius here).
        self.radius = radius # float

    def getSteering(self): # -> SteeringOutput:
        # 1. Find the target that’s closest to collision
        # Store the first collision time.
        shortestTime = 10000000000

        # Store the target that collides then, and 
        # other data that we will need and can avoid
        # recalculating.
        firstTarget = Kinematic([0,0],[0,0],0,0) # Kinematic
        firstMinSeparation = 0.0 # float
        firstDistance = 0.0
        firstRelativePos = [0,0] # Vector
        firstRelativeVel = [0,0] # Vector
        # Loop through each target.
        for target in self.targets:
            # Calculate the time to collision.
            relativePos = [0,0]
            relativePos[0] = target.position[0] - self.character.position[0]
            relativePos[1] = target.position[1] - self.character.position[1]
            relativeVel = [0,0]
            relativeVel[0] = target.velocity[0] - self.character.velocity[0]
            relativeVel[1] = target.velocity[1] - self.character.velocity[1]

            vector_velocidadRel = np.array(relativeVel)
            relativeSpeed = np.linalg.norm(vector_velocidadRel)

            vector_posRel = np.array(relativePos)

            timeToCollision = np.dot(vector_posRel, vector_velocidadRel)/(relativeSpeed * relativeSpeed)

            # Check if it is going to be a collision at all.
            distance = np.linalg.norm(vector_posRel)
            minSeparation = distance - relativeSpeed * timeToCollision
            print(minSeparation,2 * self.radius)
            if minSeparation > 2 * self.radius:
                continue

            # Check if it is the shortest.
            if timeToCollision > 0 and timeToCollision < shortestTime:
                # Store the time, target and other data.
                shortestTime = timeToCollision
                firstTarget = target
                firstMinSeparation = minSeparation
                firstDistance = distance
                firstRelativePos[0] = relativePos[0]
                firstRelativePos[1] = relativePos[1]
                firstRelativeVel[0] = relativeVel[0]
                firstRelativeVel[1] = relativeVel[1]
        print()
        # 2. Calculate the steering
        # If we have no target, then exit.
        if not firstTarget:
            result = SteeringOutput([0,0],0)
            return result

        # If we’re going to hit exactly, or if we’re already
        # colliding, then do the steering based on current position.
        if firstMinSeparation <= 0 or firstDistance < 2 * self.radius:
            relativePos[0] = firstTarget.position[0] - self.character.position[0]
            relativePos[1] = firstTarget.position[1] - self.character.position[1]

        # Otherwise calculate the future relative position.
        else:
            relativePos[0] = firstRelativePos[0] + firstRelativeVel[0] * shortestTime
            relativePos[1] = firstRelativePos[1] + firstRelativeVel[1] * shortestTime

        # Avoid the target.
        temp = np.array(relativePos)
        norma = np.linalg.norm(temp)
        vector_normalizado = temp/norma

        result = SteeringOutput([0,0],0)
        result.linear[0] = vector_normalizado[0] * self.maxAcceleration
        result.linear[1] = vector_normalizado[1] * self.maxAcceleration
        result.angular = 0
        return result
