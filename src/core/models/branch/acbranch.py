from dataclasses import dataclass, field

from src.core.models.bus.bus import Bus
from src.utils.type_hints import TwoCharString

"""
We will create from bus and to bus attributes from bus one and bus two, and these will always be in ascending order. We will follow this format in all tools.
"""

@dataclass
class ACBranch:

    bus_one :   Bus
    bus_two :   Bus
    ckt_id  :   TwoCharString
    ##ternmianl data
    r       : float = 0.00
    x 