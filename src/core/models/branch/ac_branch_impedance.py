from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import math

# ---------- Value objects (core/domain/values/...) ----------

@dataclass(frozen=True, slots=True)
class Base:
    kv: float          # nominal line-to-line kV
    mva: float         # system MVA base (PSSE base, e.g., 100 MVA)

@dataclass(frozen=True, slots=True)
class LinePU:
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
        base: Base
    ) -> "LinePU":
        # Per-unit conversions on the specified base.
        z_base = (base.kv ** 2) / base.mva  # ohms (kV^2/MVA) with kV in kV, MVA in MVA
        y_base = 1 / z_base                  # siemens
        r = r_ohm_per_km * length_km / z_base
        x = x_ohm_per_km * length_km / z_base
        b = b_s_per_km * length_km / y_base
        return LinePU(r_pu=r, x_pu=x, b_pu=b)

    def to_psse_tuple(self) -> tuple[float, float, float]:
        """Return (R, X, B) ready for a PSSE branch record (per-unit, total B)."""
        return (self.r_pu, self.x_pu, self.b_pu)

@dataclass(frozen=True, slots=True)
class LineSeqPU:
    """Optional: positive/zero-sequence split, still per-unit on (Base.mva, Base.kv)."""
    z1_pu: complex
    z0_pu: complex
    b1_pu: float
    b0_pu: float

    def to_positive_only(self) -> LinePU:
        return LinePU(self.z1_pu.real, self.z1_pu.imag, self.b1_pu)

# ---------- Entity (core/domain/entities/...) ----------

@dataclass(slots=True)
class ACLine:
    bus_i: int
    bus_j: int
    ckt_id: str
    base: Base
    imp: LinePU                 # store the value object
    rate_a_mva: Optional[float] = None
    rate_b_mva: Optional[float] = None
    rate_c_mva: Optional[float] = None
    in_service: bool = True
    name: Optional[str] = None
    owner_id: Optional[int] = None

    # Convenience properties for PSSE-style consumers:
    @property
    def r(self) -> float: return self.imp.r_pu
    @property
    def x(self) -> float: return self.imp.x_pu
    @property
    def b(self) -> float: return self.imp.b_pu

    def psse_tuple(self) -> tuple[int, int, str, float, float, float]:
        return (self.bus_i, self.bus_j, self.ckt_id, *self.imp.to_psse_tuple())
