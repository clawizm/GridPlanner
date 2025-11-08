from typing import Sequence
from src.ui.kits.grids.spec import QuerySpec
from src.ui.kits.grids.datasource import QueryPort

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
