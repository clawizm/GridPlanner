# from PyQt6.QtWidgets import QApplication, QLabel
# app = QApplication([])
# w = QLabel("PyQt6 ✅")
# w.show()
# app.exec()

if __name__ == '__main__':
    from src.core.models.shunt.switched_shunt import SwitchedShunt, ControlMode


    switched_shunt = SwitchedShunt('SC', None, None, None, control_mode=ControlMode(1))
    print()