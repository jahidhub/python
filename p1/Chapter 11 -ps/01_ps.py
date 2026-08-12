"""Create a class (2-D vector) and use it to create another class representing a 3-D
vector."""


class twoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def showing(self):
        print(f"This vector is {self.i} + {self.j}")


class threeDVector(twoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def showing(self):
        print(f"This vector is {self.i}i + {self.j}j , {self.k}k")


two = twoDVector(1, 2)
two.showing()
three = threeDVector(1, 2, 3)
three.showing()
