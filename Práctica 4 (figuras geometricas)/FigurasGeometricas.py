import math

class FigurasGeometricas:

    def area(self, *args):
        if len(args) == 1:  # Círculo
            radio = args[0]
            return math.pi * radio * radio
        
        elif len(args) == 2:  
            base, altura = args
            return base * altura  # Rectángulo
        
        elif len(args) == 3:
            if isinstance(args[1], float):  # Triángulo rectángulo
                b, h = args[0], args[1]
                return (b * h) / 2
            else:                           # Trapecio
                lado1, lado2, alto = args
                return ((lado1 + lado2) * alto) / 2
        
        elif len(args) == 2 and isinstance(args[0], float):  # Pentágono
            lado, apotema = args
            return (5 * lado * apotema) / 2
        
        else:
            raise ValueError("Parámetro no válido")
        

f = FigurasGeometricas()

print("Círculo:", f.area(3))
print("Rectángulo:", f.area(4, 6))
print("Triángulo Rectángulo:", f.area(5, 8.0))
print("Trapecio:", f.area(6, 4, 5))
print("Pentágono:", f.area(7.0, 3))
