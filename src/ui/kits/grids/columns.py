from dataclasses import dataclass
from typing import Callable, Any, Optional

Accessor = Callable[[Any], Any]
Formatter = Callable[[Any], str]

@dataclass(frozen=True)
class ColumnDef:
    key: str
    header: str
    accessor: Accessor           # row -> value
    formatter: Optional[Formatter] = None
    width: int = 120
    align: str = "left"          # "left" | "right" | "center"
    stretch: bool = False

def value_of(col: ColumnDef, row: Any) -> str:
    v = col.accessor(row)
    return col.formatter(v) if (col and col.formatter) else ("" if v is None else str(v))
