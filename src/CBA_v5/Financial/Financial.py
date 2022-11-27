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
        capital_expenditure: CapitalExpenditure = CapitalExpenditure(),
        operating_expenditure: OperatingExpenditure = OperatingExpenditure(),
        revenue: Revenue = Revenue()
    ):
        super().__init__()
        self.name: str = name
        self.capital_expenditure: CapitalExpenditure = capital_expenditure
        self.operating_expenditure: OperatingExpenditure = operating_expenditure
        self.revenue_: Revenue = revenue

        self.revenue_.five_year_lifetime.revenue_required_to_break_even = round(
                (self.operating_expenditure.operating_expenditure_items.total_opex * 5)\
                    + self.capital_expenditure.capital_expenditure_items.total_capex,
                2
            )

    # def emitUpdateSignals(self):
    #     self.capitalExpenditureChanged.emitUpdateSignals()
    #     self._charging_and_demand.emitUpdateSignals()

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
        