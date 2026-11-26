from dataclasses import dataclass
from typing import Final
from cursodeportes.tramo import Tramo



@dataclass(frozen=True, eq=True)
class Recorrido:
    _tramos_recorrido: tuple[Tramo, ...]
