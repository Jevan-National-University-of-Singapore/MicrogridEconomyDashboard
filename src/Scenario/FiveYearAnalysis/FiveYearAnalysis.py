from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

# from .InstalledCapacity import InstalledCapacity
# from .AyerKerohSiteConditions import AyerKerohSiteConditions
# from .SolarEnergyProduction import SolarEnergyProduction
# from .HourlySolarPowerGeneration import HourlySolarPowerGeneration

class FiveYearAnalysis(QObject):
    netPresentValueChanged = Signal()
    internalRateOfReturnChanged = Signal()
    netProfitsChanged = Signal()
    initialInvestmentChanged = Signal()

    def __init__(self,
        net_present_value: float = -85_599,
        internal_rate_of_return: float = 0.0308,
        net_profits: float = 212_063,
        initial_investment: float = 1_280_138
    ):
        super().__init__()
        self.net_present_value:float = net_present_value
        self.internal_rate_of_return:float = internal_rate_of_return
        self.net_profits:float = net_profits
        self.initial_investment:float = initial_investment

    def emitUpdateSignals(self):
        self.netPresentValueChanged.emit()
        self.internalRateOfReturnChanged.emit()
        self.netProfitsChanged.emit()
        self.initialInvestmentChanged.emit()

    @Property(str, notify=netPresentValueChanged) #getter
    def netPresentValue(self) -> str:
        return str(self.net_present_value)

    @netPresentValue.setter
    def netPresentValue(self, net_present_value:str) -> None:
        self.net_present_value = round(float(net_present_value), 2)
        self.netPresentValueChanged.emit()

    @Property(str, notify=internalRateOfReturnChanged) #getter
    def internalRateOfReturn(self) -> str:
        return str(self.internal_rate_of_return)

    @internalRateOfReturn.setter
    def internalRateOfReturn(self, internal_rate_of_return:str) -> None:
        self.internal_rate_of_return = round(float(internal_rate_of_return), 2)
        self.internalRateOfReturnChanged.emit()

    @Property(str, notify=netProfitsChanged) #getter
    def netProfits(self) -> str:
        return str(self.net_profits)

    @netProfits.setter
    def netProfits(self, net_profits:str) -> None:
        self.net_profits = round(float(net_profits), 2)
        self.netProfitsChanged.emit()        

    @Property(str, notify=initialInvestmentChanged) #getter
    def initialInvestment(self) -> str:
        return str(self.initial_investment)

    @initialInvestment.setter
    def initialInvestment(self, initial_investment:str) -> None:
        self.initial_investment = round(float(initial_investment), 2)
        self.initialInvestmentChanged.emit()                