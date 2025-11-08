from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import math
from src.core.value_objects.system_base import SystemBase
from src.core.value_objects.voltage_level import VoltageLevel



@dataclass(frozen=True, slots=True)
class BranchImpedancePU:
    """Series impedance and shunt charging in per-unit on (Base.mva, Base.kv)."""
    r_pu: float        # series R
    x_pu: float        # series X
    b_pu: float        # total shunt B (line charging), sign per your convention

    def z_pu(self) -> complex:
        return complex(self.r_pu, self.x_pu)

    def y_sh_pu(self) -> complex:
        # PSSE convention: total B; each end has B/2 (susceptance, jB). Here we store B only.
        return 1j * self.b_pu

    @staticmethod
    def from_per_km(
        r_ohm_per_km: float,
        x_ohm_per_km: float,
        b_s_per_km: float,        # siemens per km (total line charging per km)
        length_km: float,
        voltage: VoltageLevel,
        sys_base: SystemBase
    ) -> "BranchImpedancePU":
        # Per-unit conversions on the specified base.
        z_base = (voltage.kv ** 2) / sys_base.mva  # ohms (kV^2/MVA) with kV in kV, MVA in MVA
        y_base = 1 / z_base                  # siemens
        r = r_ohm_per_km * length_km / z_base
        x = x_ohm_per_km * length_km / z_base
        b = b_s_per_km * length_km / y_base
        return BranchImpedancePU(r_pu=r, x_pu=x, b_pu=b)

    def to_psse_tuple(self) -> tuple[float, float, float]:
        """Return (R, X, B) ready for a PSSE branch record (per-unit, total B)."""
        return (self.r_pu, self.x_pu, self.b_pu)
    
@dataclass(frozen=True, slots=True)
class EndShuntPU:
    """
    Optional per-end shunts, in per-unit (conductance G and susceptance B).
    If not provided, G_from=G_to=0 and B_from=B_to defaults to b_total/2.
    """
    g_from_pu: float = 0.0
    b_from_pu: float = 0.0
    g_to_pu: float   = 0.0
    b_to_pu: float   = 0.0

    def as_tuple(self) -> tuple[complex, complex]:
        y_from = complex(self.g_from_pu, self.b_from_pu)
        y_to   = complex(self.g_to_pu,   self.b_to_pu)
        return y_from, y_to
    



