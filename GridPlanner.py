# from PyQt6.QtWidgets import QApplication, QLabel
# app = QApplication([])
# w = QLabel("PyQt6 ✅")
# w.show()
# app.exec()

if __name__ == '__main__':
    # from src.core.models.shunt.switched_shunt import SwitchedShunt, ControlMode
    from PyQt6.QtWidgets import QApplication, QLabel, QFrame
    app = QApplication([])
    from src.ui.features.buses.views.bus_list_view import BusListView
    parent = QFrame(None)
    bus_list_view = BusListView(parent=None, bus_repo = None)
    bus_list_view.show()
    app.exec()


    # switched_shunt = SwitchedShunt('SC', None, None, None, control_mode=ControlMode(1))
    print()