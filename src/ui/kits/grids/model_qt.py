from PySide6 import QtCore, QtGui
from typing import List, Any
from .columns import ColumnDef, value_of
from .datasource import GridDataSource

ALIGN_MAP = {
    "left":  QtCore.Qt.AlignmentFlag.AlignLeft,
    "right": QtCore.Qt.AlignmentFlag.AlignRight,
    "center":QtCore.Qt.AlignmentFlag.AlignHCenter,
}

class GridModel(QtCore.QAbstractTableModel):
    def __init__(self, ds: GridDataSource, columns: List[ColumnDef], parent=None):
        super().__init__(parent)
        self.ds = ds
        self.columns = columns

    # --- Required overrides ---
    def rowCount(self, parent=QtCore.QModelIndex()) -> int:
        return 0 if parent.isValid() else len(self.ds.rows)

    def columnCount(self, parent=QtCore.QModelIndex()) -> int:
        return 0 if parent.isValid() else len(self.columns)

    def data(self, index: QtCore.QModelIndex, role: int = QtCore.Qt.ItemDataRole.DisplayRole) -> Any:
        if not index.isValid():
            return None
        row = self.ds.rows[index.row()]
        col = self.columns[index.column()]

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            return value_of(col, row)
        if role == QtCore.Qt.ItemDataRole.TextAlignmentRole:
            return int(ALIGN_MAP.get(col.align, ALIGN_MAP["left"]))
        # Optional: return raw value for sorting
        if role == QtCore.Qt.ItemDataRole.UserRole:
            v = col.accessor(row)
            return v
        return None

    def headerData(self, section: int, orientation, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role != QtCore.Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == QtCore.Qt.Orientation.Horizontal:
            return self.columns[section].header
        return section + 1

    # --- Convenience for reloads ---
    def reload(self):
        self.beginResetModel()
        self.ds.refresh()
        self.endResetModel()
