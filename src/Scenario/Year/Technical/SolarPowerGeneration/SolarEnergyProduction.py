from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class SolarEnergyProduction(QObject):
    specificYieldChanged = Signal()
    boostInverterEfficiencyChanged = Signal()
    estimatedGenerationPerDayChanged = Signal()
    estimatedGenerationPerYearChanged = Signal()
    hourlySolarPowerGenerationChanged = Signal()

    def __init__(self, boost_inverter_efficiency: float = 0.9, estimated_generation_per_day: float = 86.99):
        super().__init__()
        self.specific_yield:float = 0
        self.boost_inverter_efficiency:float = boost_inverter_efficiency
        self.estimated_generation_per_day:float = estimated_generation_per_day
        self.estimated_generation_per_year:float = 0

    def emitUpdateSignals(self):        
        self.specificYieldChanged.emit()
        self.boostInverterEfficiencyChanged.emit()
        self.estimatedGenerationPerDayChanged.emit()
        self.estimatedGenerationPerYearChanged.emit()
        self.hourlySolarPowerGenerationChanged.emit()

    @Property(float, notify=specificYieldChanged) #getter
    def specificYield(self) -> float:
        return self.specific_yield

    @specificYield.setter
    def specificYield(self, specific_yield:float) -> None:
        if self.specific_yield != specific_yield:
            self.specific_yield = specific_yield
            self.specificYieldChanged.emit()

    @Property(float, notify=boostInverterEfficiencyChanged) #getter
    def boostInverterEfficiency(self) -> float:
        return self.boost_inverter_efficiency

    @boostInverterEfficiency.setter
    def boostInverterEfficiency(self, boost_inverter_efficiency:float) -> None:
        if self.boost_inverter_efficiency != boost_inverter_efficiency:
            self.boost_inverter_efficiency = boost_inverter_efficiency
            self.boostInverterEfficiencyChanged.emit()

    @Property(float, notify=estimatedGenerationPerDayChanged) #getter
    def estimatedGenerationPerDay(self) -> float:
        return self.estimated_generation_per_day

    @estimatedGenerationPerDay.setter
    def estimatedGenerationPerDay(self, estimated_generation_per_day:float) -> None:
        if self.estimated_generation_per_day != estimated_generation_per_day:
            self.estimated_generation_per_day = estimated_generation_per_day
            self.estimatedGenerationPerDayChanged.emit()

    @Property(float, notify=estimatedGenerationPerYearChanged) #getter
    def estimatedGenerationPerYear(self) -> float:
        return self.estimated_generation_per_year

    @estimatedGenerationPerYear.setter
    def estimatedGenerationPerYear(self, estimated_generation_per_year:float) -> None:
        if self.estimated_generation_per_year != estimated_generation_per_year:
            self.estimated_generation_per_year = estimated_generation_per_year
            self.estimatedGenerationPerYearChanged.emit()