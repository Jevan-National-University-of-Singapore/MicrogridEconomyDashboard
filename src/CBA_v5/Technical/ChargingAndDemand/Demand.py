from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Demand(QObject):
    numOfUsersPerDayChanged = Signal()
    numOfUsersPerYearChanged = Signal()

    stateOfChargeAtEntryChanged = Signal()
    stateOfChargeLimitChanged = Signal()
    stateOfChargeToBeChargedChanged = Signal()

    totalWaitingTimeChanged = Signal()
    actualUsersServedPerDayChanged = Signal()
    actualEnergyServedPerDayChanged = Signal()

    def __init__(self,
        # required
        state_of_charge_at_entry:float = 0.2,
        state_of_charge_limit:float = 0.8,

        # optional
        num_of_users_per_day:int = 17,

        total_waiting_time:float = 0,
        actual_users_served_per_day:int = 17,
        actual_energy_served_per_day:float = 550.8
    ):
        super().__init__()
        self.num_of_users_per_day = num_of_users_per_day
        self.num_of_users_per_year = num_of_users_per_day * 365

        self.state_of_charge_at_entry = state_of_charge_at_entry
        self.state_of_charge_limit = state_of_charge_limit
        self.state_of_charge_to_be_charged = state_of_charge_limit - state_of_charge_at_entry

        self.total_waiting_time = total_waiting_time
        self.actual_users_served_per_day = actual_users_served_per_day
        self.actual_energy_served_per_day = actual_energy_served_per_day

        self.state_of_charge_to_be_charged = self.state_of_charge_limit - self.state_of_charge_at_entry
        self.num_of_users_per_year = self.num_of_users_per_day * 365

        self.stateOfChargeLimitChanged.connect(self.updateStateOfChargeToBeCharged)
        self.numOfUsersPerDayChanged.connect(self.updateNumOfUsersPerYear)

    def emitUpdateSignals(self):
        self.numOfUsersPerDayChanged.emit()
        self.numOfUsersPerYearChanged.emit()

        self.stateOfChargeAtEntryChanged.emit()
        self.stateOfChargeLimitChanged.emit()
        self.stateOfChargeToBeChargedChanged.emit()

        self.totalWaitingTimeChanged.emit()
        self.actualUsersServedPerDayChanged.emit()
        self.actualEnergyServedPerDayChanged.emit()

    @Property(str, notify=numOfUsersPerDayChanged) #getter
    def numOfUsersPerDay(self) -> str:
        return str(self.num_of_users_per_day)

    @numOfUsersPerDay.setter
    def numOfUsersPerDay(self, num_of_users_per_day:str):
        self.num_of_users_per_day = int(num_of_users_per_day)
        self.numOfUsersPerDayChanged.emit()

    @Property(str, notify=numOfUsersPerYearChanged) #getter
    def numOfUsersPerYear(self) -> str:
        return str(self.num_of_users_per_year)

    @numOfUsersPerYear.setter
    def numOfUsersPerYear(self, num_of_users_per_year:str):
        self.num_of_users_per_year = int(num_of_users_per_year)
        self.numOfUsersPerYearChanged.emit()
    
    @Property(str, notify=stateOfChargeAtEntryChanged) #getter
    def stateOfChargeAtEntry(self) -> str:
        return str(round(self.state_of_charge_at_entry*100, 2))

    @stateOfChargeAtEntry.setter
    def stateOfChargeAtEntry(self, state_of_charge_at_entry:str):
        self.state_of_charge_at_entry = round(float(state_of_charge_at_entry)/100, 4)
        self.stateOfChargeAtEntryChanged.emit()
    
    @Property(str, notify=stateOfChargeLimitChanged) #getter
    def stateOfChargeLimit(self) -> str:
        return str(round(self.state_of_charge_limit*100, 2))

    @stateOfChargeLimit.setter
    def stateOfChargeLimit(self, state_of_charge_limit:str):
        self.state_of_charge_limit = round(float(state_of_charge_limit)/100, 4)
        self.stateOfChargeLimitChanged.emit()
    
    @Property(str, notify=stateOfChargeToBeChargedChanged) #getter
    def stateOfChargeToBeCharged(self) -> str:
        return str(round(self.state_of_charge_to_be_charged * 100, 2))

    @stateOfChargeToBeCharged.setter
    def stateOfChargeToBeCharged(self, state_of_charge_to_be_charged:str):
        self.state_of_charge_to_be_charged = round(float(state_of_charge_to_be_charged)/100, 4)
        self.stateOfChargeToBeChargedChanged.emit()
    
    @Property(str, notify=totalWaitingTimeChanged) #getter
    def totalWaitingTime(self) -> str:
        return str(self.total_waiting_time)

    @totalWaitingTime.setter
    def totalWaitingTime(self, total_waiting_time:str):
        self.total_waiting_time = round(float(total_waiting_time), 2)
        self.totalWaitingTimeChanged.emit()
    
    @Property(str, notify=actualUsersServedPerDayChanged) #getter
    def actualUsersServedPerDay(self) -> str:
        return str(self.actual_users_served_per_day)

    @actualUsersServedPerDay.setter
    def actualUsersServedPerDay(self, actual_users_served_per_day:str):
        self.actual_users_served_per_day = int(actual_users_served_per_day)
        self.actualUsersServedPerDayChanged.emit()
    
    @Property(str, notify=actualEnergyServedPerDayChanged) #getter
    def actualEnergyServedPerDay(self) -> str:
        return str(self.actual_energy_served_per_day)

    @actualEnergyServedPerDay.setter
    def actualEnergyServedPerDay(self, actual_energy_served_per_day:str):
        self.actual_energy_served_per_day = round(float(actual_energy_served_per_day), 2)
        self.actualEnergyServedPerDayChanged.emit()

    @Slot()
    def updateStateOfChargeToBeCharged(self):
        self.state_of_charge_to_be_charged = round(self.state_of_charge_limit - self.state_of_charge_at_entry, 2)
        self.stateOfChargeToBeChargedChanged.emit()

    @Slot()
    def updateNumOfUsersPerYear(self):
        self.num_of_users_per_year = round(self.num_of_users_per_day * 365, 2)
        self.numOfUsersPerYearChanged.emit()



