from dataclasses import dataclass, field
from cursodeportes.parada import Parada
from cursodeportes.tramo import Tramo


@dataclass(eq=True)
class RedSenderos:
    _paradas: dict[str, Parada] = field(compare=False)
    _tramos: dict[str, Tramo] = field(compare=False)
