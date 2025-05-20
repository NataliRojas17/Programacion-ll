class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio

class Artista:
    def __init__(self, nombre, ci, experiencia):
        self.nombre = nombre
        self.ci = ci
        self.experiencia = experiencia

class Obra:
    def __init__(self, titulo, material, artistas, anuncio=None):
        self.titulo = titulo
        self.material = material
        self.artistas = artistas
        self.anuncio = anuncio

class Pintura(Obra):
    def __init__(self, titulo, material, artistas, genero, anuncio=None):
        super().__init__(titulo, material, artistas, anuncio)
        self.genero = genero

# Inciso (a)
a1 = Artista("Vincent van Gogh", "1359984", 32)
a2 = Artista("Leonardo Da Vinci", "207922", 47)
p1 = Pintura("La Noche Estrellada", "óleo", [a1], "Naturalismo", Anuncio(18, 1200))
p2 = Pintura("La Última Cena", "óleo y tempera", [a2], "Religioso", Anuncio(2, 1259))
print(f"Pintura 1: {p1.titulo}, Anuncio: {p1.anuncio.numero}, Precio: {p1.anuncio.precio}")
print(f"Pintura 2: {p2.titulo}, Anuncio: {p2.anuncio.numero}, Precio: {p2.anuncio.precio}")

# Inciso (b)
def promedio_experiencia(pinturas):
    experiencias = [art.experiencia for p in pinturas for art in p.artistas]
    return sum(experiencias) / len(experiencias)
print("Promedio de experiencia de los artistas:", promedio_experiencia([p1, p2]))

# Inciso (c)
def incrementar_precio(pinturas, nombre, x):
    for p in pinturas:
        if any(nombre in art.nombre for art in p.artistas) and p.anuncio:
            p.anuncio.precio += x

incrementar_precio([p1, p2], "Vincent", 500)
print(f"Nuevo precio de la pintura de Vincent ({p1.titulo}): {p1.anuncio.precio}")
