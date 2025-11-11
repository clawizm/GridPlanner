from typing import Sequence
from src.ui.kits.grids.spec import QuerySpec
from src.ui.kits.grids.datasource import QueryPort

def _apply_filters(q, f):
    if v := f.get("name_contains"):
        q = q.where(Bus.name.ilike(f"%{v}%"))
    if v := f.get("kv_between"):
        lo, hi = v
        q = q.where(Bus.kv.between(lo, hi))
    if v := f.get("zone"):
        q = q.where(Bus.zone == v)
    if v := f.get("owner_in"):
        q = q.where(Bus.owner.in_(v))
    return q

def _apply_sort(q, sort):
    mapping = {
        "id": Bus.id,
        "name": Bus.name,
        "kv": Bus.kv,
        "zone": Bus.zone,
        "owner": Bus.owner,
    }
    order = []
    for key, direction in sort or [("id","asc")]:
        col = mapping.get(key)
        if not col: 
            continue
        order.append(col.asc() if direction == "asc" else col.desc())
    return q.order_by(*order)

class BusRowDTO:
    __slots__ = ("id","name","kv","zone","owner")
    def __init__(self, id:int, name:str, kv:float, zone:str, owner:str):
        self.id, self.name, self.kv, self.zone, self.owner = id, name, kv, zone, owner

class BusQuery(QueryPort):
    def __init__(self, bus_repo):
        self.bus_repo = bus_repo  # app-layer port

    def count(self, spec: QuerySpec) -> int:
        return self.bus_repo.count(filters=spec.filters)

    def fetch(self, spec: QuerySpec) -> Sequence[BusRowDTO]:
        rows = self.bus_repo.search(
            filters=spec.filters,
            sort=spec.sort,
            limit=spec.page_size,
            offset=(spec.page - 1) * spec.page_size,
            columns=["id","name","kv","zone","owner"],
        )
        return [BusRowDTO(**r) for r in rows]
