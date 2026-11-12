from dataclasses import dataclass
from cursodeportes.posicion_lv95 import PosicionLV95


@dataclass(frozen=True)
class Parada:
    _nombre: str
    _posicion: PosicionLV95
