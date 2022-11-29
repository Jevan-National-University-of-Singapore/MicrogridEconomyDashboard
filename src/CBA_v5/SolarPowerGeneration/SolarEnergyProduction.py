from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class SolarEnergyProduction(QObject):
    specificYieldChanged = Signal()
    boostInverterEfficiencyChanged = Signal()
    estimatedGenerationPerDayChanged = Signal()
    estimatedGenerationPerYearChanged = Signal()

    def __init__(self,
        specific_yield: float = 1_306.7,
        boost_inverter_efficiency: float = 0.9,
        estimated_generation_per_day: float = 86.99,
        estimated_generation_per_year: float = 31_753
    ):
        super().__init__()
        self.specific_yield:float = specific_yield
        self.boost_inverter_efficiency:float = boost_inverter_efficiency
        self.estimated_generation_per_day:float = estimated_generation_per_day
        self.estimated_generation_per_year:float = estimated_generation_per_year

    def emitUpdateSignals(self):        
        self.specificYieldChanged.emit()
        self.boostInverterEfficiencyChanged.emit()
        self.estimatedGenerationPerDayChanged.emit()
        self.estimatedGenerationPerYearChanged.emit()

    @Property(str, notify=specificYieldChanged) #getter
    def specificYield(self) -> str:
        return str(self.specific_yield)

    @specificYield.setter
    def specificYield(self, specific_yield:str) -> None:
        self.specific_yield = round(float(specific_yield), 2)
        self.specificYieldChanged.emit()

    @Property(str, notify=boostInverterEfficiencyChanged) #getter
    def boostInverterEfficiency(self) -> str:
        return str(round(self.boost_inverter_efficiency*100, 2))

    @boostInverterEfficiency.setter
    def boostInverterEfficiency(self, boost_inverter_efficiency:str) -> None:
        self.boost_inverter_efficiency = round(float(boost_inverter_efficiency)/100, 4)
        self.boostInverterEfficiencyChanged.emit()

    @Property(str, notify=estimatedGenerationPerDayChanged) #getter
    def estimatedGenerationPerDay(self) -> str:
        return str(self.estimated_generation_per_day)

    @estimatedGenerationPerDay.setter
    def estimatedGenerationPerDay(self, estimated_generation_per_day:str) -> None:
        self.estimated_generation_per_day = round(float(estimated_generation_per_day), 2)
        self.estimatedGenerationPerDayChanged.emit()

    @Property(str, notify=estimatedGenerationPerYearChanged) #getter
    def estimatedGenerationPerYear(self) -> str:
        return str(self.estimated_generation_per_year)

    @estimatedGenerationPerYear.setter
    def estimatedGenerationPerYear(self, estimated_generation_per_year:str) -> None:
        self.estimated_generation_per_year = round(float(estimated_generation_per_year), 2)
        self.estimatedGenerationPerYearChanged.emit()