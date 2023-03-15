from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class RevenueItems(QObject):
    chargersChanged = Signal()
    retailToFacilityChanged = Signal()
    totalRevenueChanged = Signal()

    def __init__(self):
        super().__init__()
        self.retail_to_facility:float = 0
        self.chargers_:float = 0

        self.total_revenue:float = self.chargers_ + self.retail_to_facility

        self.chargersChanged.connect(self.update_totalRevenue)
        self.retailToFacilityChanged.connect(self.update_totalRevenue)

    def emitUpdateSignals(self):        
        self.chargersChanged.emit()
        self.retailToFacilityChanged.emit()
        self.totalRevenueChanged.emit()

    @Property(float, notify=chargersChanged) #getter
    def chargers(self) -> float:
        return self.chargers_

    @chargers.setter
    def chargers(self, chargers:float) -> None:
        self.chargers_ = chargers
        self.chargersChanged.emit()

    @Property(float, notify=retailToFacilityChanged) #getter
    def retailToFacility(self) -> float:
        return self.retail_to_facility

    @retailToFacility.setter
    def retailToFacility(self, retail_to_facility:str) -> None:
        self.retail_to_facility = retail_to_facility
        self.retailToFacilityChanged.emit()

    @Property(float, notify=chargersChanged) #getter
    def totalRevenue(self) -> float:
        return self.total_revenue

    @totalRevenue.setter
    def totalRevenue(self, total_revenue:float) -> None:
        self.total_revenue = total_revenue
        self.totalRevenueChanged.emit()

    @Slot()
    def update_totalRevenue(self):
        if (new_value := self.chargers_ + self.retail_to_facility) != self.total_revenue:
            self.total_revenue = new_value
        self.totalRevenueChanged.emit()        