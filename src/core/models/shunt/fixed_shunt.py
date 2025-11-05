from dataclasses import dataclass, field

from src.core.models.bus.bus import Bus
from src.core.models.area.area import Area
from src.core.models.owner.owner import Owner
from src.core.models.zone.zone import Zone
from src.utils.type_hints import TwoCharString

@dataclass
class FixedShunt:

    id: TwoCharString
    bus: Bus
    area: Area
    zone: Zone
    g_shunt: float = 0.00 
    b_shunt: float = 0.00 
    g_zero: float = 0.00 
    b_zero: float = 0.00 
    code: int = 1
    status: bool = True
