from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .SolarPowerGeneration.SolarPowerGeneration import SolarPowerGeneration
from .BatteryStorage.BatteryStorage import BatteryStorage
from .ChargingAndDemand.ChargingAndDemand import ChargingAndDemand
from .FiveYearAnalysis.FiveYearsAnalysis import FiveYearsAnalysis

class Technical(QObject):
    
    batteryStorageChanged = Signal()
    chargingAndDemandChanged = Signal()
    solarPowerGenerationChanged = Signal()
    fiveYearAnalysisChanged = Signal()

    def __init__(self, 
        name: str = None,
        battery_storage = BatteryStorage(),
        solar_power_generation = SolarPowerGeneration(),
        charging_and_demand = ChargingAndDemand(),
        five_years_analysis = FiveYearsAnalysis()
    ):
        super().__init__()
        self.battery_storage:BatteryStorage = battery_storage
        self.charging_and_demand:ChargingAndDemand = charging_and_demand
        self.solar_power_generation: SolarPowerGeneration = solar_power_generation
        self.five_years_analysis:FiveYearsAnalysis = five_years_analysis

        self.battery_storage.ess_system.charge_rate_cRate = round(self.charging_and_demand.charging_ports.dc_charger_1_rating /  self.battery_storage.ess_system.installed_capacity_kwh, 2)
        self.battery_storage.ess_system.maximum_power_kw = min(
                self.charging_and_demand.charging_ports.dc_charger_1_rating,
                self.charging_and_demand.ev_characteristics.max_power_rating,
                self.battery_storage.discharge_.power_max
            )

        self.charging_and_demand.charging_ports.dcCharger2RatingChanged.connect(self.updateBatteryStorageChargeRate)
        self.battery_storage.ess_system.installedCapacityChanged.connect(self.updateBatteryStorageChargeRate)
        
        self.charging_and_demand.charging_ports.dcCharger1RatingChanged.connect(self.updateBatteryStorageMaximumPower)
        self.charging_and_demand.ev_characteristics.maxPowerRatingChanged.connect(self.updateBatteryStorageMaximumPower)
        self.battery_storage.discharge_.powerMaxChanged.connect(self.updateBatteryStorageMaximumPower)

        self.battery_storage.grid_charging.gridDrawLimitChanged.connect(self.update_fiveYearsAnalysis_years_totalChargeSupplySection_gridOffPeak)
        self.battery_storage.grid_charging.gridDrawLimitChanged.connect(self.update_fiveYearsAnalysis_years_totalChargeSupplySection_gridPeak)

        self.battery_storage.ess_system.installedCapacityChanged.connect(self.update_fiveYearsAnalysis_yearsAll_dcChargerDemandSection_essStateOfChargeAllElement)
        self.five_years_analysis.years_[0].dc_charger_demand_section.essChargeElementChanged.connect(self.update_fiveYearsAnalysis_years0_dcChargerDemandSection_essStateOfChargeElement)
        self.five_years_analysis.years_[1].dc_charger_demand_section.essChargeElementChanged.connect(self.update_fiveYearsAnalysis_years1_dcChargerDemandSection_essStateOfChargeElement)
        self.five_years_analysis.years_[2].dc_charger_demand_section.essChargeElementChanged.connect(self.update_fiveYearsAnalysis_years2_dcChargerDemandSection_essStateOfChargeElement)
        self.five_years_analysis.years_[3].dc_charger_demand_section.essChargeElementChanged.connect(self.update_fiveYearsAnalysis_years3_dcChargerDemandSection_essStateOfChargeElement)
        self.five_years_analysis.years_[4].dc_charger_demand_section.essChargeElementChanged.connect(self.update_fiveYearsAnalysis_years4_dcChargerDemandSection_essStateOfChargeElement)

        '''
        update_fiveYearsAnalysis_years0_statusSection_reachedEssStateOfChargeElement
        '''
        self.five_years_analysis.years_[0].dc_charger_demand_section.essChargeElementChanged.connect(self.update_fiveYearsAnalysis_years0_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[1].dc_charger_demand_section.essChargeElementChanged.connect(self.update_fiveYearsAnalysis_years1_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[2].dc_charger_demand_section.essChargeElementChanged.connect(self.update_fiveYearsAnalysis_years2_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[3].dc_charger_demand_section.essChargeElementChanged.connect(self.update_fiveYearsAnalysis_years3_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[4].dc_charger_demand_section.essChargeElementChanged.connect(self.update_fiveYearsAnalysis_years4_statusSection_reachedEssStateOfChargeElement)

        self.five_years_analysis.years_[0].status_section.chargerNeededElementChanged.connect(self.update_fiveYearsAnalysis_years0_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[1].status_section.chargerNeededElementChanged.connect(self.update_fiveYearsAnalysis_years1_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[2].status_section.chargerNeededElementChanged.connect(self.update_fiveYearsAnalysis_years2_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[3].status_section.chargerNeededElementChanged.connect(self.update_fiveYearsAnalysis_years3_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[4].status_section.chargerNeededElementChanged.connect(self.update_fiveYearsAnalysis_years4_statusSection_reachedEssStateOfChargeElement)

        self.five_years_analysis.years_[0].total_charge_supply_section.totalChargeSupplyElementChanged.connect(self.update_fiveYearsAnalysis_years0_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[1].total_charge_supply_section.totalChargeSupplyElementChanged.connect(self.update_fiveYearsAnalysis_years1_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[2].total_charge_supply_section.totalChargeSupplyElementChanged.connect(self.update_fiveYearsAnalysis_years2_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[3].total_charge_supply_section.totalChargeSupplyElementChanged.connect(self.update_fiveYearsAnalysis_years3_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[4].total_charge_supply_section.totalChargeSupplyElementChanged.connect(self.update_fiveYearsAnalysis_years4_statusSection_reachedEssStateOfChargeElement)

        self.five_years_analysis.years_[0].dc_charger_demand_section.dcChargerDemandElementChanged.connect(self.update_fiveYearsAnalysis_years0_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[1].dc_charger_demand_section.dcChargerDemandElementChanged.connect(self.update_fiveYearsAnalysis_years1_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[2].dc_charger_demand_section.dcChargerDemandElementChanged.connect(self.update_fiveYearsAnalysis_years2_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[3].dc_charger_demand_section.dcChargerDemandElementChanged.connect(self.update_fiveYearsAnalysis_years3_statusSection_reachedEssStateOfChargeElement)
        self.five_years_analysis.years_[4].dc_charger_demand_section.dcChargerDemandElementChanged.connect(self.update_fiveYearsAnalysis_years4_statusSection_reachedEssStateOfChargeElement)

        self.battery_storage.ess_system.installedCapacityChanged.connect(self.update_fiveYearsAnalysis_yearsAll_statusSection_reachedEssStateOfCharge)
        self.battery_storage.ess_system.stateOfChargeUpperLimitChanged.connect(self.update_fiveYearsAnalysis_yearsAll_statusSection_reachedEssStateOfCharge)
        self.battery_storage.ess_system.stateOfChargeLowerLimitChanged.connect(self.update_fiveYearsAnalysis_yearsAll_statusSection_reachedEssStateOfCharge)




    def emitUpdateSignals(self):
        self.battery_storage.emitUpdateSignals()
        self.charging_and_demand.emitUpdateSignals()
        self.solar_power_generation.emitUpdateSignals()
        self.five_years_analysis.emitUpdateSignals()

    @Property(SolarPowerGeneration, notify=solarPowerGenerationChanged) #getter
    def solarPowerGeneration(self) -> SolarPowerGeneration:
        return self.solar_power_generation

    @Property(BatteryStorage, notify=batteryStorageChanged) #getter
    def batteryStorage(self) -> BatteryStorage:
        return self.battery_storage

    @Property(ChargingAndDemand, notify=chargingAndDemandChanged) #getter
    def chargingAndDemand(self) -> ChargingAndDemand:
        return self.charging_and_demand

    @Property(FiveYearsAnalysis, notify=fiveYearAnalysisChanged) #getter
    def fiveYearsAnalysis(self) -> FiveYearsAnalysis:
        return self.five_years_analysis

    @Slot()
    def updateBatteryStorageChargeRate(self):
        self.battery_storage.ess_system.charge_rate_cRate = round(self.charging_and_demand.charging_ports.dc_charger_1_rating /  self.battery_storage.ess_system.installed_capacity_kwh, 2)
        self.battery_storage.ess_system.chargeRateChanged.emit()

    @Slot()
    def updateBatteryStorageMaximumPower(self):
        self.battery_storage.ess_system.maximum_power_kw = min(
                self.charging_and_demand.charging_ports.dc_charger_1_rating,
                self.charging_and_demand.ev_characteristics.max_power_rating,
                self.battery_storage.discharge_.power_max
            )
        self.battery_storage.ess_system.maximumPowerChanged.emit()
                           
    @Slot()
    def update_fiveYearsAnalysis_years_totalChargeSupplySection_gridOffPeak(self):
        for year_index in range(5):
            for hour_index in [0,1,2,3,4,5,6,7,22,23]:
                new_value:float = self.battery_storage.grid_charging.grid_draw_limit_kw
                self.five_years_analysis.years_[year_index].total_charge_supply_section.setGridOffPeakElement(hour_index, new_value)

    @Slot()
    def update_fiveYearsAnalysis_years_totalChargeSupplySection_gridPeak(self):
        for year_index in range(5):
            for hour_index in [8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                new_value:float = self.battery_storage.grid_charging.grid_draw_limit_kw
                self.five_years_analysis.years_[year_index].total_charge_supply_section.setGridPeakElement(hour_index, new_value)                
        
    @Slot(int)
    def update_fiveYearsAnalysis_years0_dcChargerDemandSection_essStateOfChargeElement(self, hour_index:int):
        self._update_fiveYearsAnalysis_years_dcChargerDemandSection_essStateOfChargeElement(0, hour_index)

    @Slot(int)
    def update_fiveYearsAnalysis_years1_dcChargerDemandSection_essStateOfChargeElement(self, hour_index:int):
        self._update_fiveYearsAnalysis_years_dcChargerDemandSection_essStateOfChargeElement(1, hour_index)

    @Slot(int)
    def update_fiveYearsAnalysis_years2_dcChargerDemandSection_essStateOfChargeElement(self, hour_index:int):
        self._update_fiveYearsAnalysis_years_dcChargerDemandSection_essStateOfChargeElement(2, hour_index)

    @Slot(int)
    def update_fiveYearsAnalysis_years3_dcChargerDemandSection_essStateOfChargeElement(self, hour_index:int):
        self._update_fiveYearsAnalysis_years_dcChargerDemandSection_essStateOfChargeElement(3, hour_index)

    @Slot(int)
    def update_fiveYearsAnalysis_years4_dcChargerDemandSection_essStateOfChargeElement(self, hour_index:int):
        self._update_fiveYearsAnalysis_years_dcChargerDemandSection_essStateOfChargeElement(4, hour_index)                                

    @Slot()
    def update_fiveYearsAnalysis_yearsAll_dcChargerDemandSection_essStateOfChargeAllElement(self):
        installed_capacity = self.battery_storage.ess_system.installed_capacity_kwh
        for year in self.five_years_analysis.years_:
            for i in range(24):
                year.dc_charger_demand_section.setEssStateOfChargeElement(i, year.dc_charger_demand_section.ess_charge[i] / installed_capacity)

    def _update_fiveYearsAnalysis_years_dcChargerDemandSection_essStateOfChargeElement(self, year_index:int, hour_index:int):
        new_value:float = self.five_years_analysis.years_[year_index].dc_charger_demand_section.ess_charge[hour_index] / self.battery_storage.ess_system.installed_capacity_kwh
        self.five_years_analysis.years_[year_index].dc_charger_demand_section.setEssStateOfChargeElement(hour_index, new_value)


    @Slot(int)
    def update_fiveYearsAnalysis_years0_statusSection_reachedEssStateOfChargeElement(self, hour_index:int):
        self._update_fiveYearsAnalysis_years_statusSection_reachedEssStateOfChargeElement(
            year_index=0,
            hour_index=hour_index
        )

    @Slot(int)
    def update_fiveYearsAnalysis_years1_statusSection_reachedEssStateOfChargeElement(self, hour_index:int):
        self._update_fiveYearsAnalysis_years_statusSection_reachedEssStateOfChargeElement(
            year_index=1,
            hour_index=hour_index
        )
        
    @Slot(int)
    def update_fiveYearsAnalysis_years2_statusSection_reachedEssStateOfChargeElement(self, hour_index:int):
        self._update_fiveYearsAnalysis_years_statusSection_reachedEssStateOfChargeElement(
            year_index=2,
            hour_index=hour_index
        )

    @Slot(int)
    def update_fiveYearsAnalysis_years3_statusSection_reachedEssStateOfChargeElement(self, hour_index:int):
        self._update_fiveYearsAnalysis_years_statusSection_reachedEssStateOfChargeElement(
            year_index=3,
            hour_index=hour_index
        )

    @Slot(int)
    def update_fiveYearsAnalysis_years4_statusSection_reachedEssStateOfChargeElement(self, hour_index:int):
        self._update_fiveYearsAnalysis_years_statusSection_reachedEssStateOfChargeElement(
            year_index=4,
            hour_index=hour_index
        )              
    
    @Slot()
    def update_fiveYearsAnalysis_yearsAll_statusSection_reachedEssStateOfCharge(self):
        for year_index in range(5):
            for hour_index in range(24):
                self._update_fiveYearsAnalysis_years_statusSection_reachedEssStateOfChargeElement(
                    year_index=year_index,
                    hour_index=hour_index    
                )

    def _update_fiveYearsAnalysis_years_statusSection_reachedEssStateOfChargeElement(self, year_index:int, hour_index:int):
        if hour_index != 0:
            charger_needed: bool = self.five_years_analysis.years_[year_index].status_section.charger_needed[hour_index]
            ess_charge: float = self.five_years_analysis.years_[year_index].dc_charger_demand_section.ess_charge[hour_index-1]
            total_charge_supply: float = self.five_years_analysis.years_[year_index].total_charge_supply_section.total_charge_supply[hour_index]
            dc_charger_demand: float = self.five_years_analysis.years_[year_index].dc_charger_demand_section.dc_charger_demand[hour_index]

            installed_capacity: float = self.battery_storage.ess_system.installed_capacity_kwh
            soc_upper_limit: float = self.battery_storage.ess_system.state_of_charge_upper_limit_percentage
            soc_lower_limit: float = self.battery_storage.ess_system.state_of_charge_lower_limit_percentage

            if charger_needed:
                new_value:float = ess_charge-(dc_charger_demand-total_charge_supply) < (soc_lower_limit * installed_capacity)
                self.five_years_analysis.years_[year_index].status_section.setReachedEssStateOfChargeElement(hour_index, new_value)                
            else:
                new_value:float = (ess_charge+total_charge_supply) > (soc_upper_limit*installed_capacity)
                self.five_years_analysis.years_[year_index].status_section.setReachedEssStateOfChargeElement(hour_index, new_value)

