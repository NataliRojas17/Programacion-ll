class Pila:
    def __init__(self, n):
        self.arreglo = [0] * n  
        self.top = -1
        self.n = n

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.arreglo[self.top] = e

    def long_pop(self):
        if not self.isEmpty():
            valor = self.arreglo[self.top]
            self.top -= 1
            return valor
        return None 

    def long_peek(self):
        if not self.isEmpty():
            return self.arreglo[self.top]
        return None  

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.n - 1

pila = Pila(5)
pila.push(20)
pila.push(10)
pila.push(30)
print("Tope de la pila:", pila.long_peek()) 
print("Elemento desapilado:", pila.long_pop())
