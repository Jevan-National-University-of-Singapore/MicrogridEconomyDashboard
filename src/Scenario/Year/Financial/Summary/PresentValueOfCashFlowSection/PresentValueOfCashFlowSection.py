from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class PresentValueOfCashFlowSection(QObject):
    discountedCashFlowsChanged = Signal()
    presentValueOfCashFlowChanged = Signal()

    def __init__(self,
        discounted_cash_flows: float = 0,
        present_value_of_cash_flow: float = 1_280_138
    ):
        super().__init__()
        self.discounted_cash_flows:float = discounted_cash_flows
        self.present_value_of_cash_flow:float = present_value_of_cash_flow

    def emitUpdateSignals(self):    
        self.discountedCashFlowsChanged.emit()
        self.presentValueOfCashFlowChanged.emit()

    @Property(float, notify=discountedCashFlowsChanged) #getter
    def discountedCashFlows(self) -> float:
        return self.discounted_cash_flows

    @discountedCashFlows.setter
    def discountedCashFlows(self, discounted_cash_flows:float) -> None:
        self.discounted_cash_flows = discounted_cash_flows
        self.discountedCashFlowsChanged.emit()

    @Property(float, notify=presentValueOfCashFlowChanged) #getter
    def presentValueOfCashFlow(self) -> float:
        return self.present_value_of_cash_flow

    @presentValueOfCashFlow.setter
    def presentValueOfCashFlow(self, present_value_of_cash_flow:float) -> None:
        self.present_value_of_cash_flow = present_value_of_cash_flow
        self.presentValueOfCashFlowChanged.emit()