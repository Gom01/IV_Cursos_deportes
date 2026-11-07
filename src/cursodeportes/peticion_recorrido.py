from dataclasses import dataclass
from typing import Final

MARGEN_DISTANCIA_KM: Final[float] = 1.0
MARGEN_DESNIVEL_M: Final[float] = 50.0

@dataclass(frozen=True)
class PeticionRecorrido:
    _distancia: float
    _desnivel_positivo: float
    _parada_origen_id: str
    _parada_destino_id: str