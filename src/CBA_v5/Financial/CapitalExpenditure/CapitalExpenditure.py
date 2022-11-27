from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .CaptialExpenditureItems import CapitalExpenditureItems
from .Depreciation import Depreciation
from .ExchangeRate import ExchangeRate

class CapitalExpenditure(QObject):
    capitalExpenditureItemsChanged = Signal()
    depreciationChanged = Signal()
    exchangeRateChanged = Signal()

    def __init__(self,
        capital_expenditure_items: CapitalExpenditureItems = CapitalExpenditureItems(),
        depreciation: Depreciation = Depreciation(),
        exchange_rate: ExchangeRate = ExchangeRate()
    ):
        super().__init__()
        self.capital_expenditure_items = capital_expenditure_items
        self.depreciation_ = depreciation
        self.exchange_rate = exchange_rate

    @Property(CapitalExpenditureItems, notify=capitalExpenditureItemsChanged) #getter
    def capitalExpenditureItems(self) -> CapitalExpenditureItems:
        return self.capital_expenditure_items
        
    @Property(Depreciation, notify=depreciationChanged) #getter
    def depreciation(self) -> Depreciation:
        return self.depreciation_

    @Property(ExchangeRate, notify=exchangeRateChanged) #getter
    def exchangeRate(self) -> ExchangeRate:
        return self.exchange_rate