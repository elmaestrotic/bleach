from personaje import Personaje


class Hollow(Personaje):
    def __init__(self, nombre, poder, habilidades, mascara):
        super().__init__(nombre, poder, habilidades)
        self.mascara = mascara

    def obtener_mascara(self):
        return self.mascara
