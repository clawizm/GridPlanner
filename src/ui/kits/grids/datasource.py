from typing import Protocol, Sequence, Tuple, Any, List
from .spec import QuerySpec

class QueryPort(Protocol):
    def count(self, spec: QuerySpec) -> int: ...
    def fetch(self, spec: QuerySpec) -> Sequence[Any]: ...

class GridDataSource:
    def __init__(self, query: QueryPort):
        self.query = query
        self.spec = QuerySpec()
        self.total = 0
        self.rows: Sequence[Any] = []

    def refresh(self):
        self.total = self.query.count(self.spec)
        self.rows = self.query.fetch(self.spec)

    def set_filters(self, **filters):
        self.spec.filters.update(filters)
        self.spec.page = 1
        self.refresh()

    def set_sort(self, *sort_pairs: Tuple[str, str]):
        self.spec.sort = list(sort_pairs)
        self.refresh()

    def goto_page(self, page: int):
        self.spec.page = max(1, page)
        self.refresh()

    @property
    def page_info(self) -> Tuple[int, int, int]:
        return (self.spec.page, self.spec.page_size, self.total)
