from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Revenue(QObject):
    chargersChanged = Signal()
    retailToFacilityChanged = Signal()
    totalChanged = Signal()

    def __init__(self,
        chargers: float = 361_876,
        retail_to_facility: float = 12_071,

        total: float = 373_947
    ):
        super().__init__()
        self.chargers_: float = chargers
        self.retail_to_facility: float = retail_to_facility
        self.total_: float = total

        # self.total_ = chargers + retail_to_facility

        # self.chargersChanged.connect(self.update_total)
        # self.retailToFacilityChanged.connect(self.update_total)

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

    # @Slot()
    # def update_total(self):
    #     self.total_ = self.chargers_ + self.retail_to_facility
    #     self.totalChanged.emit()
