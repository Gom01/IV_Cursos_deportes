from dataclasses import dataclass


@dataclass(frozen=True)
class PosicionLV95:
    __lv95_east: float
    __lv95_north: float