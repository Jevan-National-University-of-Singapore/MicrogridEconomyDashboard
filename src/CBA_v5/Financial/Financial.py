from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .CapitalExpenditure.CapitalExpenditure import CapitalExpenditure
from .OperatingExpenditure.OperatingExpenditure import OperatingExpenditure
from .Revenue.Revenue import Revenue

class Financial(QObject):
    
    capitalExpenditureChanged = Signal()
    operatingExpenditureChanged = Signal()
    revenueChanged = Signal()

    def __init__(self, 
        name: str = None,
        capital_expenditure: CapitalExpenditure|None = None,
        operating_expenditure: OperatingExpenditure|None = None,
        revenue: Revenue|None = None
    ):
        super().__init__()
        self.name: str = name
        self.capital_expenditure: CapitalExpenditure = CapitalExpenditure() if capital_expenditure is None else capital_expenditure
        self.operating_expenditure: OperatingExpenditure = OperatingExpenditure() if operating_expenditure is None else operating_expenditure
        self.revenue_: Revenue = Revenue() if revenue is None else revenue

        self.revenue_.five_year_lifetime.revenue_required_to_break_even = round(
                (self.operating_expenditure.operating_expenditure_items.total_opex * 5)\
                    + self.capital_expenditure.capital_expenditure_items.total_capex,
                2
            )

    def emitUpdateSignals(self):
        self.capital_expenditure.emitUpdateSignals()
        self.operating_expenditure.emitUpdateSignals()
        self.revenue_.emitUpdateSignals()

    @Property(CapitalExpenditure, notify=capitalExpenditureChanged) #getter
    def capitalExpenditure(self) -> CapitalExpenditure:
        return self.capital_expenditure

    @Property(OperatingExpenditure, notify=operatingExpenditureChanged) #getter
    def operatingExpenditure(self) -> OperatingExpenditure:
        return self.operating_expenditure
    
    @Property(Revenue, notify=revenueChanged) #getter
    def revenue(self) -> Revenue:
        return self.revenue_

    @Slot()
    def update_revenue_fiveYearLifetime_revenueRequiredToBreakEven(self):
        self.revenue_.five_year_lifetime.revenue_required_to_break_even = round(
                (self.operating_expenditure.operating_expenditure_items.total_opex * 5)\
                    + self.capital_expenditure.capital_expenditure_items.total_capex,
                2
            )
        