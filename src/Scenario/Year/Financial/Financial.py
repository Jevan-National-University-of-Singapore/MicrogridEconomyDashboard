from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from typing import Optional

from .CapitalExpenditure.CapitalExpenditure import CapitalExpenditure
from .OperatingExpenditure.OperatingExpenditure import OperatingExpenditure
from .Revenue.Revenue import Revenue
from .Summary.Summary import Summary

class Financial(QObject):
    capitalExpenditureChanged = Signal()
    operatingExpenditureChanged = Signal()
    revenueChanged = Signal()
    summaryChanged = Signal()

    def __init__(self, 
        name: str = None,
        capital_expenditure: Optional[CapitalExpenditure] = None,
        operating_expenditure: Optional[OperatingExpenditure] = None,
        revenue: Optional[Revenue] = None,

        summary: Optional[Summary] = None
    ):
        super().__init__()
        self.name: str = name
        self.capital_expenditure: CapitalExpenditure = CapitalExpenditure() if capital_expenditure is None else capital_expenditure
        self.operating_expenditure: OperatingExpenditure = OperatingExpenditure() if operating_expenditure is None else operating_expenditure
        self.revenue_: Revenue = Revenue() if revenue is None else revenue
        self.summary_: Summary = Summary() if summary is None else summary
        
        self.operating_expenditure.operating_expenditure_items.totalOpexChanged.connect(self.update_summary_ebitdaSection_opex)
        self.capital_expenditure.capital_expenditure_items.totalCapexChanged.connect(self.update_summary_freeCashFlowSection_capex)

    def emitUpdateSignals(self):
        self.capital_expenditure.emitUpdateSignals()
        self.operating_expenditure.emitUpdateSignals()
        self.revenue_.emitUpdateSignals()
        self.summary_.emitUpdateSignals()

    @Property(CapitalExpenditure, notify=capitalExpenditureChanged) #getter
    def capitalExpenditure(self) -> CapitalExpenditure:
        return self.capital_expenditure

    @Property(OperatingExpenditure, notify=operatingExpenditureChanged) #getter
    def operatingExpenditure(self) -> OperatingExpenditure:
        return self.operating_expenditure
    
    @Property(Revenue, notify=revenueChanged) #getter
    def revenue(self) -> Revenue:
        return self.revenue_

    @Property(Summary, notify=summaryChanged) #getter
    def summary(self) -> Summary:
        return self.summary_

    @Slot()
    def update_revenue_fiveYearLifetime_revenueRequiredToBreakEven(self):
        if (
            new_value := \
                (self.operating_expenditure.operating_expenditure_items.total_opex * 5)\
                + self.capital_expenditure.capital_expenditure_items.total_capex
        ) != self.revenue_.revenue_items.total_revenue:
            self.revenue_.revenue_items.total_revenue = new_value
            self.revenue_.revenue_items.totalRevenueChanged.emit()

    @Slot()
    def update_summary_freeCashFlowSection_capex(self):
        if (
            new_value := self.capital_expenditure.capital_expenditure_items.total_capex
        ) != self.summary_.free_cash_flow_section.capex_:
            self.summary_.free_cash_flow_section.capex_ = new_value
            self.summary_.free_cash_flow_section.capexChanged.emit()

        
    @Slot()
    def update_summary_ebitdaSection_opex(self):
        if self.summary_.ebitda_section.opex_ != self.operating_expenditure.operating_expenditure_items.total_opex:
            self.summary_.ebitda_section.opex_ = self.operating_expenditure.operating_expenditure_items.total_opex
            self.summary_.ebitda_section.opexChanged.emit()
        
        