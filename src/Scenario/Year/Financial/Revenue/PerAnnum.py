from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class PerAnnum(QObject):
    chargingRevenueRequiredChanged = Signal()
    breakevenPriceToEvChargersChanged = Signal()
    priceToEvChargersChanged = Signal()

    def __init__(self,
        charging_revenue_required: float = 299_357,
        breakeven_price_to_ev_chargers: float = 1.65,
        price_to_ev_chargers: float = 2.00
    ):
        super().__init__()
        self.charging_revenue_required:float = charging_revenue_required
        self.breakeven_price_to_ev_chargers:float = breakeven_price_to_ev_chargers
        self.price_to_ev_chargers: float = price_to_ev_chargers

    def emitUpdateSignals(self):    
        self.chargingRevenueRequiredChanged.emit()
        self.breakevenPriceToEvChargersChanged.emit()
        self.priceToEvChargersChanged.emit()

    @Property(str, notify=chargingRevenueRequiredChanged) #getter
    def chargingRevenueRequired(self) -> str:
        return str(self.charging_revenue_required)

    @chargingRevenueRequired.setter
    def chargingRevenueRequired(self, charging_revenue_required:str) -> None:
        self.charging_revenue_required = round(float(charging_revenue_required), 2)
        self.chargingRevenueRequiredChanged.emit()

    @Property(str, notify=breakevenPriceToEvChargersChanged) #getter
    def breakevenPriceToEvChargers(self) -> str:
        return str(self.breakeven_price_to_ev_chargers)

    @breakevenPriceToEvChargers.setter
    def breakevenPriceToEvChargers(self, breakeven_price_to_ev_chargers:str) -> None:
        self.breakeven_price_to_ev_chargers = round(float(breakeven_price_to_ev_chargers), 2)
        self.breakevenPriceToEvChargersChanged.emit()

    @Property(str, notify=priceToEvChargersChanged) #getter
    def priceToEvChargers(self) -> str:
        return str(self.price_to_ev_chargers)

    @priceToEvChargers.setter
    def priceToEvChargers(self, price_to_ev_chargers:str) -> None:
        self.price_to_ev_chargers = round(float(price_to_ev_chargers), 2)
        self.priceToEvChargersChanged.emit()        