from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class SystemBase:
    mva: float = 100.0   # PSSE default; keep explicit for clarity
