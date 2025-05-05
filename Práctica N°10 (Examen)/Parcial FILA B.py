from multimethod import multimethod

class Ministerio:
    
    def __init__(self, nombre="", direccion="", nroEmpleados=4):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__nroEmpleados = nroEmpleados
        self.__empleados = [["Pedro Rojas Luna"],
                            ["Lucy Sosa Rios"],
                            ["Ana Perez Rojas"],
                            ["Saul Arce Calle"]]
        self.__edades = [35, 43, 26, 29]
        self.__sueldos = [2500.00, 3250.00, 2700.00, 2500.00]
    
    def __str__(self):
        cad = f"Nombre: {self.__nombre}, Dirección: {self.__direccion}, nroEmpleados: {self.__nroEmpleados}\n"
        cad += "Empleados:\n"
        for i in range(len(self.__empleados)):
            cad += f"Nombre: {self.__empleados[i][0]}, Edad: {self.__edades[i]}, Sueldo: {self.__sueldos[i]}\n"
        return cad

    def eliminarPorEdad(self, x):
        for i in range(len(self.__empleados) - 1, -1, -1):
            if self.__edades[i] == x:
                self.__empleados.pop(i)
                self.__edades.pop(i)
                self.__sueldos.pop(i)
                self.__nroEmpleados -= 1
    
    def __iadd__(self, parametros):
        otro, x = parametros      
        if isinstance(otro, Ministerio):
            for i in range(len(otro._Ministerio__empleados)):
                if otro._Ministerio__empleados[i][0].startswith(x):
                    nombre_completo = otro._Ministerio__empleados[i][0]
                    edad = otro._Ministerio__edades[i]
                    sueldo = otro._Ministerio__sueldos[i]
                    
                    self.__empleados.append([nombre_completo])
                    self.__edades.append(edad)
                    self.__sueldos.append(sueldo)
                    self.__nroEmpleados += 1
                    
                    otro._Ministerio__empleados.pop(i)
                    otro._Ministerio__edades.pop(i)
                    otro._Ministerio__sueldos.pop(i)
                    otro._Ministerio__nroEmpleados -= 1
                    
                    print(f"Empleado {nombre_completo} transferido de {otro._Ministerio__nombre} a {self.__nombre}.")
                    break
        
        return self

    def menorEdad(self):
        return min(self.__edades)
    
    def menorSueldo(self):
        return min(self.__sueldos)
    
    @multimethod
    def mostrar(self, e: int):
        cad = "Empleados con menor edad:\n"
        for i in range(len(self.__empleados)):
            if self.__edades[i] == e:
                cad += f"{self.__empleados[i][0]}, {self.__edades[i]} años\n"
        print(cad)
    
    @multimethod
    def mostrar(self, s: float):  
        cad = "Empleados con menor sueldo:\n"
        for i in range(len(self.__empleados)):
            if self.__sueldos[i] == s:
                cad += f"{self.__empleados[i][0]}, Sueldo: {self.__sueldos[i]} Bs\n"
        print(cad)


teleferico1 = Ministerio("Rojo", "Estación Central, Estación Cementerio, Estación 16 de Julio", 4)

teleferico2 = Ministerio("Morado", "Estación 6 de marzo, Estación Faro Murillo, Estación Obelisco", 3)
teleferico2._Ministerio__empleados = [["Omar Lopez Condori"], ["Laura Gomez Torrez"], ["Luis Vega Choque"]]
teleferico2._Ministerio__edades = [30, 28, 33]
teleferico2._Ministerio__sueldos = [2600, 2500, 2700]
print("Primer Ministerio:")
print(teleferico1)
print("Segundo Ministerio:")
print(teleferico2)

print("Eliminar empleados con edad 35:")
teleferico1.eliminarPorEdad(35)
print(teleferico1)

print("Transferencia de empleados:")
teleferico1 += (teleferico2, "Luis")
print("Después de transferencia:")
print(teleferico1)
print(teleferico2)

menEdad = teleferico1.menorEdad()
teleferico1.mostrar(menEdad)

menSueldo = teleferico1.menorSueldo()
teleferico1.mostrar(menSueldo)
