from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .InstalledCapacity import InstalledCapacity
from .AyerKerohSiteConditions import AyerKerohSiteConditions
from .SolarEnergyProduction import SolarEnergyProduction

class SolarPowerGeneration(QObject):
    installedCapacityChanged = Signal()
    ayerKerohSiteConditionsChanged = Signal()
    solarEnergyProductionChanged = Signal()

    def __init__(self,
        installed_capacity: InstalledCapacity = InstalledCapacity(),
        ayer_keroh_site_conditions: AyerKerohSiteConditions = AyerKerohSiteConditions(),
        solar_energy_production: SolarEnergyProduction = SolarEnergyProduction()
    ):
        super().__init__()
        self.installed_capacity: InstalledCapacity = installed_capacity
        self.ayer_keroh_site_conditions: AyerKerohSiteConditions = ayer_keroh_site_conditions
        self.solar_energy_production: SolarEnergyProduction = solar_energy_production

        self.solar_energy_production.specific_yield = round(self.ayer_keroh_site_conditions.specific_pv_power_output_per_year, 2)

        self.solar_energy_production.estimated_generation_per_day = round(
            self.ayer_keroh_site_conditions.specific_pv_power_output_per_day
                * self.installed_capacity.installed_capacity
                * self.solar_energy_production.boost_inverter_efficiency,
            2)


        self.solar_energy_production.estimated_generation_per_year = round(
            self.solar_energy_production.specific_yield
                * self.installed_capacity.installed_capacity
                * self.solar_energy_production.boost_inverter_efficiency,
            2)

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

    @Property(InstalledCapacity, notify=installedCapacityChanged) #getter
    def installedCapacity(self) -> InstalledCapacity:
        return self.installed_capacity
        
    @Property(AyerKerohSiteConditions, notify=ayerKerohSiteConditionsChanged) #getter
    def ayerKerohSiteConditions(self) -> AyerKerohSiteConditions:
        return self.ayer_keroh_site_conditions

    @Property(SolarEnergyProduction, notify=solarEnergyProductionChanged) #getter
    def solarEnergyProduction(self) -> SolarEnergyProduction:
        return self.solar_energy_production

    @Slot()
    def update_solarEnergyProduction_specificYield(self):
        self.solar_energy_production.specific_yield = round(self.ayer_keroh_site_conditions.specific_pv_power_output_per_year, 2)
        self.solar_energy_production.specificYieldChanged.emit()

    @Slot()
    def update_solarEnergyProduction_estimatedGenerationPerDay(self):
        self.solar_energy_production.estimated_generation_per_day = round(
            self.ayer_keroh_site_conditions.specific_pv_power_output_per_day
                * self.installed_capacity.installed_capacity
                * self.solar_energy_production.boost_inverter_efficiency,
            2)
        self.solar_energy_production.estimatedGenerationPerDayChanged.emit()


    @Slot()
    def update_solarEnergyProduction_estimatedGenerationPerYear(self):
        self.solar_energy_production.estimated_generation_per_year = round(
            self.solar_energy_production.specific_yield
                * self.installed_capacity.installed_capacity
                * self.solar_energy_production.boost_inverter_efficiency,
            2)
        self.solar_energy_production.estimatedGenerationPerYearChanged.emit()