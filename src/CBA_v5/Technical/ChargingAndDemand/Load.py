from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Load(QObject):
    requiredEnergyPerUserChanged = Signal()
    requiredEnergyPerDayChanged = Signal()
    requiredEnergyPerYearChanged = Signal()

    def __init__(self,
        # required
        required_energy_per_user:float,
        required_energy_per_day:float
    ):
        super().__init__()
        self._required_energy_per_user = required_energy_per_user
        self._required_energy_per_day = required_energy_per_day
        self._required_energy_per_year = required_energy_per_day * 365

    @Property(str, notify=requiredEnergyPerUserChanged) #getter
    def requiredEnergyPerUser(self) -> str:
        return str(self._required_energy_per_user)

    @requiredEnergyPerUser.setter
    def requiredEnergyPerUser(self, required_energy_per_user:str):
        self._required_energy_per_user = float(required_energy_per_user)

    @Property(str, notify=requiredEnergyPerDayChanged) #getter
    def requiredEnergyPerDay(self) -> str:
        return str(self._required_energy_per_day)

    @requiredEnergyPerDay.setter
    def requiredEnergyPerDay(self, required_energy_per_day:str):
        self._required_energy_per_day = float(required_energy_per_day)
        self._required_energy_per_year = self._required_energy_per_day * 365
    
    @Property(str, notify=requiredEnergyPerYearChanged) #getter
    def requiredEnergyPerYear(self) -> str:
        return str(self._required_energy_per_year)

    @requiredEnergyPerYear.setter
    def requiredEnergyPerYear(self, required_energy_per_year:str):
        self._required_energy_per_year = float(required_energy_per_year)