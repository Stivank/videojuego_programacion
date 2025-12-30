# Archivo principal del videojuego

from guerrero import Guerrero
from mago import Mago
from ladron import Ladron

from orco import Orco
from arpia import Arpia
from oscar import Oscar

import pocion

vida = pocion.Pocion("Recuperación de vida", 10)
daño = pocion.Pocion("Daño", 10)
escudo = pocion.Pocion("Escudo", 10)

"""
# Pruebas para ver si las pociones funcionan. La poción tiene el método tomar_pocion, recibe un personaje y modifica directamente sus atributos según el tipo de poción.
print("Vida antes:", guerrero.vida)
vida.tomar_pocion(guerrero)
print("Vida después:", guerrero.vida)
"""

# Mira si te parece bien este tipo de menú para el combate, si quieres tocarlo hazlo.
# Notas:
# - En mis clases, debo revisar los feedbacks. Devuelven frases repetidas o que no se deberían mostrar en determinados momentos. La función 'defender()' es la que dice cosas más raras.
# - Pendiente implementar pociones. Al avanzar de combate, el personaje no tiene vida suficiente y muere en seguida.
# - El trabajo de Stivan funciona estupendo. Tal vez pueda revisar sus clases para ver cómo implementar el feedback en las mías.
# - Tal vez haya que hacer que las pociones recuperen más vida

def combate(personaje, enemigo) -> bool:
    contador_habilidad_enemigo = 0
    print(f"\n¡{personaje.nombre} se enfrenta a {enemigo.nombre}!")
    print(f"Vida {enemigo.nombre}: {enemigo.vida}")

    while personaje.esta_vivo() and enemigo.esta_vivo():
        print("\n--¿Qué quieres hacer?--") # Redundante si se va a preguntar lo mismo más adelante.
        print("1- Atacar")
        print("2- Defender")
        print("3- Habilidad especial")
        print("---------------------------")
        
        opcion = input(f"¿Qué va a hacer {personaje.nombre}? ")

        match opcion:
            case "1":
                personaje.atacar(enemigo)
                print(f"El guerrero {personaje.nombre} ataca con su espada.")
            case "2":
                personaje.defender(enemigo)
            case "3":
                personaje.habilidad_especial(enemigo)
            case _:
                print(f"{personaje.nombre} no sabe hacer eso.")
                continue

        # Si el enemigo muere, termina el combate
        if not enemigo.esta_vivo():
            print(f"\n{enemigo.nombre} ha sido derrotado.")
            return True

        # Habilidad especial del enemigo (ejemplo: cuando baja de la mitad)
        # La habilidad especial del enemigo se acumulaba cada turno. Añado una variable para hacer que solo actúe una vez.
        if enemigo.vida <= 60 and contador_habilidad_enemigo == 0:
            enemigo.habilidad_especial()
            contador_habilidad_enemigo = 1

        # Turno del enemigo
        enemigo.atacar(personaje)

    return personaje.esta_vivo()
                
def iniciar_juego():
    # Prueba de combate completo
    personaje = Guerrero("Cadalas")

    enemigos = [Orco(), Arpia(), Oscar()]

    for enemigo in enemigos:
        gana = combate(personaje, enemigo)
        if not gana:
            print("\nGAME OVER.")
            return # ?

    print("\n¡Has derrotado a todos los enemigos! ¡Victoria!")

if __name__ == "__main__":
    iniciar_juego()