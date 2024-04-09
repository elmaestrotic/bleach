from personaje import Personaje


class Shinigami(Personaje):
    def __init__(self, nombre, poder, habilidades, zanpakuto):
        super().__init__(nombre, poder, habilidades)
        self.zanpakuto = zanpakuto

    def obtener_zanpakuto(self):
        return self.zanpakuto
