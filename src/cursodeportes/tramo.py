from dataclasses import dataclass
from typing import Final
from cursodeportes.punto_lv95 import PuntoLV95


MIN_PUNTOS_TRAMO: Final[int] = 2


@dataclass(frozen=True)
class Tramo:
    _puntos: tuple[PuntoLV95, ...]
