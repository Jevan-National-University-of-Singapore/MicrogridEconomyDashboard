from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class InstalledCapacity(QObject):
    installedCapacityChanged = Signal()

    def __init__(self,
        installed_capacity: float = 27,
    ):
        super().__init__()
        self.installed_capacity:float = installed_capacity

    def emitUpdateSignals(self):    
        self.installedCapacityChanged.emit()

    @Property(str, notify=installedCapacityChanged) #getter
    def installedCapacity(self) -> str:
        return str(self.installed_capacity)

    @installedCapacity.setter
    def installedCapacity(self, installed_capacity:str) -> None:
        self.installed_capacity = round(float(installed_capacity), 2)
        self.installedCapacityChanged.emit()