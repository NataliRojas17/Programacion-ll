from multimethod import multimethod

class LineaTeleferico:
    def __init__(self, color="", tramo="", nroCabinas=0, nroEmpleados=0):
        self.color = color
        self.tramo = tramo
        self.nroCabinas = nroCabinas
        self.nroEmpleados = nroEmpleados
        self.empleados = []  
        self.edades = []     
        self.sueldos = []    
    def agregar_empleado(self, nombre, paterno, materno, edad, sueldo):
        if self.nroEmpleados < 100:
            self.empleados.append([nombre, paterno, materno])
            self.edades.append(edad)
            self.sueldos.append(sueldo)
            self.nroEmpleados += 1    
    def __str__(self):
        cad = f"Color: {self.color}, Tramo: {self.tramo}, nroCabinas: {self.nroCabinas},nroEmpleados: {self.nroEmpleados}\n"
        cad += "Empleados:\n"
        for i in range(self.nroEmpleados):
            cad += f"  {self.empleados[i][0]} {self.empleados[i][1]} {self.empleados[i][2]} - Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}\n"
        return cad
    def eliminarPorApellido(self, apellido):
        i = 0
        while i < self.nroEmpleados:
            if self.empleados[i][1] == apellido or self.empleados[i][2] == apellido:
                self.empleados.pop(i)
                self.edades.pop(i)
                self.sueldos.pop(i)
                self.nroEmpleados -= 1
            else:
                i += 1
    def __add__(self, other_and_name):
        other, nombre = other_and_name
        if isinstance(other, LineaTeleferico):
            for i in range(self.nroEmpleados):
                if self.empleados[i][0].lower() == nombre.lower():
                    other.agregar_empleado(
                        self.empleados[i][0],
                        self.empleados[i][1],
                        self.empleados[i][2],
                        self.edades[i],
                        self.sueldos[i]
                    )
                    self.eliminar_empleado_por_indice(i)
                    break
        return other
    def eliminar_empleado_por_indice(self, idx):
        self.empleados.pop(idx)
        self.edades.pop(idx)
        self.sueldos.pop(idx)
        self.nroEmpleados -= 1

    def mayorEdad(self):
        return max(self.edades) if self.edades else None

    def mayorSueldo(self):
        return max(self.sueldos) if self.sueldos else None

    @multimethod
    def mostrar(self, edad: int):
        print("Empleados con mayor edad:")
        for i in range(self.nroEmpleados):
            if self.edades[i] == edad:
                print(f"  {self.empleados[i][0]} {self.empleados[i][1]} {self.empleados[i][2]} - Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}")

    @multimethod
    def mostrar(self, sueldo: float):
        print("Empleados con mayor sueldo:")
        for i in range(self.nroEmpleados):
            if self.sueldos[i] == sueldo:
                print(f"  {self.empleados[i][0]} {self.empleados[i][1]} {self.empleados[i][2]} - Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}")

t1 = LineaTeleferico("Rojo", "Estación Central - Cementerio - 16 de Julio", 20)
t2 = LineaTeleferico("Azul", "Estación Periférica - Estación Prado", 15)

t1.agregar_empleado("Pedro", "Rojas", "Luna", 35, 2500.0)
t1.agregar_empleado("Lucy", "Sosa", "Rios", 43, 3250.0)
t1.agregar_empleado("Ana", "Perez", "Rojas", 26, 2700.0)
t1.agregar_empleado("Saul", "Arce", "Calle", 29, 2500.0)

print("Linea Teleferico")
print(t1)

t1.eliminarPorApellido("Perez")
print("Eliminando por apellido...(Perez)")
print(t1)

t1 + (t2, "Saul")
print("Después de transferir a Saul de teleferico 1 a teleferico2:")
print("Teleférico 1:")
print(t1)
print("Teleférico 2:")
print(t2)

t1.mostrar(t1.mayorEdad())
t1.mostrar(t1.mayorSueldo())
