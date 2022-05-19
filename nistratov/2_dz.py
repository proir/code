import math
from re import S

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, x):
        self.x += x.x
        self.y += x.y
    
    def distance(self, point):
        return math.sqrt((self.x-point.x)**2 + (self.y-point.y)**2)


class Figure2D:
    def __init__(self, x, y):
        self.Center = Point2D(x,y)
    
    def move(self, point):
        self.Center+=point

    def moveTo(self, point):
        self.Center=point

class Triangle2D(Figure2D):
    def __init__(self, a, b, c):
        super().__init__(0,0)
        self.a = a
        self.b = b
        self.c = c
    def getArea(self):
        l12 = self.a.distance(self.a)
        l23 = self.b.distance(self.b)
        l13 = self.c.distance(self.a)
        P = (l12+l23+l13)/2
        return(math.sqrt(P *(P-l12)*(P-l13)*(P-l23)))

