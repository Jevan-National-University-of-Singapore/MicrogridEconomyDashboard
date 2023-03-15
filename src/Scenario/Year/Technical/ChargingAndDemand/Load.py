from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Load(QObject):
    requiredEnergyPerUserChanged = Signal()
    requiredEnergyPerDayChanged = Signal()
    requiredEnergyPerYearChanged = Signal()

    def __init__(self):
        super().__init__()
        self.required_energy_per_user:float = 0
        self.required_energy_per_day:float = 0
        self.required_energy_per_year:float = self.required_energy_per_day * 365

        '''****************************************
                    CONNECTIONS
        ****************************************'''  
        self.requiredEnergyPerDayChanged.connect(self.updateRequiredEnergyPerYear)

    def emitUpdateSignals(self):
        self.requiredEnergyPerUserChanged.emit()
        self.requiredEnergyPerDayChanged.emit()
        self.requiredEnergyPerYearChanged.emit()        

    @Property(float, notify=requiredEnergyPerUserChanged) #getter
    def requiredEnergyPerUser(self) -> float:
        return self.required_energy_per_user

    @requiredEnergyPerUser.setter
    def requiredEnergyPerUser(self, required_energy_per_user:float):
        if self.required_energy_per_user != required_energy_per_user:
            self.required_energy_per_user = required_energy_per_user
            self.requiredEnergyPerUserChanged.emit()

    @Property(float, notify=requiredEnergyPerDayChanged) #getter
    def requiredEnergyPerDay(self) -> float:
        return self.required_energy_per_day

    @requiredEnergyPerDay.setter
    def requiredEnergyPerDay(self, required_energy_per_day:float):
        if self.required_energy_per_day != required_energy_per_day:
            self.required_energy_per_day = required_energy_per_day
            self.requiredEnergyPerDayChanged.emit()
    
    @Property(float, notify=requiredEnergyPerYearChanged) #getter
    def requiredEnergyPerYear(self) -> float:
        return self.required_energy_per_year

    @requiredEnergyPerYear.setter
    def requiredEnergyPerYear(self, required_energy_per_year:float):
        if self.required_energy_per_year != required_energy_per_year:
            self.required_energy_per_year = required_energy_per_year
            self.requiredEnergyPerYearChanged.emit()

    @Slot()
    def updateRequiredEnergyPerYear(self):
        if (new_value := self.required_energy_per_day * 365) != self.required_energy_per_year:
            self.required_energy_per_year = new_value
            self.requiredEnergyPerYearChanged.emit()