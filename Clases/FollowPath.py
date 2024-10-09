from Seek import Seek

class Path:
    #def getParam(position: Vector, lastParam: float)# -> float
    def getParam(position, lastParam):
        print()
    #def getPosition(param: float)# -> Vector
    def getPosition(param: float):
        print()


class FollowPath(Seek):
    def __init__(self, character, target, maxAcceleration,path,pathOffset,currentPos):
        super().__init__(character, target, maxAcceleration)
        self.path = Path()
        # The distance along the path to generate the 
        # target. Can be negative if the character is 
        # moving in the reverse direction.
        self.pathOffset = pathOffset # float

        # The current position on the path.
        self.currentPos = currentPos # float

        # ...Other data is derived from the superclass...

    def getSteeringFP(self):# -> SteeringOutput:
        # 1. Calculate the target to delegate to face.
        # Find the current position on the path.
        currentParam = self.path.getParam(self.character.position, self.currentPos)
        # Offset it.
        targetParam = currentParam + self.pathOffset

        # Get the target position.
        self.target.position = self.path.getPosition(targetParam)

        # 2. Delegate to seek.
        return self.getSteering()