from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Breakeven(QObject):
    totalRevenueRequiredChanged = Signal()
    revenueFromRetailToFacilityChanged = Signal()
    revenueRequiredFromChargersChanged = Signal()
    evChargingPriceToBreakevenChanged = Signal()

    def __init__(self):
        # total_revenue_required: float = -85_599,
        # revenue_from_retail_to_facility: float = 0.0308,
        # revenue_required_from_chargers: float = 212_063,
        # ev_charging_price_to_breakeven: float = 1_280_138
        super().__init__()
        self.total_revenue_required:float = 0
        self.revenue_from_retail_to_facility:float = 0
        self.revenue_required_from_chargers:float = 0
        self.ev_charging_price_to_breakeven:float = 0

        self.totalRevenueRequiredChanged.connect(self.update_revenueRequiredFromChargers)
        self.revenueRequiredFromChargersChanged.connect(self.update_revenueRequiredFromChargers)



    def emitUpdateSignals(self):
        self.totalRevenueRequiredChanged.emit()
        self.revenueFromRetailToFacilityChanged.emit()
        self.revenueRequiredFromChargersChanged.emit()
        self.evChargingPriceToBreakevenChanged.emit()

    @Property(float, notify=totalRevenueRequiredChanged) #getter
    def totalRevenueRequired(self) -> float:
        return self.total_revenue_required

    @totalRevenueRequired.setter
    def totalRevenueRequired(self, net_present_value:float) -> None:
        self.total_revenue_required = net_present_value
        self.totalRevenueRequiredChanged.emit()

    @Property(float, notify=revenueFromRetailToFacilityChanged) #getter
    def revenueFromRetailToFacility(self) -> float:
        return self.revenue_from_retail_to_facility

    @revenueFromRetailToFacility.setter
    def revenueFromRetailToFacility(self, revenue_from_retail_to_facility:float) -> None:
        self.revenue_from_retail_to_facility = revenue_from_retail_to_facility
        self.revenueFromRetailToFacilityChanged.emit()

    @Property(float, notify=revenueRequiredFromChargersChanged) #getter
    def revenueRequiredFromChargers(self) -> float:
        return self.revenue_required_from_chargers

    @revenueRequiredFromChargers.setter
    def revenueRequiredFromChargers(self, revenue_required_from_chargers:float) -> None:
        self.revenue_required_from_chargers = revenue_required_from_chargers
        self.revenueRequiredFromChargersChanged.emit()        

    @Property(float, notify=evChargingPriceToBreakevenChanged) #getter
    def evChargingPriceToBreakeven(self) -> float:
        return self.ev_charging_price_to_breakeven

    @evChargingPriceToBreakeven.setter
    def evChargingPriceToBreakeven(self, ev_charging_price_to_breakeven:float) -> None:
        self.ev_charging_price_to_breakeven = ev_charging_price_to_breakeven
        self.evChargingPriceToBreakevenChanged.emit()      

    @Slot()
    def update_revenueRequiredFromChargers(self):
        if (
            new_value := self.total_revenue_required - self.revenue_from_retail_to_facility
        ) != self.revenue_required_from_chargers:
            self.revenueRequiredFromChargers = new_value