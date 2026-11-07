from dataclasses import dataclass
from cursodeportes.tramo import Tramo
from typing import Final

DISTANCIA_MAXIMA_PARADA_M: Final[float] = 500.0

@dataclass(frozen=True)
class Recorrido:
    _tramos: tuple[Tramo, ...]