from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class PerAnnum(QObject):
    chargingRevenueRequiredChanged = Signal()
    priceToEvChargersChanged = Signal()

    def __init__(self,
        charging_revenue_required: float = 299_357,
        price_to_ev_chargers: float = 1.65
    ):
        super().__init__()
        self.charging_revenue_required:float = charging_revenue_required
        self.price_to_ev_chargers:float = price_to_ev_chargers

    def emitUpdateSignals(self):    
        self.chargingRevenueRequiredChanged.emit()
        self.priceToEvChargersChanged.emit()

    @Property(str, notify=chargingRevenueRequiredChanged) #getter
    def chargingRevenueRequired(self) -> str:
        return str(self.charging_revenue_required)

    @chargingRevenueRequired.setter
    def chargingRevenueRequired(self, charging_revenue_required:str) -> None:
        self.charging_revenue_required = round(float(charging_revenue_required), 2)
        self.chargingRevenueRequiredChanged.emit()

    @Property(str, notify=priceToEvChargersChanged) #getter
    def priceToEvChargers(self) -> str:
        return str(self.price_to_ev_chargers)

    @priceToEvChargers.setter
    def priceToEvChargers(self, price_to_ev_chargers:str) -> None:
        self.price_to_ev_chargers = round(float(price_to_ev_chargers), 2)
        self.priceToEvChargersChanged.emit()