
import math
from ssl import PROTOCOL_TLSv1_1

class Figure2D:
    def __init__(self):
        self.color = None

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

class Point2D(Figure2D):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

    def area(self):
        return 0

    def Mirror( self, p_0):
        return Point2D(p_0.x+(p_0.x-self.x), p_0.y+(p_0.y-self.y))

    def Belonging(self, p_0):
        if p_0.x == self.x and p_0.y == self.y:
            return "belong"



class Segment2D(Figure2D):
    def __init__(self, p_1, p_2):
        self.p1 = p_1
        self.p2 = p_2

    def area(self):
        return 0
        
    def distance(self):
        return math.sqrt((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2)


    def Mirror(self, p_0):
        Segment2D(p_0.mirror(self.p_1) , p_0.mirror(self.p_2))

    def Belonging(self, p_0):
        for X in range(self.p1.x,self.p2.x+1):
            if p_0.x == X:
                for Y in range(self.p1.y,self.p2.y+1):
                    if p_0.y == Y:
                        return "Belong"
    

class Triangle2D(Figure2D):
    def __init__(self, p_1, p_2, p_3):
        self.p1 = p_1
        self.p2 = p_2
        self.p3 = p_3
    
    def area(self):
        l12 = self.p1.distance(self.p2)
        l13 = self.p1.distance(self.p3)
        l23 = self.p2.distance(self.p3)
        pp = (l12 + l13 + l23) / 2.0
        return math.sqrt(pp * (pp - l12) * (pp - l13) * (pp - l23))

    def Mirror(self, p_0):
        return  Triangle2D(p_0.mirror(self.p_1) , p_0.mirror(self.p_2) , p_0.mirror(self.p_3))

    def Belonging(self, p_0):
        for X in range(min(self.p1.x,self.p2.x, self.p3.x),max(self.p1.x,self.p2.x, self.p3.x)):
            if p_0.x == X:
                for Y in range(min(self.p1.y,self.p2.y, self.p3.y),max(self.p1.y,self.p2.y, self.p3.y)):
                    if p_0.y == Y:
                        if p_0.x*p_0.y <= self.area:
                            return "Belong"
                 
class Trapezoid2D(Figure2D):
     def __init__(self, p_1, p_2, p_3, p_4):
        self.p1 = p_1
        self.p2 = p_2
        self.p3 = p_3
        self.p4 = p_4
    
     def area(self):
        MAX = 0
        d_1 = 0
        d_2 = 0
        A_1 = [self.p1.distance(self.p2),self.p1, self.p2]
        B_1 = [self.p1.distance(self.p3),self.p1, self.p3]
        C_1 = [self.p1.distance(self.p4),self.p1, self.p4]
        A_2 = [self.p2.distance(self.p1),self.p2, self.p1]
        B_2 = [self.p2.distance(self.p3),self.p2, self.p3]
        C_2 = [self.p2.distance(self.p4),self.p2, self.p4]
        A_3 = [self.p3.distance(self.p2),self.p3, self.p2]
        B_3 = [self.p3.distance(self.p1),self.p3, self.p1]
        C_3 = [self.p3.distance(self.p4),self.p3, self.p4]
        A_4 = [self.p4.distance(self.p2),self.p4, self.p2]
        B_4 = [self.p4.distance(self.p3),self.p4, self.p3]
        C_4 = [self.p4.distance(self.p1),self.p4, self.p1]
        Otrezki = [A_1, B_1, C_1,A_2, B_2, C_2, A_3, B_3, C_3, A_4, B_4, C_4]
        for i in range(len(Otrezki)):
            if i >= MAX:
                MAX = Otrezki[i][0]
                d_1 == i

        for i in range(len(Otrezki)):
            if i != d_1:
                if i >= MAX:
                    MAX = Otrezki[i]
                    d_2 == i

        return 0.5*d_1*d_2*math.acos((math.sqrt(((Otrezki[d_1][1].x -Otrezki[d_1][2].x) * (Otrezki[d_2][1].x -Otrezki[d_2][2].x))**2 + ((Otrezki[d_1][1].y -Otrezki[d_1][2].y) * (Otrezki[d_2][1].y -Otrezki[d_2][2].y))**2)/(math.sqrt((Otrezki[d_1][1].x -Otrezki[d_1][2].x)**2 + (Otrezki[d_1][1].y - Otrezki[d_1][2].y)**2) * (Otrezki[d_2][1].x -Otrezki[d_2][2].x)**2 + (Otrezki[d_2][1].y -Otrezki[d_2][2].y)**2)))
        
        
     def Mirror(self, p_0):
         return Rectangle2D(p_0.mirror(self.p_1) ,p_0.mirror(self.p_2) ,p_0.mirror(self.p_3) ,p_0.mirror(self.p_4) )

     def Belonging(self, p_0):
         for X in range(min(self.p1.x,self.p2.x, self.p3.x),max(self.p1.x,self.p2.x, self.p3.x)):
             if p_0.x == X:
                 for Y in range(min(self.p1.y,self.p2.y, self.p3.y),max(self.p1.y,self.p2.y, self.p3.y)):
                     if p_0.y == Y:
                         if p_0.x*p_0.y <= self.area:
                             return "Belong"
     
class Rectangle2D(Figure2D):
    def __init__(self, p_1, p_2, p_3, p_4):
        self.p1 = p_1
        self.p2 = p_2
        self.p3 = p_3
        self.p4 = p_4


    def area(self):
        MAX = 0
        d_1 = 0
        d_2 = 0
        A_1 = [self.p1.distance(self.p2),self.p1, self.p2]
        B_1 = [self.p1.distance(self.p3),self.p1, self.p3]
        C_1 = [self.p1.distance(self.p4),self.p1, self.p4]
        A_2 = [self.p2.distance(self.p1),self.p2, self.p1]
        B_2 = [self.p2.distance(self.p3),self.p2, self.p3]
        C_2 = [self.p2.distance(self.p4),self.p2, self.p4]
        A_3 = [self.p3.distance(self.p2),self.p3, self.p2]
        B_3 = [self.p3.distance(self.p1),self.p3, self.p1]
        C_3 = [self.p3.distance(self.p4),self.p3, self.p4]
        A_4 = [self.p4.distance(self.p2),self.p4, self.p2]
        B_4 = [self.p4.distance(self.p3),self.p4, self.p3]
        C_4 = [self.p4.distance(self.p1),self.p4, self.p1]
        Otrezki = [A_1, B_1, C_1,A_2, B_2, C_2, A_3, B_3, C_3, A_4, B_4, C_4]
        for i in range(len(Otrezki)):
            if i >= MAX:
                MAX = Otrezki[i][0]
                d_1 == i

        for i in range(len(Otrezki)):
            if i != d_1:
                if i >= MAX:
                    MAX = Otrezki[i]
                    d_2 == i

        return 0.5*d_1*d_2*math.acos((math.sqrt(((Otrezki[d_1][1].x -Otrezki[d_1][2].x) * (Otrezki[d_2][1].x -Otrezki[d_2][2].x))**2 + ((Otrezki[d_1][1].y -Otrezki[d_1][2].y) * (Otrezki[d_2][1].y -Otrezki[d_2][2].y))**2)/(math.sqrt((Otrezki[d_1][1].x -Otrezki[d_1][2].x)**2 + (Otrezki[d_1][1].y - Otrezki[d_1][2].y)**2) * (Otrezki[d_2][1].x -Otrezki[d_2][2].x)**2 + (Otrezki[d_2][1].y -Otrezki[d_2][2].y)**2)))
        
   
    def Belonging(self, p_0):
         for X in range(min(self.p1.x,self.p2.x, self.p3.x),max(self.p1.x,self.p2.x, self.p3.x)):
             if p_0.x == X:
                 for Y in range(min(self.p1.y,self.p2.y, self.p3.y),max(self.p1.y,self.p2.y, self.p3.y)):
                     if p_0.y == Y:
                         if p_0.x*p_0.y <= self.area:
                             return "Belong"
     

    def Mirror(self, p_0):
         return Rectangle2D(p_0.mirror(self.p_1) ,p_0.mirror(self.p_2) ,p_0.mirror(self.p_3) ,p_0.mirror(self.p_4) )

class Square2D(Figure2D):
     def __init__(self, p_1, p_2, p_3, p_4):
        self.p1 = p_1
        self.p2 = p_2
        self.p3 = p_3
        self.p4 = p_4

     def area(self):
        l12 = self.p1.distance(self.p2)
        l13 = self.p1.distance(self.p3)
        if l12 >= l13:
            return l13*l13

     def Mirror(self, p_0):
         return Rectangle2D(p_0.mirror(self.p_1) ,p_0.mirror(self.p_2) ,p_0.mirror(self.p_3) ,p_0.mirror(self.p_4) )

     def Belonging(self, p_0):  
            if p_0.x >= min(self.p1.x, self.p2.x, self.p3.x, self.p4.x) and p_0.x <= max(self.p1.x, self.p2.x, self.p3.x, self.p4.x):
                if p_0.y >= min(self.p1.y, self.p2.y, self.p3.y, self.p4.y) and p_0.x <= max(self.p1.y, self.p2.y, self.p3.y, self.p4.y):
                    return "Belong"

class Circle2D(Figure2D):
    def __init__(self, p_1, R):
        self.p1 = p_1
        self.r = R

    def area(self):
         return 3.14159265359*self.r*self.r
    
    def Mirror(self, p_0):
          return Circle2D(p_0.mirror(self.p_1), self.r.distance(self.p1))

    def Belonging(self, p_0):  
        R = self.r.distance(self.p1)
        if p_0.x >= self.p1.x - self.r.x and p_0.x <= self.p1.x + self.r.x:
            if math.sqrt(p_0.x**2 + p_0.y**2) <= R**2:
                return "Belong"



