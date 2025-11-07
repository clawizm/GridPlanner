from dataclasses import dataclass, field
from typing import List, TYPE_CHECKING

from src.core.models.area.area import Area
from src.core.models.bus.bus import Bus
from src.core.models.owner.owner import Owner
from src.core.models.zone.zone import Zone
from src.utils.type_hints import TwoCharString
from src.core.value_objects.percentage import Percentage
"""
The desired voltage magnitude (in p.u.) at the generator’s terminal or at its regulating bus, 
depending on how the generator’s excitation control is configured.
"""
 
"""
base (Machine Base MVA) is the MVA base of the generator itself — 
the rating used internally for per-unit (p.u.) calculations of that particular machine’s electrical quantities 
(currents, voltages, reactances, etc.).

resistance is the per-unit Thevenin (or source) resistance of the generator’s internal voltage source, on the machine’s own MBASE.
reactance is the per-unit Thevenin (or source) reactance of the generator’s internal voltage source, on the machine’s own MBASE.

transformer_resistance is the per-unit resistance of the generator’s step-up transformer (on the machine’s MBASE). 
It represents the real (lossy) component of the transformer impedance between the generator terminal and the system bus.

transformer_reactance is the per-unit resistance of the generator’s step-up transformer (on the machine’s MBASE). 
It represents the imaginary (reactive) component of the transformer impedance between the generator terminal and the system bus.

gentap is the per-unit tap ratio of the generator’s step-up transformer, 
used by GridPlanner to scale voltages and impedances between the generator terminals and the system bus.
A value of 1.0 means nominal tap; 
values above or below 1.0 simulate the transformer’s tap-changer effect on generator voltage and reactive power flow.
"""
@dataclass
class GeneratorOwner:
    """Represents an owner of a Generator Unit

    Parameters
    ----------
    owner : Owner
        An instance of Owner indicating the ID and name of this GeneratorOwner
    percentage : Percentage
        The percentage of the unit that the owner owns.
    """
    owner: Owner
    percentage: Percentage


@dataclass
class Generator:
    """This is a test class for dataclasses.

    This is the body of the docstring description.

    Parameters
    ---
    id : TwoCharString 
        A two character unique ID used to identify this Generator. (Can not be the same as any IDs of other Generators at this Bus)
    bus : Bus
        The bus this generator is located at.
    zone : Zone
        The zone this generator belongs to.
    area : Area
        The area this generator belongs to.
    ref_voltage : float
        The desired voltage magnitude (in p.u.) at the generator’s terminal or at its regulating bus, 
        depending on how the generator’s excitation control is configured.
    regulator_bus : Bus
        The bus that this generator is trying to control the voltage of. 
        The ref_voltage is the desired voltage of this bus, which the generator is trying to control.
    status : bool
        The in-service state of this generator.
    p_gen : float
        The current Real Power that this generator is outputing.
    p_max : float
        The max Real Power this generator can output.
    p_min : float
        The min Real Power this generator can output.
    q_gen : float
        The current Reactive Power that this generator is outputing.
    q_max : float
        The max Reactive Power this generator can output.
    q_min : float
        The min Reactive Power this generator can output.
    base : float
        base (Machine Base MVA) is the MVA base of the generator itself — 
        the rating used internally for per-unit (p.u.) calculations  
        (currents, voltages, reactances, etc.).
    internal_resistance : float
        resistance is the per-unit Thevenin (or source) resistance of the 
        generator’s internal voltage source, on the machine’s own MBASE.
    internal_reactance : float
        reactance is the per-unit Thevenin (or source) reactance of the 
        generator’s internal voltage source, on the machine’s own MBASE.
    transformer_resistance : float
        transformer_resistance is the per-unit resistance of the generator’s step-up transformer (on the machine’s MBASE). 
        It represents the real (lossy) component of the transformer impedance between the generator terminal and the system bus.
    transformer_reactance : float
        transformer_reactance is the per-unit resistance of the generator’s step-up transformer (on the machine’s MBASE). 
        It represents the imaginary (reactive) component of the transformer impedance between the generator terminal and the system bus.
    gentap : float
        gentap is the per-unit tap ratio of the generator’s step-up transformer, 
        used by GridPlanner to scale voltages and impedances between the generator terminals and the system bus.
        A value of 1.0 means nominal tap; 
        values above or below 1.0 simulate the transformer’s tap-changer effect on generator voltage and reactive power flow.
    owners : list[GeneratorOwner]
        
    """

    id      : TwoCharString
    bus                     : Bus
    zone                    : Zone
    area                    : Area
    ref_voltage : float = 1.00
    regulator_bus   : Bus
    status : bool = True
    p_gen : float = 0.00
    p_max : float = 0.00
    p_min : float = 0.00
    q_gen : float = 0.00
    q_max : float = 0.00    
    q_min : float = 0.00
    base : float = 0.00 
    internal_resistance: float = 0.00
    internal_reactance: float = 0.00
    transformer_resistance: float = 0.0
    transformer_reactance: float = 0.0
    gentap: float = 1.00
    owners: list[GeneratorOwner] = field(default_factory=list)
    subtransient_x: float = 0.00
    transient_x: float = 0.00
    synchronous_x: float = 0.00
    r_negative: float = 0.00
    x_negative: float = 0.00
    r_zero : float = 0.00
    x_zero : float = 0.00
    grounding_z : float = 0.00
    grounding_r : float = 0.00
    grounding_x : float = 0.00
    reference_angle : float = 0.00

    #base again?
    #machine: types!
    #renewable machine!
    # voltage droop?



Generator(owners=)