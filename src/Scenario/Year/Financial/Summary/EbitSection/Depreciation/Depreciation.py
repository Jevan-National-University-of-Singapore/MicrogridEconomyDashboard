from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Depreciation(QObject):
    chargersChanged = Signal()
    essChanged = Signal()
    totalChanged = Signal()

    def __init__(self,
        chargers: float = 361_876,
        ess: float = 12_071,

        total: float = 373_947
    ):
        super().__init__()
        self.chargers_: float = chargers
        self.ess_: float = ess
        self.total_: float = total


    def emitUpdateSignals(self):    
        self.chargersChanged.emit()
        self.essChanged.emit()
        self.totalChanged.emit()

    @Property(float, notify=chargersChanged) #getter
    def chargers(self) -> float:
        return self.chargers_

    @chargers.setter
    def chargers(self, chargers:float) -> None:
        self.chargers_ = chargers
        self.chargersChanged.emit()

    @Property(float, notify=essChanged) #getter
    def ess(self) -> float:
        return self.ess_

    @ess.setter
    def ess(self, ess:float) -> None:
        self.ess_ = ess
        self.essChanged.emit()

    @Property(float, notify=totalChanged) #getter
    def total(self) -> float:
        return self.total_

    @total.setter
    def total(self, total_:float) -> None:
        self.total_ = total_
        self.totalChanged.emit()        


    @Slot()
    def update_total(self):
        self.total_ = self.chargers_ + self.ess_
        self.totalChanged.emit()