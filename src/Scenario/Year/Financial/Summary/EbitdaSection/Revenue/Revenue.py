from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Revenue(QObject):
    chargersChanged = Signal()
    retailToFacilityChanged = Signal()
    totalChanged = Signal()

    def __init__(self):
        super().__init__()
        self.chargers_: float = 0
        self.retail_to_facility: float = 0
        self.total_:float = self.chargers_ + self.retail_to_facility


    def emitUpdateSignals(self):    
        self.chargersChanged.emit()
        self.retailToFacilityChanged.emit()
        self.totalChanged.emit()

    @Property(float, notify=chargersChanged) #getter
    def chargers(self) -> float:
        return self.chargers_

    @chargers.setter
    def chargers(self, chargers:float) -> None:
        if self.chargers_ != chargers:
            self.chargers_ = chargers
            self.chargersChanged.emit()

    @Property(float, notify=retailToFacilityChanged) #getter
    def retailToFacility(self) -> float:
        return self.retail_to_facility

    @retailToFacility.setter
    def retailToFacility(self, retail_to_facility:float) -> None:
        if self.retail_to_facility != retail_to_facility:
            self.retail_to_facility = retail_to_facility
            self.retailToFacilityChanged.emit()

    @Property(float, notify=totalChanged) #getter
    def total(self) -> float:
        return self.total_

    @total.setter
    def total(self, total_:float) -> None:
        if self.total_ != total_:
            self.total_ = total_
            self.totalChanged.emit()        