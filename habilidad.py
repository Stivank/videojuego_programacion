from abc import ABC, abstractmethod

# CAMBIOS RECIENTES (2026-01-02)
# - Ajustado interfaz para que coincidan:
#   atacar(self, enemigo) -> None, defender(self) -> bool, habilidad_especial(self, enemigo) -> None

class Habilidad(ABC):
    @abstractmethod
    def atacar(self, enemigo) -> None:
        pass

    @abstractmethod
    def defender(self) -> bool:
        pass

    @abstractmethod
    def habilidad_especial(self, enemigo) -> None:
        pass
