'''Add a static method in problem 2, to greet the user with hello'''


class calculator:

    def __init__(self, n):
        self.no = n

    def square(self):
        print(f"This is the square of this number: {self.no *self.no}")

    def cube(self):
        print(f"This is the cube of this number: {self.no *self.no*self.no}")

    def square_root(self):
        print(f"This is the square of this number: {self.no**1/2}")

    @staticmethod
    def static_greet():
        print("hello there!")

num = calculator(5)
num.square()
num.cube()
num.square_root()
num.static_greet()
