import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point1):
        return math.sqrt(((self.x - point1.x) ** 2) + ((self.y - point1.y) ** 2))