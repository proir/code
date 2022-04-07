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
    """
        Point Center - точка привязки фигуры, по-хорошему - центр масс.
    """
    def __init__(self, x, y):
        self.Center = Point2D(x,y)
    
    def move(self, point):
        self.Center+=point

    def moveTo(self, point):
        self.Center=point
#поворачивать сложно - нужно обозначать базис и прочее-прочее.

class Triangle2D(Figure2D):
    """
        Point1, Point2, Point3, 
    """
    def __init__(self, point1, point2, point3):
        super().__init__(0,0)
        self.Point1 = point1
        self.Point2 = point2
        self.Point3 = point3
    def getArea(self):
        l12 = self.Point1.distance(self.Point2)
        l23 = self.Point2.distance(self.Point2)
        l13 = self.Point3.distance(self.Point1)
        pp = (l12+l23+l13)/2
        return(math.sqrt(pp *(pp-l12)*(pp-l13)*(pp-l23)))

class Tetragon2D(Figure2D):
    """
        Point1, Point2, Point3, Point4
    """
    def __init__(self, point1, point2, point3, point4):
        super().__init__(0,0)
        self.Point1 = point1
        self.Point2 = point2
        self.Point3 = point3
        self.Point4 = point4
    def getArea(self):
        x = Triangle2D(self.Point1, self.Point2, self.Point3)
        y = Triangle2D(self.Point2, self.Point3, self.Point4)
        return x.getArea()+y.getArea() 

class Rectagnle2D(Tetragon2D):
    """
        Point1, Point2
    """
    def __init__(self, point1, point2):
        super().__init__(point1, Point2D(point1.x, point2.y), 
        point2, Point2D(point2.x, point1.y))

        # self.Point1 = point1
        # self.Point2 = point2
    
    def getArea(self):
        S = (self.Point1.x-self.Point2.x)*(self.Point1.y-self.Point2.y)
        if(S<0):
            return -S
        return S

class Square2D(Rectagnle2D):
    """
        Point1, Point2
    """
    def __init__(self, point1, point2):
        super().__init__(point1, point2)

class Segment2d(Figure2D):
    """
        Point1, Point2
    """
    def __init__(self, point1, point2):
        super().__init__(0, 0)
        self.Point1 = point1
        self.Point2 = point2

    def getArea(self):
        return 0
    def length(self):
        return self.Point1.distance(self.Point2)
