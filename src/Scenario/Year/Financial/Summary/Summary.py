from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from typing import Optional

from .EbitdaSection.EbitdaSection import EbitdaSection
from .EbitSection.EbitSection import EbitSection
from .NetIncomeSection.NetIncomeSection import NetIncomeSection
from .FreeCashFlowSection.FreeCashFlowSection import FreeCashFlowSection
from .PresentValueOfCashFlowSection.PresentValueOfCashFlowSection import PresentValueOfCashFlowSection

class Summary(QObject):
    ebitdaSectionChanged = Signal()
    ebitSectionChanged = Signal()
    netIncomeSectionChanged = Signal()
    freeCashFlowSectionChanged = Signal()
    presentValueOfCashFlowSectionChanged = Signal()

    def __init__(self,
        ebitda_section: Optional[EbitdaSection] = None,
        ebit_section: Optional[EbitSection] = None,
        net_income_section: Optional[NetIncomeSection] = None,
        free_cash_flow_section: Optional[FreeCashFlowSection] = None,
        present_value_of_cash_flow_section: Optional[PresentValueOfCashFlowSection] = None
    ):
        super().__init__()
        self.ebitda_section:EbitdaSection = EbitdaSection() if ebitda_section is None else ebitda_section
        self.ebit_section:EbitSection = EbitSection() if ebit_section is None else ebit_section
        self.net_income_section:NetIncomeSection = NetIncomeSection() if net_income_section is None else net_income_section
        self.free_cash_flow_section: FreeCashFlowSection = FreeCashFlowSection() if free_cash_flow_section is None else free_cash_flow_section
        self.present_value_of_cash_flow_section: PresentValueOfCashFlowSection = PresentValueOfCashFlowSection() if present_value_of_cash_flow_section is None else present_value_of_cash_flow_section
        
    def emitUpdateSignals(self):    
        self.ebitdaSectionChanged.emit()
        self.ebitSectionChanged.emit()
        self.netIncomeSectionChanged.emit()
        self.freeCashFlowSectionChanged.emit()
        self.presentValueOfCashFlowSectionChanged.emit()

    @Property(EbitdaSection, notify=ebitdaSectionChanged) #getter
    def ebitdaSection(self) -> EbitdaSection:
        return self.ebitda_section

    @ebitdaSection.setter
    def ebitdaSection(self, ebitda_section:EbitdaSection) -> None:
        self.ebitda_section = ebitda_section
        self.ebitdaSectionChanged.emit()


    @Property(EbitSection, notify=ebitSectionChanged) #getter
    def ebitSection(self) -> EbitSection:
        return self.ebit_section

    @ebitSection.setter
    def ebitSection(self, ebit_section:EbitSection) -> None:
        self.ebit_section = ebit_section
        self.ebitSectionChanged.emit()        

    @Property(NetIncomeSection, notify=netIncomeSectionChanged) #getter
    def netIncomeSection(self) -> NetIncomeSection:
        return self.net_income_section

    @netIncomeSection.setter
    def netIncomeSection(self, net_income:NetIncomeSection) -> None:
        self.net_income_section = net_income
        self.netIncomeSectionChanged.emit()             
        
    @Property(FreeCashFlowSection, notify=freeCashFlowSectionChanged) #getter
    def freeCashFlowSection(self) -> FreeCashFlowSection:
        return self.free_cash_flow_section

    @freeCashFlowSection.setter
    def freeCashFlowSection(self, free_cash_flow_section:FreeCashFlowSection) -> None:
        self.free_cash_flow_section = free_cash_flow_section
        self.freeCashFlowSectionChanged.emit()        

    @Property(PresentValueOfCashFlowSection, notify=presentValueOfCashFlowSectionChanged) #getter
    def presentValueOfCashFlowSection(self) -> PresentValueOfCashFlowSection:
        return self.present_value_of_cash_flow_section

    @presentValueOfCashFlowSection.setter
    def presentValueOfCashFlowSection(self, present_value_of_cash_flow_section_changed:PresentValueOfCashFlowSection) -> None:
        self.present_value_of_cash_flow_section = present_value_of_cash_flow_section_changed
        self.presentValueOfCashFlowSectionChanged.emit()                     