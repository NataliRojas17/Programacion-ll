import math
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
class Circulo:
    def __init__(self, c, r):
        self.c = c
        self.r = r
    def __str__(self):
        return f"Circulo con centro en {self.c} y radio {self.r}"
    def dibuja(self):
        print(f"Dibujando circulo con centro en {self.c} y radio {self.r}")
    def area(self):
        return math.pi * (self.r ** 2)
    def perimetro(self):
        return 2 * math.pi * self.r

centro = Punto(5, 10)
circulo = Circulo(centro, 65)
print(circulo)
circulo.dibuja()
print(f"Area: {circulo.area():.3f}")
print(f"Perimetro: {circulo.perimetro():.3f}")
