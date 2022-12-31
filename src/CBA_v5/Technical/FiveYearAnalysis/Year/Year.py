from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .DcChargerDemandSection import DcChargerDemandSection
from .StatusSection import StatusSection
from .TotalChargeSupplySection import TotalChargeSupplySection

class Year(QObject):
    DcChargerDemandSectionChanged = Signal()
    StatusChanged = Signal()
    TotalChargeSupplySectionChanged = Signal()

    def __init__(self,
        dc_charger_demand_section = DcChargerDemandSection(),
        status_section = StatusSection(),
        total_charge_supply_section = TotalChargeSupplySection()
    ):
        super().__init__()
        self.dc_charger_demand_section: DcChargerDemandSection = dc_charger_demand_section
        self.status_section: StatusSection = status_section
        self.total_charge_supply_section: TotalChargeSupplySection = total_charge_supply_section

    def emitUpdateSignals(self):
        self.dc_charger_demand_section.emitUpdateSignals()
        self.status_section.emitUpdateSignals()
        self.total_charge_supply_section.emitUpdateSignals()

    @Property(DcChargerDemandSection, notify=DcChargerDemandSectionChanged) #getter
    def dcChargerDemandSection(self) -> DcChargerDemandSection:
        return self.dc_charger_demand_section
        
    @Property(StatusSection, notify=StatusChanged) #getter
    def statusSection(self) -> StatusSection:
        return self.status_section

    @Property(TotalChargeSupplySection, notify=TotalChargeSupplySectionChanged) #getter
    def totalChargeSupplySection(self) -> TotalChargeSupplySection:
        return self.total_charge_supply_section

