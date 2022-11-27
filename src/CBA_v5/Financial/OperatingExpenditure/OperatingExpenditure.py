from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .OperatingExpenditureItems import OperatingExpenditureItems
from .FixedOAndM import FixedOAndM

class OperatingExpenditure(QObject):
    operatingExpenditureItemsChanged = Signal()
    fixedOAndMChanged = Signal()

    def __init__(self,
        operating_expenditure_items: OperatingExpenditureItems = OperatingExpenditureItems(),
        fixed_o_and_m: FixedOAndM = FixedOAndM()
    ):
        super().__init__()
        self.operating_expenditure_items: OperatingExpenditureItems = operating_expenditure_items
        self.fixed_o_and_m: FixedOAndM = fixed_o_and_m

    def emitUpdateSignals(self):
        self.operating_expenditure_items.emitUpdateSignals()
        self.fixed_o_and_m.emitUpdateSignals()

    @Property(OperatingExpenditureItems, notify=operatingExpenditureItemsChanged) #getter
    def operatingExpenditureItems(self) -> OperatingExpenditureItems:
        return self.operating_expenditure_items
        
    @Property(FixedOAndM, notify=fixedOAndMChanged) #getter
    def fixedOAndM(self) -> FixedOAndM:
        return self.fixed_o_and_m