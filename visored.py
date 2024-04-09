from shinigami import Shinigami
from hollow import Hollow

class Visored(Shinigami, Hollow):
    def __init__(self, nombre, poder, habilidades, zanpakuto, mascara):
        Shinigami.__init__(self, nombre, poder, habilidades, zanpakuto)
        Hollow.__init__(self, nombre, poder, habilidades, mascara)
