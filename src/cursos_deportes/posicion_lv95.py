from dataclasses import dataclass


@dataclass(frozen=True)
class PosicionLV95:
    lv95_east: float
    lv95_north: float