from dataclasses import dataclass
from src.core.models.zone.zone import Zone
from src.core.models.area.area import Area
from src.core.models.owner.owner import Owner

@dataclass
class SubSystem:

    zone: Zone
    area: Area
    owner: Owner
