from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Load(QObject):
    requiredEnergyPerUserChanged = Signal()
    requiredEnergyPerDayChanged = Signal()
    requiredEnergyPerYearChanged = Signal()

    def __init__(self,
        # required
        required_energy_per_user:float = 32.4,
        required_energy_per_day:float = 550.8
    ):
        super().__init__()
        self.required_energy_per_user = required_energy_per_user
        self.required_energy_per_day = required_energy_per_day
        
        self.required_energy_per_year = round(required_energy_per_day * 365, 2)

        self.requiredEnergyPerDayChanged.connect(self.updateRequiredEnergyPerYear)

    def emitUpdateSignals(self):
        self.requiredEnergyPerUserChanged.emit()
        self.requiredEnergyPerDayChanged.emit()
        self.requiredEnergyPerYearChanged.emit()        

    @Property(str, notify=requiredEnergyPerUserChanged) #getter
    def requiredEnergyPerUser(self) -> str:
        return str(self.required_energy_per_user)

    @requiredEnergyPerUser.setter
    def requiredEnergyPerUser(self, required_energy_per_user:str):
        self.required_energy_per_user = round(float(required_energy_per_user), 2)
        self.requiredEnergyPerUserChanged.emit()

    @Property(str, notify=requiredEnergyPerDayChanged) #getter
    def requiredEnergyPerDay(self) -> str:
        return str(self.required_energy_per_day)

    @requiredEnergyPerDay.setter
    def requiredEnergyPerDay(self, required_energy_per_day:str):
        self.required_energy_per_day = round(float(required_energy_per_day), 2)
        self.requiredEnergyPerDayChanged.emit()
    
    @Property(str, notify=requiredEnergyPerYearChanged) #getter
    def requiredEnergyPerYear(self) -> str:
        return str(self.required_energy_per_year)

    @requiredEnergyPerYear.setter
    def requiredEnergyPerYear(self, required_energy_per_year:str):
        self.required_energy_per_year = round(float(required_energy_per_year), 2)
        self.requiredEnergyPerYearChanged.emit()

    @Slot()
    def updateRequiredEnergyPerYear(self):
        self.required_energy_per_year = round(self.required_energy_per_day * 365, 2)
        self.requiredEnergyPerYearChanged.emit()