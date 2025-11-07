from dataclasses import dataclass, field

from src.core.models.area.area import Area
from src.core.models.bus.bus import Bus
from src.core.models.owner.owner import Owner
from src.core.models.zone.zone import Zone
from src.utils.type_hints import TwoCharString

@dataclass
class Load:
    
    id                      : TwoCharString
    bus                     : Bus
    zone                    : Zone
    area                    : Area
    owner                   : Owner
    mw                      : float = 0.0
    mvar                    : float = 0.0
    ip                      : float = 0.0
    iq                      : float = 0.0
    yp                      : float = 0.0
    yq                      : float = 0.0
    distributed_gen_p       : float = 0.0
    distributed_gen_q       : float = 0.0
    distributed_gen_status  : bool = False
    status                  : bool = True
    scalable                : bool = False
    interruptible           : bool = False
    grounding_flag          : bool = False
    p_neg                   : float = 0.00
    q_neg                   : float = 0.00
    p_zero                  : float = 0.00
    q_zero                  : float = 0.00
    type                    : str = ''