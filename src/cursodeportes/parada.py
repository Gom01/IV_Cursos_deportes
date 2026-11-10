from dataclasses import dataclass, field
from cursodeportes.posicion_lv95 import PosicionLV95


@dataclass(eq=True)
class Parada:
    _identificador: str
    _nombre: str = field(compare=False)
    _posicion: PosicionLV95 = field(compare=False)
