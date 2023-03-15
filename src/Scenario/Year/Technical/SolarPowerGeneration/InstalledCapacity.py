from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class InstalledCapacity(QObject):
    installedCapacityChanged = Signal()

    def __init__(self, installed_capacity: float = 27):
        super().__init__()
        self.installed_capacity:float = installed_capacity

    def emitUpdateSignals(self):    
        self.installedCapacityChanged.emit()

    @Property(float, notify=installedCapacityChanged) #getter
    def installedCapacity(self) -> float:
        return self.installed_capacity

    @installedCapacity.setter
    def installedCapacity(self, installed_capacity:float) -> None:
        if self.installed_capacity != installed_capacity :
            self.installed_capacity = installed_capacity
            self.installedCapacityChanged.emit()