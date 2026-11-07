from dataclasses import dataclass
from cursodeportes.posicion_lv95 import PosicionLV95


@dataclass(eq=False)
class Parada:
    _parent_sloid_service_point: str
    _designation_official: str
    _posicion: PosicionLV95