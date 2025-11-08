from PySide6 import QtWidgets
from src.ui.kits.grids.datasource import GridDataSource
from src.ui.kits.grids.binder_qt import QtGridBinder
from src.ui.features.buses.data.bus_query import BusQuery
from .columns import BusColumns

class BusListView(QtWidgets.QWidget):
    def __init__(self, parent, bus_repo):
        super().__init__(parent)
        self.table = QtWidgets.QTableView(self)
        self.filter_box = QtWidgets.QLineEdit(self)
        self.filter_box.setPlaceholderText("Quick filter…")

        ds = GridDataSource(BusQuery(bus_repo))
        self.binder = QtGridBinder(self.table, BusColumns, ds)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.filter_box)
        layout.addWidget(self.table)

        # initial load
        self.binder.reload()

        # client-side filter (optional)
        self.filter_box.textChanged.connect(self.binder.set_filter_text)

        # example signal forwarding (double-click -> open detail)
        self.table.doubleClicked.connect(self._on_row_activated)

    def _on_row_activated(self, index):
        # Translate proxy -> source row to get the DTO
        src = self.binder.proxy.mapToSource(index)
        row_obj = self.binder.model.ds.rows[src.row()]
        # TODO: emit a signal or call presenter
        # self.presenter.on_row_activated(row_obj.id)
