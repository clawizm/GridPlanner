from dataclasses import dataclass, field

from src.core.models.bus.bus import Bus
from src.utils.type_hints import TwoCharString
from src.core.value_objects.branch_impedance import BranchImpedancePU, EndShuntPU

"""
We will create from bus and to bus attributes from bus one and bus two, and these will always be in ascending order. We will follow this format in all tools.
We don't need to pass voltage to this object, we should puull it from the buses.
"""

@dataclass
class ACBranch:

    bus_one     :   Bus
    bus_two     :   Bus
    ckt_id      :   TwoCharString
    ##ternmianl data
    impedance   :   BranchImpedancePU
    end_shunt   :   EndShuntPU
    status      :   bool
    metered     :   bool
    

    @property
    def r(self) -> float: return self.impedance.r_pu
    @property
    def x(self) -> float: return self.impedance.x_pu
    @property
    def b(self) -> float: return self.impedance.b_pu

@dataclass(slots=True)
class ACLine:
    bus_i: int
    bus_j: int
    ckt_id: str
    impedance: LinePU                 # store the value object
    rate_a_mva: Optional[float] = None
    rate_b_mva: Optional[float] = None
    rate_c_mva: Optional[float] = None
    in_service: bool = True
    name: Optional[str] = None
    owner_id: Optional[int] = None

    # Convenience properties for PSSE-style consumers:


    def psse_tuple(self) -> tuple[int, int, str, float, float, float]:
        return (self.bus_i, self.bus_j, self.ckt_id, *self.imp.to_psse_tuple())