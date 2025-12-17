
from personaje import Personaje

class Ladron(Personaje):
    def __init__(self, nombre, rol, vida, daño, nivel):
        super().__init__(nombre, rol, vida, daño, nivel)