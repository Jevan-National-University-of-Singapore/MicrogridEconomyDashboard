from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class FiveYearLifetime(QObject):
    requiredFromChargersChanged = Signal()
    retailToFacilityChanged = Signal()
    revenueRequiredToBreakEvenChanged = Signal()

    def __init__(self,
        retail_to_facility: float = 67_062,
        revenue_required_to_break_even: float = 1_863_201
    ):
        super().__init__()
        self.retail_to_facility:float = retail_to_facility
        self.revenue_required_to_break_even:float = revenue_required_to_break_even

        self.required_from_chargers:float = round(revenue_required_to_break_even - retail_to_facility, 2)

        self.revenueRequiredToBreakEvenChanged.connect(self.updateRequiredFromChargers)
        self.retailToFacilityChanged.connect(self.updateRequiredFromChargers)

    def emitUpdateSignals(self):        
        self.requiredFromChargersChanged.emit()
        self.retailToFacilityChanged.emit()
        self.revenueRequiredToBreakEvenChanged.emit()

    @Property(str, notify=requiredFromChargersChanged) #getter
    def requiredFromChargers(self) -> str:
        return str(self.required_from_chargers)

    @requiredFromChargers.setter
    def requiredFromChargers(self, required_from_chargers:str) -> None:
        self.required_from_chargers = round(float(required_from_chargers), 2)
        self.requiredFromChargersChanged.emit()

    @Property(str, notify=retailToFacilityChanged) #getter
    def retailToFacility(self) -> str:
        return str(self.retail_to_facility)

    @retailToFacility.setter
    def retailToFacility(self, retail_to_facility:str) -> None:
        self.retail_to_facility = round(float(retail_to_facility), 2)
        self.retailToFacilityChanged.emit()

    @Property(str, notify=requiredFromChargersChanged) #getter
    def revenueRequiredToBreakEven(self) -> str:
        return str(self.revenue_required_to_break_even)

    @revenueRequiredToBreakEven.setter
    def revenueRequiredToBreakEven(self, revenue_required_to_break_even:str) -> None:
        self.revenue_required_to_break_even = round(float(revenue_required_to_break_even), 2)
        self.revenueRequiredToBreakEvenChanged.emit()

    @Slot()
    def updateRequiredFromChargers(self):
        self.required_from_chargers:float = round(self.revenue_required_to_break_even - self.retail_to_facility, 2)
        self.requiredFromChargersChanged.emit()