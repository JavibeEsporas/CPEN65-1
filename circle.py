import math
class Circle:
    def __init__(self, pi, r):
        self.pi = math.pi           #Using built in math.pi
        self.r = r

    def Area(self):
        print("Area of Circle =", self.pi * self.r ** 2)  #Formula for Area of Circle: πr^2


circ = Circle(math.pi, 8) 
circ.Area()

