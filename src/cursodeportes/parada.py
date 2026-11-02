from dataclasses import dataclass
from cursodeportes.posicion_lv95 import PosicionLV95


@dataclass
class Parada:
    parentSloidServicePoint: str
    designationOfficial: str
    posicion: PosicionLV95