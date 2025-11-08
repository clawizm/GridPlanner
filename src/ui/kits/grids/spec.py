from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

@dataclass
class QuerySpec:
    
    filters: Dict[str, Any] = field(default_factory=dict)
    sort: List[Tuple[str, str]] = field(default_factory=list)  # [("kv","desc")]
    page: int = 1
    page_size: int = 200
