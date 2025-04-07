import tkinter as tk
from tkinter import messagebox
import random

class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = 3

    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas

    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas, ventana):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = None
        self.ventana = ventana

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        self.mostrar_interfaz()

    def mostrar_interfaz(self):
        self.ventana.title("Juego Adivina el Número")
        self.entrada_usuario = tk.Entry(self.ventana)
        self.entrada_usuario.pack(pady=10)

        self.boton_adivinar = tk.Button(self.ventana, text="Adivinar", command=self.adivinar)
        self.boton_adivinar.pack(pady=10)

        self.mensaje = tk.Label(self.ventana, text="Adivina el número entre 0 y 10:", font=("Arial", 16))
        self.mensaje.pack(pady=18)

    def adivinar(self):
        numero_usuario = self.entrada_usuario.get()
        if numero_usuario.isdigit():  
            numero_usuario = int(numero_usuario)
            if numero_usuario == self.numeroAAdivinar:
                messagebox.showinfo("¡Acertaste!!", "¡Acertaste! Has adivinado el número.")
                self.actualizaRecord()
                self.ventana.quit()
            else:
                if not self.quitaVida():
                    self.mensaje.config(text="Te has quedado sin vidas.")
                    messagebox.showinfo("Game Over", "Te has quedado sin vidas.")
                    self.ventana.quit()
                else:
                    if numero_usuario < self.numeroAAdivinar:
                        self.mensaje.config(text=f"El número es mayor. Tienes {self.numeroDeVidas} vidas restantes."
                                            if self.numeroDeVidas > 0 else "Te has quedado sin vidas.")
                    else:
                        self.mensaje.config(text=f"El número es menor. Tienes {self.numeroDeVidas} vidas restantes."
                                            if self.numeroDeVidas > 0 else "Te has quedado sin vidas.")
        else:
            messagebox.showwarning("Entrada no válida", "Por favor, ingresa un número válido.")

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def __init__(self, numeroDeVidas, ventana):
        super().__init__(numeroDeVidas, ventana)

    def valida_numero(self, numero):
        if numero % 2 == 0: 
            return True
        else:
            messagebox.showwarning("Número no válido", "El número debe ser par y estar entre 0 y 10.")
            return False

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.choice([0, 2, 4, 6, 8, 10]) 
        self.mostrar_interfaz()

    def adivinar(self):
        numero_usuario = self.entrada_usuario.get()
        if numero_usuario.isdigit():
            numero_usuario = int(numero_usuario)
            if self.valida_numero(numero_usuario):
                if numero_usuario == self.numeroAAdivinar:
                    messagebox.showinfo("¡Acertaste!", "¡Acertaste! Has adivinado el número par.")
                    self.actualizaRecord()
                    self.ventana.quit()
                else:
                    if not self.quitaVida():
                        self.mensaje.config(text="Te has quedado sin vidas.")
                        messagebox.showinfo("Game Over", "Te has quedado sin vidas.")
                        self.ventana.quit()
                    else:
                        if numero_usuario < self.numeroAAdivinar:
                            self.mensaje.config(text=f"El número es mayor. Tienes {self.numeroDeVidas} vidas restantes."
                                                if self.numeroDeVidas > 0 else "Te has quedado sin vidas.")
                        else:
                            self.mensaje.config(text=f"El número es menor. Tienes {self.numeroDeVidas} vidas restantes."
                                                if self.numeroDeVidas > 0 else "Te has quedado sin vidas.")
        else:
            messagebox.showwarning("Entrada no válida", "Por favor, ingresa un número válido.")

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self, numeroDeVidas, ventana):
        super().__init__(numeroDeVidas, ventana)

    def valida_numero(self, numero):
        if numero % 2 != 0:
            return True
        else:
            messagebox.showwarning("Número no válido", "El número debe ser impar y estar entre 0 y 10.")
            return False

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.choice([1, 3, 5, 7, 9])  
        self.mostrar_interfaz()

    def adivinar(self):
        numero_usuario = self.entrada_usuario.get()
        if numero_usuario.isdigit():
            numero_usuario = int(numero_usuario)
            if self.valida_numero(numero_usuario):
                if numero_usuario == self.numeroAAdivinar:
                    messagebox.showinfo("¡Acertaste!", "¡Acertaste! Has adivinado el número impar.")
                    self.actualizaRecord()
                    self.ventana.quit()
                else:
                    if not self.quitaVida():
                        self.mensaje.config(text="Te has quedado sin vidas.")
                        messagebox.showinfo("Game Over", "Te has quedado sin vidas.")
                        self.ventana.quit()
                    else:
                        if numero_usuario < self.numeroAAdivinar:
                            self.mensaje.config(text=f"El número es mayor. Tienes {self.numeroDeVidas} vidas restantes."
                                                if self.numeroDeVidas > 0 else "Te has quedado sin vidas.")
                        else:
                            self.mensaje.config(text=f"El número es menor. Tienes {self.numeroDeVidas} vidas restantes."
                                                if self.numeroDeVidas > 0 else "Te has quedado sin vidas.")
        else:
            messagebox.showwarning("Entrada no válida", "Por favor, ingresa un número válido.")

def main():
    ventana = tk.Tk()

    juego1 = JuegoAdivinaNumero(3, ventana)
    juego2 = JuegoAdivinaPar(3, ventana)
    juego3 = JuegoAdivinaImpar(3, ventana)

    boton_juego1 = tk.Button(ventana, text="Jugar Adivina el Número", command=juego1.juega)
    boton_juego1.pack(pady=10)

    boton_juego2 = tk.Button(ventana, text="Jugar Adivina un Número Par", command=juego2.juega)
    boton_juego2.pack(pady=10)

    boton_juego3 = tk.Button(ventana, text="Jugar Adivina un Número Impar", command=juego3.juega)
    boton_juego3.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()
