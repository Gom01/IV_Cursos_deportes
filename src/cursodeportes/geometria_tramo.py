from dataclasses import dataclass
from cursodeportes.punto_lv95 import PuntoLV95
from typing import Final

MIN_PUNTOS_GEOMETRIA: Final[int] = 2

@dataclass(frozen=True)
class GeometriaTramo:
    __puntos: tuple[PuntoLV95, ...]