from dataclasses import dataclass, field
from cursodeportes.parada import Parada
from cursodeportes.tramo import Tramo
from typing import Final

MARGEN_DISTANCIA_KM: Final[float] = 1.0
MARGEN_DESNIVEL_M: Final[float] = 50.0
DISTANCIA_MAXIMA_PARADA_M: Final[float] = 500.0



@dataclass
class RedSenderos:
    _paradas: frozenset[Parada] 
    _tramos: frozenset[Tramo] 
