from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class ExcessToFacility(QObject):
    electricityPerDayChanged = Signal()
    electricityPerYearChanged = Signal()

    def __init__(self,
        # required
        electricity_per_day:float = 550.8
    ):
        super().__init__()
        self.electricity_per_day = electricity_per_day

        self.electricity_per_year = round(self.electricity_per_day * 365)

        self.electricityPerDayChanged.connect(self.updateElectricityPerYear)

    def emitUpdateSignals(self):
        self.electricityPerDayChanged.emit()
        self.electricityPerYearChanged.emit()

    @Property(str, notify=electricityPerDayChanged) #getter
    def electricityPerDay(self) -> str:
        return str(self.electricity_per_day)

    @electricityPerDay.setter
    def electricityPerDay(self, electricity_per_day:str):
        self.electricity_per_day = round(float(electricity_per_day))
        self.electricityPerDayChanged.emit()

    @Property(str, notify=electricityPerYearChanged) #getter
    def electricityPerYear(self) -> str:
        return str(self.electricity_per_year)

    @electricityPerYear.setter
    def electricityPerYear(self, electricity_per_year:str):
        self.electricity_per_year = round(float(electricity_per_year))
        self.electricityPerYearChanged.emit()

    @Slot()
    def updateElectricityPerYear(self):
        self.electricity_per_year = round(self.electricity_per_day * 365)
        self.electricityPerYearChanged.emit()