from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class DiscountedCashFlowsSection(QObject):
    cumulativeCashFlowChanged = Signal()
    presentValueOfCashFlowChanged = Signal()
    weightedAverageCostOfCapitalChanged = Signal()

    def __init__(self):
        super().__init__()
        self.cumulative_cash_flow:float = 0
        self.present_value_of_cash_flow:float = 0
        self.weighted_average_cost_of_capital:float = 0.079

    def emitUpdateSignals(self):    
        self.cumulativeCashFlowChanged.emit()
        self.presentValueOfCashFlowChanged.emit()
        self.weightedAverageCostOfCapitalChanged.emit()

    @Property(float, notify=cumulativeCashFlowChanged) #getter
    def cumulativeCashFlow(self) -> float:
        return self.cumulative_cash_flow

    @cumulativeCashFlow.setter
    def cumulativeCashFlow(self, cumulative_cash_flow:float) -> None:
        if self.cumulative_cash_flow != cumulative_cash_flow:
            self.cumulative_cash_flow = cumulative_cash_flow
            self.cumulativeCashFlowChanged.emit()

    @Property(float, notify=presentValueOfCashFlowChanged) #getter
    def presentValueOfCashFlow(self) -> float:
        return self.present_value_of_cash_flow

    @presentValueOfCashFlow.setter
    def presentValueOfCashFlow(self, present_value_of_cash_flow:float) -> None:
        if self.present_value_of_cash_flow != present_value_of_cash_flow:
            self.present_value_of_cash_flow = present_value_of_cash_flow
            self.presentValueOfCashFlowChanged.emit()

    @Property(float, notify=presentValueOfCashFlowChanged) #getter
    def weightedAverageCostOfCapital(self) -> float:
        return self.weighted_average_cost_of_capital

    @weightedAverageCostOfCapital.setter
    def weightedAverageCostOfCapital(self, weighted_average_cash_flow:float) -> None:
        if self.weighted_average_cost_of_capital != weighted_average_cash_flow:
            self.weighted_average_cost_of_capital = weighted_average_cash_flow
            self.weightedAverageCostOfCapitalChanged.emit()