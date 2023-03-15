from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class ExcessToFacility(QObject):
    electricityPerDayChanged = Signal()
    electricityPerYearChanged = Signal()

    def __init__(self):
        super().__init__()
        self.electricity_per_day = 0
        self.electricity_per_year = self.electricity_per_day * 365

        '''****************************************
                    CONNECTIONS
        ****************************************'''  
        self.electricityPerDayChanged.connect(self.updateElectricityPerYear)

    def emitUpdateSignals(self):
        self.electricityPerDayChanged.emit()
        self.electricityPerYearChanged.emit()

    @Property(float, notify=electricityPerDayChanged) #getter
    def electricityPerDay(self) -> float:
        return self.electricity_per_day

    @electricityPerDay.setter
    def electricityPerDay(self, electricity_per_day:float):
        if self.electricity_per_day != electricity_per_day:
            self.electricity_per_day = electricity_per_day
            self.electricityPerDayChanged.emit()

    @Property(float, notify=electricityPerYearChanged) #getter
    def electricityPerYear(self) -> float:
        return self.electricity_per_year

    @electricityPerYear.setter
    def electricityPerYear(self, electricity_per_year:float):
        if self.electricity_per_year != electricity_per_year:
            self.electricity_per_year = electricity_per_year
            self.electricityPerYearChanged.emit()

    @Slot()
    def updateElectricityPerYear(self):
        if (new_value := self.electricity_per_day * 365) != self.electricity_per_year:
            self.electricity_per_year = new_value
            self.electricityPerYearChanged.emit()