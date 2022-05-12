import math

class Figure2D:
    def __init__(self):
        self.colour = None

    def set_colour(self,colour):
        self.colour = colour

    def get_colour(self):
        return self.colour

class Point2D(Figure2D):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

    def area(self):
        return 0

    def mirror_point(self, p0):
        return Point2D(p0.x + p0.x - self.x, p0.y + p0.y - self.y)

    def lineMirror_point(self,)

class Segment2D(Figure2D):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        return 0
    
    def distance(self):
        return self.p1.distance(self.p2)

    def mirror_point(self, p0):
        return Segment2D(p0.mirror_point(self.p1),p0.mirror_point(self.p2))

class Trapeze2D(Figure2D):
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def area(self):
        l12 = self.p1.distance(self.p2)
        l23 = self.p2.distance(self.p3)
        l34 = self.p3.distance(self.p4)
        l41 = self.p4.distance(self.p1)
        pp = (l12 + l34 + l23 + l41) / 2.0
        return math.sqrt(pp*(pp-l12)*(pp-l23)*(pp-l34)*(pp-l41))

    def mirror_point(self, p0):
        return Trapeze2D(p0.mirror_point(self.p1),p0.mirror_point(self.p2),p0.mirror_point(self.p3),p0.mirror_point(self.p4))

class Rectangle(Trapeze2D):
    def __init__(self, p1, p2, p3, p4):
        super().__init__(p1, p2, p3, p4)

    def area(self):
        return self.p1.distance(self.p2) * self.p2.distance(self.p3)

    def mirror_point(self, p0):
        return Rectangle(p0.mirror_point(self.p1),p0.mirror_point(self.p2),p0.mirror_point(self.p3),p0.mirror_point(self.p4))

class Triangle2D(Figure2D):
    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        l12 = self.p1.distance(self.p2)
        l13 = self.p1.distance(self.p3)
        l23 = self.p2.distance(self.p3)
        pp = (l12 + l13 + l23) / 2.0
        return math.sqrt(pp*(pp-l12)*(pp-l13)*(pp-l23))

    def mirror_point(self, p0):
        return Triangle2D(p0.mirror_point(self.p1),p0.mirror_point(self.p2),p0.mirror_point(self.p3))

class Circle2D(Figure2D):
    def __init__(self,p1,R):
        self.p1 = p1
        self.R = R



f = Figure2D()
f.set_colour("Terraria")

p1 = Point2D(0, 0)
p2 = Point2D(1, 0)
p3 = Point2D(0, 1)
p4 = Point2D(1, 1)


P = p4.mirror_point(p2)
x = P.x
y = P.y
print(x,y)

t = Triangle2D(p1, p2, p3)
a = t.area()
print(t)

R = Rectangle(p1, p2, p4, p3)
A = R.area()
print(A)

