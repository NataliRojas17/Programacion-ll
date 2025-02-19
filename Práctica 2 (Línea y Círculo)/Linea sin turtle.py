class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def __str__(self):
        return f"Línea p1 {self.p1} y linea p2{self.p2}"
    def dibuja_linea(self):
        print(f"Dibujando desde p1 {self.p1} hasta p2 {self.p2}")
punto1 = Punto(0, 5)
punto2 = Punto(50, 35)
linea = Linea(punto1, punto2)
print(linea)
linea.dibuja_linea()
