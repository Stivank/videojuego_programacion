from enemigo import Enemigo

class Orco(Enemigo):
    def __init__(self, nombre: str = "Orco", vida: int = 120, daño: int = 25, nivel: int = 1) -> None:
        super().__init__(nombre, vida, daño, nivel)

    def atacar(self, personaje) -> None: #Voy a hacer tambien sin returns innecesarios
        # El orco pega al personaje
        personaje.recibir_daño(self.daño)
        print(f"El orco {self.nombre} ataca con su garrote.")
        print(f"{personaje.nombre}: {personaje.vida}")

    def habilidad_especial(self) -> None:
        # Se enfurece: sube daño
        self.daño += 5
        print(f"El orco {self.nombre} entra en furia y aumenta su daño en +5.")
        print(f"Daño actual del orco: {self.daño}")
