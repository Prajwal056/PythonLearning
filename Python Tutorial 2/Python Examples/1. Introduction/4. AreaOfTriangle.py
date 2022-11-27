
from cmath import *
class square_root:     #parent class
    def __init__(self,f,s,t):
        self.f = f
        self.s = s
        self.t = t

    def is_valid(self):
        if self.f or self.s or self.t <= 0:
            print("Error !! Please enter a valid side")
    def check_all_sides(self):
        if self.f + self.s <= self.t or self.f + self.t <= self.s or self.s + self.t <= self.f <= self.f:
            print("Error !! Sides are not valid")           
    def solution(self):
        s = (self.f+self.s+self.t) / 2
        area = sqrt(s * (s - self.f) * (s - self.s) * (s - self.t))
        print(area)

b = square_root(5,4,3)
b.is_valid()
b.check_all_sides()
b.solution()
if b.is_valid()
       