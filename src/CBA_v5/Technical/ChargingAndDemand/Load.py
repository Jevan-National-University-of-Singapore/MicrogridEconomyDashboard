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
        self._required_energy_per_user = required_energy_per_user
        self._required_energy_per_day = required_energy_per_day
        # self._required_energy_per_year = required_energy_per_day * 365

        self.requiredEnergyPerDayChanged.connect(self.updateRequiredEnergyPerYear)

    def emitUpdateSignals(self):
        self.requiredEnergyPerUserChanged.emit()
        self.requiredEnergyPerDayChanged.emit()
        self.requiredEnergyPerYearChanged.emit()        

    @Property(str, notify=requiredEnergyPerUserChanged) #getter
    def requiredEnergyPerUser(self) -> str:
        return str(self._required_energy_per_user)

    @requiredEnergyPerUser.setter
    def requiredEnergyPerUser(self, required_energy_per_user:str):
        self._required_energy_per_user = float(required_energy_per_user)
        self.requiredEnergyPerUserChanged.emit()

    @Property(str, notify=requiredEnergyPerDayChanged) #getter
    def requiredEnergyPerDay(self) -> str:
        return str(self._required_energy_per_day)

    @requiredEnergyPerDay.setter
    def requiredEnergyPerDay(self, required_energy_per_day:str):
        self._required_energy_per_day = float(required_energy_per_day)
        self.requiredEnergyPerDayChanged.emit()
    
    @Property(str, notify=requiredEnergyPerYearChanged) #getter
    def requiredEnergyPerYear(self) -> str:
        return str(self._required_energy_per_year)

    @requiredEnergyPerYear.setter
    def requiredEnergyPerYear(self, required_energy_per_year:str):
        self._required_energy_per_year = float(required_energy_per_year)
        self.requiredEnergyPerYearChanged.emit()

    @Slot()
    def updateRequiredEnergyPerYear(self):
        self._required_energy_per_year = self._required_energy_per_day * 365
        self.requiredEnergyPerYearChanged.emit()