class Cola:
    def __init__(self, n):
        self.arreglo = [0] * n  
        self.inicio = 0
        self.fin = -1
        self.n = n
        self.cantidad = 0

    def insert(self, e):
        if not self.isFull():
            self.fin = (self.fin + 1) % self.n
            self.arreglo[self.fin] = e
            self.cantidad += 1

    def remove(self):
        if not self.isEmpty():
            valor = self.arreglo[self.inicio]
            self.inicio = (self.inicio + 1) % self.n
            self.cantidad -= 1
            return valor
        return None 

    def peek(self):
        if not self.isEmpty():
            return self.arreglo[self.inicio]
        return None 

    def isEmpty(self):
        return self.cantidad == 0

    def isFull(self):
        return self.cantidad == self.n

    def size(self):
        return self.cantidad

cola = Cola(6)
cola.insert(10)
cola.insert(20)
cola.insert(30)
print("Frente de la cola:", cola.peek())  
print("Elemento removido:", cola.remove())
print(cola.size())
print(cola.isFull())
print(cola.isEmpty())
