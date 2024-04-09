class Personaje:
    def __init__(self, nombre, poder, habilidades):
        self.nombre = nombre
        self.poder = poder
        self.habilidades = habilidades

    def obtener_nombre(self):
        return self.nombre

    def obtener_poder(self):
        return self.poder

    def obtener_habilidades(self):
        return self.habilidades

    def agregar_habilidad(self, habilidad):
        self.habilidades.append(habilidad)

    def eliminar_habilidad(self, habilidad):
        if habilidad in self.habilidades:
            self.habilidades.remove(habilidad)
