from dataclasses import dataclass


@dataclass(frozen=True)
class PosicionLV95:
    _lv95_east: float
    _lv95_north: float