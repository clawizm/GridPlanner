from dataclasses import dataclass, field
from src.core.value_objects.voltage_level import VoltageLevel
from typing import Union
from numbers import Number

@dataclass
class Rating:
    """
    Represents any rating. Either *mva* or *amps* must be provided,
    and the other is computed from the *voltage* provided.
    """
    voltage : VoltageLevel
    _mva    : int = field(init=False, repr=False)
    _amps   : int = field(init=False, repr=False)

    def __init__(self,
                 voltage: VoltageLevel,
                 *,
                 mva: Union[int, None] = None,
                 amps: Union[int, None] = None):
        self.voltage = voltage
        if (mva is None) and (amps is None):
            raise ValueError("Specify exactly one of MVA or AMPS")
        if mva is None:
            self.amps = amps
        else:
            self.mva = mva

    @classmethod
    def from_mva_and_amps(cls, mva: int, amps: int):
        kv = get_kv_from_mva_and_amps(mva, amps)
        return Rating(voltage=kv, mva=mva, amps=amps)
    
    @amps.setter
    def amps(self, value: int):
        if not isinstance(value, Number):
            raise TypeError(f"Please provide a number for amps, not type: {value}")
        self._amps = value
        self._mva = convert_amps_to_mva(value, self.voltage)
        return 
    
    @property
    def mva(self)->Union[int, None]:
        return self._mva
    
    @mva.setter
    def mva(self, value: int):
        if not isinstance(value, Number):
            raise TypeError(f"Please provide a number for mva, not type: {value}")
        self._mva = value
        self._mva = convert_mva_to_amps(value, self.voltage)
        return
    
    def __repr__(self):
        return f"(kV={self.voltage}, amps={self.amps}, mva={self.mva})"

class Ratings:
    
    rate1   :   Rating
    rate2   :   Rating
    rate3   :   Rating
    rate4   :   Rating
    rate5   :   Rating
    rate6   :   Rating
    rate7   :   Rating
    rate8   :   Rating
    rate9   :   Rating
    rate10  :   Rating
    rate11  :   Rating
    rate12  :   Rating
