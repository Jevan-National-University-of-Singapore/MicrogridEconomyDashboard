from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Pricing(QObject):
    breakevenPriceToEvChargersChanged = Signal()
    priceToEvChargersChanged = Signal()

    def __init__(self,
        # breakeven_price_to_ev_chargers: float = 1.65,
        price_to_ev_chargers: float = 2.00
    ):
        super().__init__()
        # self.breakeven_price_to_ev_chargers:float = breakeven_price_to_ev_chargers
        self.price_to_ev_chargers: float = price_to_ev_chargers

    def emitUpdateSignals(self):    
        self.breakevenPriceToEvChargersChanged.emit()
        self.priceToEvChargersChanged.emit()

    # @Property(float, notify=breakevenPriceToEvChargersChanged) #getter
    # def breakevenPriceToEvChargers(self) -> float:
    #     return self.breakeven_price_to_ev_chargers

    # @breakevenPriceToEvChargers.setter
    # def breakevenPriceToEvChargers(self, breakeven_price_to_ev_chargers:float) -> None:
    #     if self.breakeven_price_to_ev_chargers != breakeven_price_to_ev_chargers:
    #         self.breakeven_price_to_ev_chargers = breakeven_price_to_ev_chargers
    #         self.breakevenPriceToEvChargersChanged.emit()

    @Property(float, notify=priceToEvChargersChanged) #getter
    def priceToEvChargers(self) -> float:
        return self.price_to_ev_chargers

    @priceToEvChargers.setter
    def priceToEvChargers(self, price_to_ev_chargers:float) -> None:
        if self.price_to_ev_chargers != price_to_ev_chargers:
            self.price_to_ev_chargers = price_to_ev_chargers
            self.priceToEvChargersChanged.emit()        