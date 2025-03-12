import math

class FigurasGeometricas:
    def area(self, *args):
        if len(args) == 1:
            radio = args[0]
            return math.pi * radio * radio   # circulo
        elif len(args) == 2:
            if isinstance(args[0], float) and isinstance(args[1], float):
                b, h = args
                return (b * h) / 2     # triangulo rectángulo 
            else:
                if isinstance(args[0], int) and isinstance(args[1], float):
                    lado, apotema = args
                    return ((5 * lado) * apotema) / 2   #pentagono
                else:
                    if isinstance(args[0], int) and isinstance(args[1], int):
                        b, h = args
                        return b * h    #rectángulo 
        elif len(args) == 3:
            l1, l2, h = args
            return ((l1 + l2) * h) / 2  #trapecio
        else:
            raise ValueError("Parámetro no válido")
f = FigurasGeometricas()

print("Círculo: ", f.area(3))
print("Rectángulo: ", f.area(4, 6)) 
print("Triángulo Rectángulo: ", f.area(5.0, 9.0))  
print("Trapecio: ", f.area(8, 3, 5))  
print("Pentágono: ", f.area(9, 4.5))
