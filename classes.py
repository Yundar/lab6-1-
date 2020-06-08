import math


class Triangle:
    def __init__(self, side1, side2, angle):
        self.side1 = float(side1)
        self.side2 = float(side2)
        self.angle = float(angle)

    def perimeter(self):
        c = math.sqrt(
            self.side1 ** 2 + self.side2 ** 2 - 2 * self.side1 * self.side2 * math.cos(math.radians(self.angle)))
        p = c + self.side2 + self.side1
        return p

    def area(self):
        a = (self.side1 * self.side2 * math.sin(self.angle)) / 2
        return a


class RightTriangle(Triangle):
    def __init__(self, side1, side2, angle):
        super().__init__(side1, side2, angle)

    def perimeter(self):
        c = math.sqrt(self.side1 ** 2 + self.side2 ** 2)
        p = c + self.side2 + self.side1
        return p

    def area(self):
        a = self.side1 * self.side2 / 2


class EquilateralTriangle(Triangle):
    def __init__(self, side1, side2, angle):
        super().__init__(side1, side2, angle)

    def perimeter(self):
        p = self.side1 * 3
        return p

    def area(self):
        a = (self.side1 * math.sqrt(3)) / 4
        return a


class IsoscelesTriangle(Triangle):
    def __init__(self, side1, side2, angle):
        super().__init__(side1, side2, angle)

    def area(self): # Якщо вважати, що 1 з заданих сторін є основою рівнобедренного трикутника
        

t = IsoscelesTriangle(3, 4, 90)
print(t.perimeter())
