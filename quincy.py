from personaje import Personaje


class Quincy(Personaje):
    def __init__(self, nombre, poder, habilidades, arco):
        super().__init__(nombre, poder, habilidades)
        self.arco = arco

    def obtener_arco(self):
        return self.arco
