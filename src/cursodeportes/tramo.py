from dataclasses import dataclass
from cursodeportes.geometria_tramo import GeometriaTramo


@dataclass
class Tramo:
    uuid: str
    geometria: GeometriaTramo