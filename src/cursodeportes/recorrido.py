from dataclasses import dataclass
from cursodeportes.tramo import PuntoLV95
from typing import Final

DISTANCIA_MAXIMA_PARADA_M: Final[float] = 500.0


@dataclass(frozen=True, eq=True)
class Recorrido:
    puntos: tuple[PuntoLV95, ...]
