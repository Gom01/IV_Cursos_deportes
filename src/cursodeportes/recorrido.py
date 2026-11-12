from dataclasses import dataclass
from cursodeportes.punto_lv95 import PuntoLV95
from typing import Final

DISTANCIA_MAXIMA_PARADA_M: Final[float] = 500.0


@dataclass(frozen=True, eq=True)
class Recorrido:
    _tramos_ids: tuple[str, ...]
