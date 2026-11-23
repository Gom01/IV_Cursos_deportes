from dataclasses import dataclass
from typing import Final



@dataclass(frozen=True, eq=True)
class Recorrido:
    _tramos_ids: tuple[str, ...]
