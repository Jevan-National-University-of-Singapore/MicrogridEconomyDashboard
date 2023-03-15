from typing import Optional

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .DcChargerDemandSection import DcChargerDemandSection
from .StatusSection import StatusSection
from .TotalChargeSupplySection import TotalChargeSupplySection

class HourlyBreakdown(QObject):
    dcChargerDemandSectionChanged:Signal = Signal()
    statusChanged:Signal = Signal()
    totalChargeSupplySectionChanged:Signal = Signal()

    def __init__(self,
        dc_charger_demand_section:Optional[DcChargerDemandSection] = None,
        status_section:Optional[StatusSection] = None,
        total_charge_supply_section:Optional[TotalChargeSupplySection] = None
    ):
        super().__init__()
        self.dc_charger_demand_section: DcChargerDemandSection = DcChargerDemandSection() if dc_charger_demand_section is None else dc_charger_demand_section
        self.status_section: StatusSection = StatusSection() if status_section is None else status_section
        self.total_charge_supply_section: TotalChargeSupplySection = TotalChargeSupplySection() if total_charge_supply_section is None else total_charge_supply_section
               
        '''****************************************
                    CONNECTIONS
        ****************************************'''  
        self.dc_charger_demand_section.dcChargerDemandElementChanged.connect(self.update_dcChargerDemandSection_loadOnEss)
        self.total_charge_supply_section.totalChargeSupplyElementChanged.connect(self.update_dcChargerDemandSection_loadOnEss)

        self.total_charge_supply_section.totalChargeSupplyElementChanged.connect(self.update_dcChargerDemandSection_essChargeWithLoad)
        self.dc_charger_demand_section.loadOnEssElementChanged.connect(self.update_dcChargerDemandSection_essChargeWithLoad)
        self.status_section.chargeSufficiencyElementChanged.connect(self.update_dcChargerDemandSection_essChargeWithLoad)
        self.status_section. reachedEssStateOfChargeElementChanged.connect(self.update_dcChargerDemandSection_essChargeWithLoad)
        self.dc_charger_demand_section.essChargeElementChanged.connect(self.update_dcChargerDemandSection_essChargeWithLoad)

        self.dc_charger_demand_section.essChargeElementChanged.connect(self.update_statusSection_chargeSufficiency)
        self.dc_charger_demand_section.essStateOfChargeElementChanged.connect(self.update_statusSection_chargeSufficiency)

        self.total_charge_supply_section.totalChargeSupplyElementChanged.connect(self.update_statusSection_chargeState)
        self.dc_charger_demand_section.dcChargerDemandElementChanged.connect(self.update_statusSection_chargeState)
        self.status_section.chargerNeededElementChanged.connect(self.update_statusSection_chargeState)
        self.status_section.reachedEssStateOfChargeElementChanged.connect(self.update_statusSection_chargeState)

        self.dc_charger_demand_section.dcChargerDemandElementChanged.connect(self.update_statusSection_chargerNeeded)

    def emitUpdateSignals(self):
        self.dc_charger_demand_section.emitUpdateSignals()
        self.status_section.emitUpdateSignals()
        self.total_charge_supply_section.emitUpdateSignals()

    @Property(DcChargerDemandSection, notify=dcChargerDemandSectionChanged) #getter
    def dcChargerDemandSection(self) -> DcChargerDemandSection:
        return self.dc_charger_demand_section
        
    @Property(StatusSection, notify=statusChanged) #getter
    def statusSection(self) -> StatusSection:
        return self.status_section

    @Property(TotalChargeSupplySection, notify=totalChargeSupplySectionChanged) #getter
    def totalChargeSupplySection(self) -> TotalChargeSupplySection:
        return self.total_charge_supply_section

    @Slot(int)
    def update_dcChargerDemandSection_loadOnEss(self, hour_index: int):
        dc_charger_demand_at_hour_index:float = self.dc_charger_demand_section.dc_charger_demand[hour_index]
        total_charge_supply:float = self.total_charge_supply_section.total_charge_supply[hour_index]

        if dc_charger_demand_at_hour_index == 0:
            self.dc_charger_demand_section.setLoadOnEssElement(hour_index, 0)
        elif dc_charger_demand_at_hour_index > total_charge_supply:
            self.dc_charger_demand_section.setLoadOnEssElement(hour_index, dc_charger_demand_at_hour_index - total_charge_supply)
        else:
            self.dc_charger_demand_section.setLoadOnEssElement(hour_index, 0)

    def _update_dcChargerDemandSection_essChargeWithLoad_firstHour(self, hour_index:int):
        new_value = self.total_charge_supply_section.total_charge_supply[hour_index] - self.dc_charger_demand_section.dc_charger_demand[hour_index]

        self.dc_charger_demand_section.setEssChargeElement(hour_index, new_value)

    def _update_dcChargerDemandSection_essChargeWithLoad_nonFirstHour(self, hour_index: int):
        total_charge_supply:float = self.total_charge_supply_section.total_charge_supply[hour_index]
        previous_hour_value:float = self.dc_charger_demand_section.ess_charge[hour_index-1]

        new_value:float = previous_hour_value

        if self.dc_charger_demand_section.load_on_ess[hour_index] > 0:
            #here
            if self.status_section.charge_sufficiency[hour_index]:
                if self.status_section.reached_ess_state_of_charge[hour_index]:
                    new_value = previous_hour_value + total_charge_supply
                else:
                    new_value = previous_hour_value - self.dc_charger_demand_section.load_on_ess[hour_index]

            else:
                new_value = previous_hour_value + total_charge_supply

        elif self.status_section.reached_ess_state_of_charge[hour_index]:
            new_value = previous_hour_value
        else:
            new_value = previous_hour_value + total_charge_supply
           
        self.dc_charger_demand_section.setEssChargeElement(hour_index, new_value)
        '''
        S45: load_on_ess
        S50: insufficient_charge
        S53: reached_ess_soc
        R46: previous_ess_charge_with_load
        S41: total_charge_supply

        IF(S45>0,
            IF(S50="NO",
                IF(S53="NO",
                    R46-S45,
                else
                    R46+S41),
            else
                R46+S41),
        else 
            IF(S53="NO",
                R46+S41,
            else 
                R46))

        =IF(S45>0,IF(S50="NO",IF(S53="NO",R46-S45,R46+S41),R46+S41),IF(S53="NO",R46+S41,R46))
        '''

    @Slot(int)
    def update_dcChargerDemandSection_essChargeWithLoad(self, _: int):
        self._update_dcChargerDemandSection_essChargeWithLoad_firstHour(0)
        for hour_index in range(23):
            self._update_dcChargerDemandSection_essChargeWithLoad_nonFirstHour(hour_index+1)

    @Slot(int)
    def update_statusSection_chargeSufficiency(self, hour_index:int):
        if hour_index == 0:
            self.status_section.setChargeSufficiencyElement(0, True)
        else:
            new_value: float = self.dc_charger_demand_section.load_on_ess[hour_index] < self.dc_charger_demand_section.ess_charge[hour_index-1]
            self.status_section.setChargeSufficiencyElement(hour_index, new_value)

    @Slot(int)
    def update_statusSection_chargeState(self, hour_index:int):
        if self.status_section.charger_needed[hour_index]:
            new_value:str = "charge" if self.status_section.reached_ess_state_of_charge[hour_index] else "discharge"
            self.status_section.setChargeStatusElement(hour_index, new_value)
        elif self.total_charge_supply_section.total_charge_supply[hour_index] > 0:
            self.status_section.setChargeStatusElement(hour_index, "charge")
        elif (
            self.total_charge_supply_section.total_charge_supply[hour_index]
            + self.dc_charger_demand_section.dc_charger_demand[hour_index]
        ) > 0:
            self.status_section.setChargeStatusElement(hour_index, "idle")
        

    @Slot(int)        
    def update_statusSection_chargerNeeded(self, hour_index:int):
        self.status_section.setChargerNeededElement(
            hour_index,
            self.dc_charger_demand_section.dc_charger_demand[hour_index] > 0    
        )

