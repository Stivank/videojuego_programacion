from enemigo import Enemigo

class Oscar(Enemigo):
    def __init__(self, nombre: str = "Óscar (Jefe final)", vida: int = 200, daño: int = 35, nivel: int = 3) -> None:
        super().__init__(nombre, vida, daño, nivel)

    def atacar(self, personaje) -> None: #Voy a hacer tambien sin returns innecesarios
        # El jefe ataca más fuerte
        personaje.recibir_daño(self.daño)
        print(f"{self.nombre} lanza un ataque devastador.")
        print(f"{personaje.nombre}: {personaje.vida}")

    def habilidad_especial(self) -> None:
        # Entra en "fase 2": sube nivel y daño
        self.nivel += 1
        self.daño += 10
        print(f"{self.nombre} entra en fase 2: nivel +1 y daño +10.")
        print(f"Nivel: {self.nivel} | Daño: {self.daño}")
