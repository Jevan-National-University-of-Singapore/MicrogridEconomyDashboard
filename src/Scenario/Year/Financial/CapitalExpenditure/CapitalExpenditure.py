from typing import Optional

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .CapitalExpenditureItems import CapitalExpenditureItems
from .Depreciation import Depreciation
from .ExchangeRate import ExchangeRate

class CapitalExpenditure(QObject):
    capitalExpenditureItemsChanged = Signal()
    depreciationChanged = Signal()
    exchangeRateChanged = Signal()

    def __init__(self,
        capital_expenditure_items: Optional[CapitalExpenditureItems] = None,
        depreciation: Optional[Depreciation] = None,
        exchange_rate: Optional[ExchangeRate] = None
    ):
        super().__init__()
        self.capital_expenditure_items: CapitalExpenditureItems = CapitalExpenditureItems() if capital_expenditure_items is None else capital_expenditure_items
        self.depreciation_: Depreciation = Depreciation() if depreciation is None else depreciation
        self.exchange_rate: ExchangeRate = ExchangeRate() if exchange_rate is None else exchange_rate

    def emitUpdateSignals(self):
        self.capital_expenditure_items.emitUpdateSignals()
        self.depreciation_.emitUpdateSignals()
        self.exchange_rate.emitUpdateSignals()

    @Property(CapitalExpenditureItems, notify=capitalExpenditureItemsChanged) #getter
    def capitalExpenditureItems(self) -> CapitalExpenditureItems:
        return self.capital_expenditure_items
        
    @Property(Depreciation, notify=depreciationChanged) #getter
    def depreciation(self) -> Depreciation:
        return self.depreciation_

    @Property(ExchangeRate, notify=exchangeRateChanged) #getter
    def exchangeRate(self) -> ExchangeRate:
        return self.exchange_rate