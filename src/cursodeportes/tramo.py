from dataclasses import dataclass
from cursodeportes.geometria_tramo import GeometriaTramo


@dataclass
class Tramo:
    __uuid: str
    __geometria: GeometriaTramo