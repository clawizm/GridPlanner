from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class VoltageLevel:
    kv: float            # nominal L-L kV for that equipment/bus
