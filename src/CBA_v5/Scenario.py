from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .ChargingAndDemand.ChargingAndDemand import ChargingAndDemand
from .Technical.Technical import Technical
from .Financial.Financial import Financial

class Scenario(QObject):
    
    chargingAndDemandChanged = Signal()
    technicalChanged = Signal()
    financialChanged = Signal()

    def __init__(self, 
        name: str = None,
        charging_and_demand = ChargingAndDemand(),
        technical = Technical(),
        financial = Financial()
    ):
        super().__init__()
        self.charging_and_demand: ChargingAndDemand = charging_and_demand
        self.technical_: Technical = technical
        self.financial_: Financial = financial

    @Property(ChargingAndDemand, notify=chargingAndDemandChanged) #getter
    def chargingAndDemand(self) -> ChargingAndDemand:
        return self.charging_and_demand

    @chargingAndDemand.setter
    def chargingAndDemand(self, charging_and_demand: ChargingAndDemand):
        self.charging_and_demand = charging_and_demand
        self.chargingAndDemandChanged.emit()

    @Property(Technical, notify=technicalChanged) #getter
    def technical(self) -> Technical:
        return self.technical_

    @technical.setter
    def technical(self, technical:Technical):
        self.technical_ = technical


    @Property(Financial, notify=financialChanged) #getter
    def financial(self) -> Financial:
        return self.financial_

    @financial.setter
    def financial(self, financial:Financial):
        self.financial_ = financial
        