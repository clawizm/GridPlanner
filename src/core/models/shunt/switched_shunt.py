from dataclasses import dataclass, field
from typing import Literal, Annotated
from enum import IntEnum

from src.core.models.bus.bus import Bus
from src.core.models.area.area import Area
from src.core.models.owner.owner import Owner
from src.core.models.zone.zone import Zone
from src.utils.type_hints import TwoCharString, TenItemListLimit

class AdjustmentMethod(IntEnum):

    """
    Adjustment Methods.

    - 0 = Sequential Input Order
    - 1 = Nearest Combination
    """

    SEQUENTIAL_INPUT_ORDER = 0
    NEAREST_COMBINATION = 1 

    def describe(self)->str:
        """Human-readable explanation for the status."""
        explantions = {
            self.SEQUENTIAL_INPUT_ORDER: 'Adjust using Sequential Input Order',
            self.NEAREST_COMBINATION: 'Adjust using Nearest Combination'
        }
        return explantions[self]
    

class ControlMode(IntEnum):

    """
    Operational States.

    - 0 = Locked
    - 1 = Discrete Control Voltage
    - 2 = Continuous Control Voltage
    - 3 = Discrete Control Plant (Mvar)
    - 4 = Discrete Control VSC Conv (Mvar)
    - 5 = Discrete Control Remote SWS (Mvar)
    - 6 = Discrete Control Shunt Element (Mvar)
    """
    
    LOCKED = 0
    DISCRETE_CNTRL_VOLTAGE = 1
    CONTINUOUS_CONTRL_VOLTAGE = 2
    DISCRETE_C0NTRL_PLANT = 3 
    DISCRETE_CONTRL_VSC_CONV = 4
    DISCRETE_CONTRL_REMOTE_SWS = 5
    DISCRETE_CONTRL_SHUNT_ELEM = 6

    def describe(self)->str:
        """Human-readable explanation for the status."""
        explantions = {
            self.LOCKED: 'This shunt is locked and will not add/remove blocks from service.',
            self.DISCRETE_CNTRL_VOLTAGE: 'This Shunt is a Discrete Voltage Controlling Device.'
        }
        return explantions[self]

@dataclass
class SwitchedShuntBlock:

    status: bool = False
    steps: int = 0
    size: int = 0

@dataclass
class SwitchedShunt:

    id: TwoCharString
    bus: Bus
    area: Area
    zone: Zone
    code: int = 1
    status: bool = True
    control_mode: ControlMode = ControlMode(1)
    adjustment_method: AdjustmentMethod = AdjustmentMethod(0) 
    v_hi: float = 1.03
    h_low: float = 0.95
    contributed_percentage: float = 1
    regulated_bus: Bus = None
    name: str = ''
    b_init: float = 0.00
    # blocks: TenItemListLimit = field(default_factory=lambda: [0] * 10)
