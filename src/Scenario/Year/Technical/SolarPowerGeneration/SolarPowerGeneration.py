from typing import Optional

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .InstalledCapacity import InstalledCapacity
from .AyerKerohSiteConditions import AyerKerohSiteConditions
from .SolarEnergyProduction import SolarEnergyProduction
from .HourlySolarPowerGeneration import HourlySolarPowerGeneration

class SolarPowerGeneration(QObject):
    installedCapacityChanged = Signal()
    ayerKerohSiteConditionsChanged = Signal()
    solarEnergyProductionChanged = Signal()
    hourlySolarPowerGenerationChanged = Signal()

    def __init__(self,
        installed_capacity: Optional[InstalledCapacity] = None,
        ayer_keroh_site_conditions: Optional[AyerKerohSiteConditions] = None,
        solar_energy_production: Optional[SolarEnergyProduction] = None,
        hourly_solar_power_generation: Optional[HourlySolarPowerGeneration] = None
    ):
        super().__init__()
        self.installed_capacity: InstalledCapacity = InstalledCapacity() if installed_capacity is None else installed_capacity
        self.ayer_keroh_site_conditions: AyerKerohSiteConditions = AyerKerohSiteConditions() if ayer_keroh_site_conditions is None else ayer_keroh_site_conditions
        self.solar_energy_production: SolarEnergyProduction = SolarEnergyProduction() if solar_energy_production is None else solar_energy_production
        self.hourly_solar_power_generation: HourlySolarPowerGeneration = HourlySolarPowerGeneration() if hourly_solar_power_generation is None else hourly_solar_power_generation

        self.ayer_keroh_site_conditions.specificPvPowerOutputPerYearChanged.connect(self.update_solarEnergyProduction_specificYield)

        self.ayer_keroh_site_conditions.specificPvPowerOutputPerDayChanged.connect(self.update_solarEnergyProduction_estimatedGenerationPerDay)
        self.installed_capacity.installedCapacityChanged.connect(self.update_solarEnergyProduction_estimatedGenerationPerDay)
        self.solar_energy_production.boostInverterEfficiencyChanged.connect(self.update_solarEnergyProduction_estimatedGenerationPerDay)

        self.solar_energy_production.specificYieldChanged.connect(self.update_solarEnergyProduction_estimatedGenerationPerYear)
        self.installed_capacity.installedCapacityChanged.connect(self.update_solarEnergyProduction_estimatedGenerationPerYear)
        self.solar_energy_production.boostInverterEfficiencyChanged.connect(self.update_solarEnergyProduction_estimatedGenerationPerYear)

    def emitUpdateSignals(self):
        self.installed_capacity.emitUpdateSignals()
        self.ayer_keroh_site_conditions.emitUpdateSignals()
        self.solar_energy_production.emitUpdateSignals()
        self.hourly_solar_power_generation.emitUpdateSignals()

    @Property(InstalledCapacity, notify=installedCapacityChanged) #getter
    def installedCapacity(self) -> InstalledCapacity:
        return self.installed_capacity
        
    @Property(AyerKerohSiteConditions, notify=ayerKerohSiteConditionsChanged) #getter
    def ayerKerohSiteConditions(self) -> AyerKerohSiteConditions:
        return self.ayer_keroh_site_conditions

    @Property(SolarEnergyProduction, notify=solarEnergyProductionChanged) #getter
    def solarEnergyProduction(self) -> SolarEnergyProduction:
        return self.solar_energy_production

    @Property(HourlySolarPowerGeneration, notify=hourlySolarPowerGenerationChanged) #getter
    def hourlySolarPowerGeneration(self) -> HourlySolarPowerGeneration:
        return self.hourly_solar_power_generation        

    @Slot()
    def update_solarEnergyProduction_specificYield(self):
        if self.solar_energy_production.specific_yield != self.ayer_keroh_site_conditions.specific_pv_power_output_per_year:
            self.solar_energy_production.specific_yield = self.ayer_keroh_site_conditions.specific_pv_power_output_per_year
            self.solar_energy_production.specificYieldChanged.emit()

    @Slot()
    def update_solarEnergyProduction_estimatedGenerationPerDay(self):
        if (
            new_value := \
                self.ayer_keroh_site_conditions.specific_pv_power_output_per_day \
                * self.installed_capacity.installed_capacity \
                * self.solar_energy_production.boost_inverter_efficiency
        ) != self.solar_energy_production.estimated_generation_per_day:
            self.solar_energy_production.estimated_generation_per_day = new_value
            self.solar_energy_production.estimatedGenerationPerDayChanged.emit()


    @Slot()
    def update_solarEnergyProduction_estimatedGenerationPerYear(self):
        if (
            new_value := \
            self.solar_energy_production.specific_yield \
            * self.installed_capacity.installed_capacity \
            * self.solar_energy_production.boost_inverter_efficiency
        ) != self.solar_energy_production.estimated_generation_per_year:
            self.solar_energy_production.estimated_generation_per_year = new_value
            self.solar_energy_production.estimatedGenerationPerYearChanged.emit()
