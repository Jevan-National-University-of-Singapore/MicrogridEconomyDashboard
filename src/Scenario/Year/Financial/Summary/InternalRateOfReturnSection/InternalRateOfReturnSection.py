from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class InternalRateOfReturnSection(QObject):
    netPresentValueChanged = Signal()
    internalRateOfReturnChanged = Signal()
    netProfitsFairValueChanged = Signal()
    initialInvestmentChanged = Signal()

    def __init__(self):
        super().__init__()
        self.net_present_value:float = 0
        self.internal_rate_of_return:float = 0
        self.net_profits_fair_value: float = 0,
        self.initial_investment: float = 0

    def emitUpdateSignals(self):    
        self.netPresentValueChanged.emit()
        self.internalRateOfReturnChanged.emit()
        self.netProfitsFairValueChanged.emit()
        self.initialInvestmentChanged.emit()

    @Property(float, notify=netPresentValueChanged) #getter
    def netPresentValue(self) -> float:
        return self.net_present_value

    @netPresentValue.setter
    def netPresentValue(self, tax_expense:float) -> None:
        if self.net_present_value != tax_expense:
            self.net_present_value = tax_expense
            self.netPresentValueChanged.emit()

    @Property(float, notify=internalRateOfReturnChanged) #getter
    def internalRateOfReturn(self) -> float:
        return self.internal_rate_of_return

    @internalRateOfReturn.setter
    def internalRateOfReturn(self, net_income:float) -> None:
        if self.internal_rate_of_return != net_income:
            self.internal_rate_of_return = net_income
            self.internalRateOfReturnChanged.emit()

    @Property(float, notify=netProfitsFairValueChanged) #getter
    def netProfitsFairValue(self) -> float:
        return self.net_profits_fair_value

    @netProfitsFairValue.setter
    def netProfitsFairValue(self, net_profits_fair_value:float) -> None:
        if self.net_profits_fair_value != net_profits_fair_value:
            self.net_profits_fair_value = net_profits_fair_value
            self.netProfitsFairValueChanged.emit()

    @Property(float, notify=initialInvestmentChanged) #getter
    def initialInvestment(self) -> float:
        return self.initial_investment

    @initialInvestment.setter
    def initialInvestment(self, initial_investment:float) -> None:
        if self.initial_investment != initial_investment:
            self.initial_investment = initial_investment
            self.initialInvestmentChanged.emit()            