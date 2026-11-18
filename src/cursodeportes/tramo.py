from dataclasses import dataclass
from typing import Final
from cursodeportes.posicion_lv95 import PosicionLV95


MIN_PUNTOS_TRAMO: Final[int] = 2


@dataclass(frozen=True)
class Tramo:
    _puntos: tuple[PosicionLV95, ...]
