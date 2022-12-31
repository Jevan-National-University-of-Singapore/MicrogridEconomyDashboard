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
        