from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from typing import Optional

from .EbitdaSection.EbitdaSection import EbitdaSection
from .EbitSection.EbitSection import EbitSection
from .NetIncomeSection.NetIncomeSection import NetIncomeSection
from .FreeCashFlowSection.FreeCashFlowSection import FreeCashFlowSection
from .DiscountedCashFlowsSection.DiscountedCashFlowsSection import DiscountedCashFlowsSection
from .InternalRateOfReturnSection.InternalRateOfReturnSection import InternalRateOfReturnSection

class Summary(QObject):
    ebitdaSectionChanged = Signal()
    ebitSectionChanged = Signal()
    netIncomeSectionChanged = Signal()
    freeCashFlowSectionChanged = Signal()
    discountedCashFlowsSectionChanged = Signal()
    internalRateOfReturnSectionChanged = Signal()

    def __init__(self,
        ebitda_section: Optional[EbitdaSection] = None,
        ebit_section: Optional[EbitSection] = None,
        net_income_section: Optional[NetIncomeSection] = None,
        free_cash_flow_section: Optional[FreeCashFlowSection] = None,
        discounted_cash_flow_section: Optional[DiscountedCashFlowsSection] = None,
        internal_rate_of_return_section: Optional[InternalRateOfReturnSection] = None
    ):
        super().__init__()
        self.ebitda_section:EbitdaSection = EbitdaSection() if ebitda_section is None else ebitda_section
        self.ebit_section:EbitSection = EbitSection() if ebit_section is None else ebit_section
        self.net_income_section:NetIncomeSection = NetIncomeSection() if net_income_section is None else net_income_section
        self.free_cash_flow_section: FreeCashFlowSection = FreeCashFlowSection() if free_cash_flow_section is None else free_cash_flow_section
        self.discounted_cash_flow_section: DiscountedCashFlowsSection = DiscountedCashFlowsSection() if discounted_cash_flow_section is None else discounted_cash_flow_section
        self.internal_rate_of_return_section: InternalRateOfReturnSection = InternalRateOfReturnSection() if internal_rate_of_return_section is None else internal_rate_of_return_section
               
        self.ebitda_section.ebitdaChanged.connect(self.update_ebitSection_ebit)
        self.ebit_section.depreciation_.totalChanged.connect(self.update_ebitSection_ebit)

        self.ebit_section.ebitChanged.connect(self.update_netIncomeSection_taxExpense)

        self.ebit_section.ebitChanged.connect(self.update_netIncomeSection_netIncome)
        self.net_income_section.taxExpenseChanged.connect(self.update_netIncomeSection_netIncome)

        self.net_income_section.netIncomeChanged.connect(self.update_freeCashFlowSection_operatingCashFlow) #error trace 2.1
        self.ebit_section.depreciation_.totalChanged.connect(self.update_freeCashFlowSection_operatingCashFlow)

        
    def emitUpdateSignals(self):    
        self.ebitda_section.emitUpdateSignals()
        self.ebit_section.emitUpdateSignals()
        self.net_income_section.emitUpdateSignals()
        self.free_cash_flow_section.emitUpdateSignals()
        self.discounted_cash_flow_section.emitUpdateSignals()
        self.internal_rate_of_return_section.emitUpdateSignals()

        self.ebitdaSectionChanged.emit()
        self.ebitSectionChanged.emit()
        self.netIncomeSectionChanged.emit()
        self.freeCashFlowSectionChanged.emit()
        self.discountedCashFlowsSectionChanged.emit()
        self.internalRateOfReturnSectionChanged.emit()

    @Property(EbitdaSection, notify=ebitdaSectionChanged) #getter
    def ebitdaSection(self) -> EbitdaSection:
        return self.ebitda_section

    @ebitdaSection.setter
    def ebitdaSection(self, ebitda_section:EbitdaSection) -> None:
        if self.ebitda_section != ebitda_section:
            self.ebitda_section = ebitda_section
            self.ebitdaSectionChanged.emit()


    @Property(EbitSection, notify=ebitSectionChanged) #getter
    def ebitSection(self) -> EbitSection:
        return self.ebit_section

    @ebitSection.setter
    def ebitSection(self, ebit_section:EbitSection) -> None:
        if self.ebit_section != ebit_section:
            self.ebit_section = ebit_section
            self.ebitSectionChanged.emit()        

    @Property(NetIncomeSection, notify=netIncomeSectionChanged) #getter
    def netIncomeSection(self) -> NetIncomeSection:
        return self.net_income_section

    @netIncomeSection.setter
    def netIncomeSection(self, net_income:NetIncomeSection) -> None:
        if self.net_income_section != net_income:
            self.net_income_section = net_income    
            self.netIncomeSectionChanged.emit()                 
        
    @Property(FreeCashFlowSection, notify=freeCashFlowSectionChanged) #getter
    def freeCashFlowSection(self) -> FreeCashFlowSection:
        return self.free_cash_flow_section

    @freeCashFlowSection.setter
    def freeCashFlowSection(self, free_cash_flow_section:FreeCashFlowSection) -> None:
        if self.free_cash_flow_section != free_cash_flow_section:
            self.free_cash_flow_section = free_cash_flow_section    
            self.freeCashFlowSectionChanged.emit()          

    @Property(DiscountedCashFlowsSection, notify=discountedCashFlowsSectionChanged) #getter
    def discountedCashFlowsSection(self) -> DiscountedCashFlowsSection:
        return self.discounted_cash_flow_section

    @discountedCashFlowsSection.setter
    def discountedCashFlowsSection(self, discounted_cash_flow_section:DiscountedCashFlowsSection) -> None:
        if self.discounted_cash_flow_section != discounted_cash_flow_section:
            self.discounted_cash_flow_section = discounted_cash_flow_section  
            self.discountedCashFlowsSectionChanged.emit()        

    @Property(InternalRateOfReturnSection, notify=internalRateOfReturnSectionChanged) #getter
    def internalRateOfReturnSection(self) -> InternalRateOfReturnSection:
        return self.internal_rate_of_return_section

    @internalRateOfReturnSection.setter
    def internalRateOfReturnSection(self, internal_rate_of_return_section:InternalRateOfReturnSection) -> None:
        if self.internal_rate_of_return_section != internal_rate_of_return_section:
            self.internal_rate_of_return_section = internal_rate_of_return_section  
            self.internalRateOfReturnSectionChanged.emit()                 

    @Slot()
    def update_ebitSection_ebit(self):
        if (value := self.ebitda_section.ebitda_ - self.ebit_section.depreciation_.total_) != self.ebit_section.ebit_:
            self.ebit_section.ebit_ = value
            self.ebit_section.ebitChanged.emit()

    @Slot()
    def update_netIncomeSection_taxExpense(self):
        if(new_value := 0.25 * self.ebit_section.ebit_) != self.net_income_section.tax_expense:
            self.net_income_section.tax_expense = new_value
            self.net_income_section.taxExpenseChanged.emit()

    @Slot()
    def update_netIncomeSection_netIncome(self):
        if (
            new_value := self.ebit_section.ebit_ - self.net_income_section.tax_expense
        ) != self.net_income_section.net_income:
            self.net_income_section.net_income = new_value
            self.net_income_section.netIncomeChanged.emit()

    @Slot()
    def update_freeCashFlowSection_operatingCashFlow(self):
        if (
            new_value := self.net_income_section.net_income + self.ebit_section.depreciation_.total_
        ) != self.free_cash_flow_section.operating_cash_flow:
            self.free_cash_flow_section.operating_cash_flow = new_value
            self.free_cash_flow_section.operatingCashFlowChanged.emit()
        