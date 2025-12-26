from enemigo import Enemigo

class Arpia(Enemigo):
    def __init__(self, nombre: str = "Arpía", vida: int = 90, daño: int = 20, nivel: int = 1) -> None:
        super().__init__(nombre, vida, daño, nivel)

    def atacar(self, personaje) -> None: #Voy a hacer tambien sin returns innecesarios
        # Ataca al personaje y le quita vida según el daño de la arpía
        personaje.recibir_daño(self.daño)
        print(f"La arpía {self.nombre} ataca desde el aire con sus garras.")
        print(f"{personaje.nombre}: {personaje.vida}")

    def habilidad_especial(self) -> None:
        # Se cura un poco para aguantar más
        self.vida += 10
        print(f"La arpía {self.nombre} se eleva y recupera 10 de vida.")
        print(f"{self.nombre}: {self.vida}")
