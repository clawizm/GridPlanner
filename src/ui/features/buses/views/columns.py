from src.ui.kits.grids.columns import ColumnDef

BusColumns = [
    ColumnDef("id", "ID", accessor=lambda r: r.id, width=70, align="right"),
    ColumnDef("name", "Name", accessor=lambda r: r.name, stretch=True),
    ColumnDef("kv", "kV", accessor=lambda r: r.kv, align="right"),
    ColumnDef("zone", "Zone", accessor=lambda r: r.zone),
    ColumnDef("owner", "Owner", accessor=lambda r: r.owner),
]
