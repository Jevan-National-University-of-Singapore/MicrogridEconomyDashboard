from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class NetIncomeSection(QObject):
    taxExpenseChanged = Signal()
    netIncomeChanged = Signal()

    def __init__(self,
        tax_expense: float = 10_399,
        net_income: float = 299_357
    ):
        super().__init__()
        self.tax_expense:float = tax_expense
        self.net_income:float = net_income

    def emitUpdateSignals(self):    
        self.taxExpenseChanged.emit()
        self.netIncomeChanged.emit()

    @Property(float, notify=taxExpenseChanged) #getter
    def taxExpense(self) -> float:
        return self.tax_expense

    @taxExpense.setter
    def taxExpense(self, tax_expense:float) -> None:
        if self.tax_expense != tax_expense:
            self.tax_expense = tax_expense
            self.taxExpenseChanged.emit()

    @Property(float, notify=netIncomeChanged) #getter
    def netIncome(self) -> float:
        return self.net_income

    @netIncome.setter
    def netIncome(self, net_income:float) -> None:
        if self.net_income != net_income:
            self.net_income = net_income
            self.netIncomeChanged.emit()