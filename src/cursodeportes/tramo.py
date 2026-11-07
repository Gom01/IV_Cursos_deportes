from dataclasses import dataclass
from cursodeportes.geometria_tramo import GeometriaTramo


@dataclass(eq=False)
class Tramo:
    _uuid: str
    _geometria: GeometriaTramo