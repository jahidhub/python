"""
Write a class “Calculator” capable of finding square, cube and square root of a
number.
"""


class calculator:

    def __init__(self, n):
        self.no = n

    def square(self):
        print(f"This is the square of this number: {self.no *self.no}")

    def cube(self):
        print(f"This is the cube of this number: {self.no *self.no*self.no}")

    def square_root(self):
        print(f"This is the square of this number: {self.no**1/2}")


num = calculator(5)
num.square()
num.cube()
num.square_root()