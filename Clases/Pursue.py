from .Arrive import Arrive
import numpy as np

class Pursue(Arrive):
    #def __init__(self,character,target,maxAcceleration,maxSpeed,targetRadius,slowRadius,timeToTarget,maxPrediction,targetP): 
    def __init__(self, character, target, maxAcceleration, maxSpeed, targetRadius, slowRadius, timeToTarget,maxPrediction,targetR):
        super().__init__(character, target, maxAcceleration, maxSpeed, targetRadius, slowRadius, timeToTarget)
        # The maximum prediction time.
        self.maxPrediction =  maxPrediction # float
        # OVERRIDES the target data in seek (in other 
        # words this class has two bits of data called 
        # target: Seek.target is the superclass target 
        # which will be automatically calculated and 
        # shouldn’t be set, and Pursue.target is the 
        # target we’re pursuing).
        self.targetR = targetR # Kinematic  --> target real
         
        # ...Other data is derived from the superclass...
    
    def getSteeringP(self): # -> SteeringOutput:
        # 1. Calculate the target to delegate to seek
        # Work out the distance to target.
        direction = [0,0]
        direction[0] = self.targetR.position[0] - self.character.position[0]
        direction[1] = self.targetR.position[1] - self.character.position[1]
        vector_direction = np.array(direction)
        distance = np.linalg.norm(vector_direction)
    
        # Work out our current speed.
        vector_velocidad = np.array(self.character.velocity)
        speed = np.linalg.norm(vector_velocidad)
    
        # Check if speed gives a reasonable prediction time.
        #print(speed,"speed",distance,"distance",self.maxPrediction,"maxPrediction",distance / self.maxPrediction)
        if speed <= distance / self.maxPrediction:
            prediction = self.maxPrediction
        # Otherwise calculate the prediction time.
        else:
            prediction = distance / speed

        # Put the target together.
        # Seek.target = explicitTarget
        vector_velocidad2 = np.array(self.targetR.velocity)
        speed2 = np.linalg.norm(vector_velocidad2)
        if speed2 == 0:
            self.target.position[0] = self.targetR.position[0]
            self.target.position[1] = self.targetR.position[1]
        else:
            self.target.position[0] += self.targetR.velocity[0] * prediction
            self.target.position[1] += self.targetR.velocity[1] * prediction

        # 2. Delegate to Arrive.    
        return self.getSteering()