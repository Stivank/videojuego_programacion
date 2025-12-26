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
orco = Orco()
arpia = Arpia()
boss = Oscar()

"""
# Prueba de las habilidades de los personajes. Funcionan, pero a veces imprimen frases que no quiero. Revisar.
guerrero = Guerrero("Cadalas")
print(f"Primer combate: \n¡{guerrero.nombre} se va a enfrentar a un {orco.nombre}!\nVida {orco.nombre}: {orco.vida}")
while guerrero.esta_vivo() and orco.esta_vivo():
    print("1- Atacar\n2- Defender\n3- Habilidad especial")
    opcion = ""
    while opcion != range(1,4):
        opcion = input(f"¿Qué va a hacer {guerrero.nombre}? ")
        match opcion:
            case "1":
                guerrero.atacar(orco)
            case "2":
                guerrero.defender(orco)
            case "3":
                guerrero.habilidad_especial(orco)
            case _:
                print(f"{guerrero.nombre} no sabe hacer eso.")
                opcion = input(f"¿Qué va a hacer {guerrero.nombre}?")
    if orco.vida <= 60:
        orco.habilidad_especial() # Habría que pasar el personaje como parámetro una vez modificada la función en la clase Orco.
    orco.atacar()




# Pruebas para ver si las pociones funcionan. La poción tiene el método tomar_pocion, recibe un personaje y modifica directamente sus atributos según el tipo de poción.
print("Vida antes:", guerrero.vida)
vida.tomar_pocion(guerrero)
print("Vida después:", guerrero.vida)
"""

# Mira si te parece bien este tipo de menú para el combate, si quieres tocarlo hazlo.

def combate(personaje, enemigo) -> bool:
    print(f"\n¡{personaje.nombre} se enfrenta a {enemigo.nombre}!")
    print(f"Vida {enemigo.nombre}: {enemigo.vida}")

    while personaje.esta_vivo() and enemigo.esta_vivo():
        print("\n--¿Qué quieres hacer?--")
        print("1- Atacar")
        print("2- Defender")
        print("3- Habilidad especial")
        print("---------------------------")
        
        opcion = input(f"¿Qué va a hacer {personaje.nombre}? ")

        match opcion:
            case "1":
                personaje.atacar(enemigo)
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
        if enemigo.vida <= 60:
            enemigo.habilidad_especial()

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
            return

    print("\n¡Has derrotado a todos los enemigos! ¡Victoria!")


if __name__ == "__main__":
    iniciar_juego()