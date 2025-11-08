from PySide6 import QtWidgets, QtCore
from typing import List
from .columns import ColumnDef
from .datasource import GridDataSource
from .model_qt import GridModel

class QtGridBinder:
    """Owns QTableView + model + proxy; exposes .reload() and simple helpers."""
    def __init__(self, table: QtWidgets.QTableView, columns: List[ColumnDef], ds: GridDataSource):
        self.table = table
        self.ds = ds
        self.model = GridModel(ds, columns, parent=table)
        self.proxy = QtCore.QSortFilterProxyModel(table)
        self.proxy.setSourceModel(self.model)
        self.proxy.setSortRole(QtCore.Qt.ItemDataRole.UserRole)
        self.proxy.setFilterCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)

        table.setModel(self.proxy)
        table.setSortingEnabled(True)
        table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        table.horizontalHeader().setStretchLastSection(False)
        table.verticalHeader().setVisible(False)

        # Apply column widths
        for i, c in enumerate(columns):
            if c.stretch:
                table.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
            else:
                table.setColumnWidth(i, c.width)

        # Resort will call back into model via proxy; you can intercept to push to server sort
        table.horizontalHeader().sortIndicatorChanged.connect(self._on_sort_changed)

    def _on_sort_changed(self, column: int, order: QtCore.Qt.SortOrder):
        # Push sort down to server (DB) via GridDataSource; key from ColumnDef.key
        key = self.model.columns[column].key
        direction = "asc" if order == QtCore.Qt.SortOrder.AscendingOrder else "desc"
        self.ds.set_sort((key, direction))
        # Model reload already done in set_sort() -> ds.refresh(); reflect in view:
        self.model.beginResetModel()
        self.model.endResetModel()

    def set_filter_text(self, text: str):
        # Client-side quick filter (optional). For server-side, call ds.set_filters(...)
        self.proxy.setFilterFixedString(text)

    def reload(self):
        self.model.reload()
