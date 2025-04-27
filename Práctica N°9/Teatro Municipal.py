import tkinter as tk
from PIL import Image, ImageTk

class Boleto:
    def __init__(self, numero, precio = 0.0):
        self.numero = numero
        self.precio = precio

    def mostrar(self):
        return f"Número: {self.numero}, Precio: {self.precio:.1f}"

class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 100.0

class Platea(Boleto):
    def __init__(self, numero, dias):
        super().__init__(numero)
        self.precio = 50.0 if dias >= 10 else 60.0

class Galeria(Boleto):
    def __init__(self, numero, dias):
        super().__init__(numero)
        self.precio = 25.0 if dias >= 10 else 30.0

def vender():
    tipo_boleto = tipo.get()
    try:
        numero = int(entrada_numero.get())
        dias = int(entrada_dias.get()) if tipo_boleto != "Palco" else 0

        if tipo_boleto == "Palco":
            boleto = Palco(numero)
        elif tipo_boleto == "Platea":
            boleto = Platea(numero, dias)
        elif tipo_boleto == "Galeria":
            boleto = Galeria(numero, dias)
        else:
            resultado.config(text="Seleccione un tipo de boleto.")
            return

        resultado.config(text=f"Número: {boleto.numero}, Precio: {boleto.precio:.1f} bs.")
    except ValueError:
        resultado.config(text="Datos inválidos. Ingrese números válidos.")

ventana = tk.Tk()
ventana.title("Teatro Municipal Achá")
ventana.geometry("480x460")
ventana.resizable(False, False)

frame_superior = tk.LabelFrame(ventana, text="", padx=12, pady=12, bg="white")
frame_superior.pack(padx=10, pady=5, fill="x")

tk.Label(frame_superior, text="Teatro Municipal Achá", fg= "navy", anchor="center", font=("Rockwell", 18, "bold"), width=20, bg="white").pack(side="left")

try:
    img = Image.open("Teatro_Acha.jpg")  
    img = img.resize((120, 80))
    foto = ImageTk.PhotoImage(img)
    lbl_img = tk.Label(frame_superior, image=foto)
    lbl_img.image = foto
    lbl_img.pack(side="right")
except:
    tk.Label(frame_superior, text="[Sin imagen]").pack(side="right")
frame_datos = tk.LabelFrame(ventana, text="Datos del Boleto", font=("Rockwell", 12, "bold"), padx=10, pady=10)
frame_datos.pack(padx=10, pady=5, fill="x")
frame_botons = tk.Frame(frame_datos)
frame_botons.grid(row=0, column=0, columnspan=2, pady=5)

tipo = tk.StringVar()
tk.Radiobutton(frame_botons, text="Palco", variable=tipo, value="Palco", width=10, height=2, font=("Rockwell", 11)).grid(row=0, column=0, padx=5)
tk.Radiobutton(frame_botons, text="Platea", variable=tipo, value="Platea", width=10, height=2, font=("Rockwell", 11)).grid(row=0, column=1, padx=5)
tk.Radiobutton(frame_botons, text="Galeria", variable=tipo, value="Galeria", width=10, height=2, font=("Rockwell", 11)).grid(row=0, column=2, padx=5)

tk.Label(frame_datos, text="Número:", font=("Rockwell", 12)).grid(row=1, column=0, pady=5, sticky='w')
entrada_numero = tk.Entry(frame_datos, width=15, bg="#e0eff5")
entrada_numero.grid(row=1, column=1, pady=5, sticky='w')

tk.Label(frame_datos, text="Cant. Días para el Evento:", font=("Rockwell", 12)).grid(row=2, column=0, pady=5, sticky='w')
entrada_dias = tk.Entry(frame_datos, width=15, bg="#e0eff5")
entrada_dias.grid(row=2, column=1, pady=5, sticky='w')

frame_datos.grid_columnconfigure(0, weight=0)
frame_datos.grid_columnconfigure(1, weight=1)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=20)
tk.Button(frame_botones, text="Vender", font=("Rockwell", 11), bg="#dde9ed", width=10, command=vender).grid(row=0, column=0, padx=20)
tk.Button(frame_botones, text="Salir", font=("Rockwell", 11), bg="#dde9ed", width=10, command=ventana.destroy).grid(row=0, column=1, padx=20)

frame_info = tk.LabelFrame(ventana, text="Información", font=("Rockwell", 12, "bold"), padx=10, pady=10)
frame_info.pack(padx=10, pady=5, fill="x")
resultado = tk.Label(frame_info, text="", font=("Rockwell", 16), fg="blue")
resultado.pack()
ventana.mainloop()
