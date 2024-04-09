class Zanpakuto:
    def __init__(self, nombre, propietario):
        self.nombre = nombre
        self.propietario = propietario
        self.bankai_activado = False

    def activar_bankai(self):
        self.bankai_activado = True
        print(f"¡{self.propietario} ha activado su Bankai!")

    def obtener_nombre(self):
        return self.nombre

    def obtener_propietario(self):
        return self.propietario
