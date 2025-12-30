
from habilidad import Habilidad
from personaje import Personaje
import pocion
from enemigo import Enemigo

class Guerrero(Personaje, Habilidad):
    def __init__(self, nombre: str, rol: str = "Ataque melé", vida: int = 110, daño: int = 30, nivel: int = 1) -> None:
        super().__init__(nombre, rol, vida, daño, nivel)

    def atacar(self, enemigo) -> None: # Voy a quitar todos los returns innecesarios
        enemigo.recibir_daño(self.daño) # Estoy metiendo estas nuevas líneas para ver si puedo enlazar los ataques de uno con el daño recibido de otro
        print(f"El guerrero {self.nombre} ataca con su espada.")

    def defender(self, enemigo) -> None:
        self.recibir_daño(-enemigo.daño) # Pruebas para ver cómo implementamos la defensa
        enemigo.daño = 0
        print(f"El guerrero {self.nombre} se defiende con su escudo.")
        # Tal vez pueda trastear con booleanos para ver si con eso se implementa mejor

    def habilidad_especial(self, enemigo) -> None:
        print(f"¡El guerrero {self.nombre} se carga de rabia!")
        self.daño += 10
        self.atacar(enemigo) # Llama a la función 'atacar'
        self.daño -= 10 # Devuelve el daño a su valor inicial después de un ataque especial