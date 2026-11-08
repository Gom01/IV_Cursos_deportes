from dataclasses import dataclass
from cursodeportes.punto_lv95 import PuntoLV95
from typing import Final

MIN_PUNTOS_GEOMETRIA: Final[int] = 2

@dataclass(eq=False)
class Tramo:
    _uuid: str
    _geometria: tuple[PuntoLV95, ...]