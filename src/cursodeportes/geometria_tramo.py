from dataclasses import dataclass
from cursodeportes.punto_lv95 import PuntoLV95


@dataclass(frozen=True)
class GeometriaTramo:
    puntos: tuple[PuntoLV95, ...]