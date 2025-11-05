from dataclasses import dataclass, field
from typing import List, TYPE_CHECKING

from src.core.models.area.area import Area
from src.core.models.owner.owner import Owner
from src.core.models.zone.zone import Zone

@dataclass
class Bus:
    
    id                  : int
    name                : str
    zone                : Zone
    area                : Area
    owner               : Owner
    base_voltage        : float = 138.0
    voltage_pu          : float = 1.0
    voltage_angle       : float = 0
    normal_vmax_pu      : float = 1.05
    normal_vmin_pu      : float = 0.95
    emergency_vmax_pu   : float = 1.05
    emergency_vmin_pu   : float = 0.92


