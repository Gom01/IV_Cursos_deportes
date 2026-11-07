from dataclasses import dataclass


@dataclass(frozen=True)
class PeticionRecorrido:
    __distancia: float
    __desnivel_positivo: float
    __parada_origen_id: str
    __parada_destino_id: str