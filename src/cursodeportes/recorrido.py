from dataclasses import dataclass
from cursodeportes.tramo import Tramo


@dataclass(frozen=True)
class Recorrido:
    __tramos: tuple[Tramo, ...]