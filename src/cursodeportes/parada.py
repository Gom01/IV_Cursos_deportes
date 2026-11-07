from dataclasses import dataclass
from cursodeportes.posicion_lv95 import PosicionLV95


@dataclass
class Parada:
    __parent_sloid_service_point: str
    __designation_official: str
    __posicion: PosicionLV95