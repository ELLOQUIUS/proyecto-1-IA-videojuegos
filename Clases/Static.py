import math
import numpy as np

class Static:
    def __init__(self,position, orientation):
        self.position = position        # vector
        self.orientation = orientation  # float
    # Transforma en angulo (la orientacion) a su vector unitario correspondiente
    def asVector(self):
        radian = math.radians(self.orientation)
        x = math.cos(radian)
        y = math.sin(radian)
        return [x, y]
