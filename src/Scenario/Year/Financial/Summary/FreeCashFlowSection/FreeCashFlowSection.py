from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class FreeCashFlowSection(QObject):
    operatingCashFlowChanged = Signal()
    capexChanged = Signal()
    changeInNetWorkingCapitalChanged = Signal()
    freeCashFlowChanged = Signal()

    def __init__(self,
        operating_cash_flow: float = 0,
        capex: float = 1_280_138,
        change_in_net_working_capital: float = 0,
        free_cash_flow: float =  1_280_138
    ):
        super().__init__()
        self.operating_cash_flow:float = operating_cash_flow
        self.capex_:float = capex
        self.change_in_net_working_capital:float = change_in_net_working_capital
        self.free_cash_flow:float = free_cash_flow

    def emitUpdateSignals(self):    
        self.operatingCashFlowChanged.emit()
        self.capexChanged.emit()
        self.changeInNetWorkingCapitalChanged.emit()

    @Property(float, notify=operatingCashFlowChanged) #getter
    def operatingCashFlow(self) -> float:
        return self.operating_cash_flow

    @operatingCashFlow.setter
    def operatingCashFlow(self, operating_cash_flow:float) -> None:
        self.operating_cash_flow = operating_cash_flow
        self.operatingCashFlowChanged.emit()

    @Property(float, notify=capexChanged) #getter
    def capex(self) -> float:
        return self.capex_

    @capex.setter
    def capex(self, capex:float) -> None:
        self.capex_ = capex
        self.capexChanged.emit()

    @Property(float, notify=changeInNetWorkingCapitalChanged) #getter
    def changeInNetWorkingCapital(self) -> float:
        return self.change_in_net_working_capital

    @changeInNetWorkingCapital.setter
    def changeInNetWorkingCapital(self, change_in_net_working_capital:float) -> None:
        self.change_in_net_working_capital = change_in_net_working_capital
        self.changeInNetWorkingCapitalChanged.emit()

    @Property(float, notify=freeCashFlowChanged) #getter
    def freeCashFlow(self) -> float:
        return self.free_cash_flow

    @freeCashFlow.setter
    def freeCashFlow(self, free_cash_flow:float) -> None:
        self.free_cash_flow = free_cash_flow
        self.freeCashFlowChanged.emit()        