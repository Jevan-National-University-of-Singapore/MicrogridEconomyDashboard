from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from CaptialExpenditureItems import CapitalExpenditureItems
from Depreciation import Depreciation
from ExchangeRate import ExchangeRate

class CapitalExpenditure(QObject):
    capitalExpenditureItemsChanged = Signal()
    depreciationChanged = Signal()
    exchangeRateChanged = Signal()

    def __init__(self,
        capital_expenditure_items: CapitalExpenditureItems,
        depreciation: Depreciation,
        exchange_rate = ExchangeRate
    ):
        super().__init__()
        self._capital_expenditure_items = capital_expenditure_items
        self._depreciation = depreciation
        self._exchange_rate = exchange_rate

    @Property(CapitalExpenditureItems, notify=capitalExpenditureItemsChanged) #getter
    def capitalExpenditureItems(self) -> CapitalExpenditureItems:
        return self._capital_expenditure_items
        
    @Property(Depreciation, notify=depreciationChanged) #getter
    def depreciation(self) -> Depreciation:
        return self._depreciation

    @Property(ExchangeRate, notify=exchangeRateChanged) #getter
    def exchangeRate(self) -> ExchangeRate:
        return self._exchange_rate