class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio =precio
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
p2 = Pintura("Mona Lisa", "óleo", [a2], "Retrato")
print(f"Pintura 1: {p1.titulo}, con anuncio: {p1.anuncio.numero}, Precio: {p1.anuncio.precio}")
print(f"Pintura 2: {p2.titulo}, sin anuncio: {p2.anuncio}")

# Inciso (b)
def artista_mas_experimentado(pinturas):
    return max((art for p in pinturas for art in p.artistas), key=lambda a: a.experiencia).nombre
print("Artista con más experiencia:", artista_mas_experimentado([p1, p2]))
# Inciso (c)
p2.anuncio = Anuncio(9, 1050)
total = p1.anuncio.precio + p2.anuncio.precio
print(f"Anuncio agregado a {p2.titulo}, nuevo total de venta: {total}")
