from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Demand(QObject):
    numOfUsersPerDayChanged = Signal()
    numOfUsersPerYearChanged = Signal()
    additionalNumberOfUsersPerYearChanged = Signal()

    usersPerHourChanged = Signal()
    usersPerHourElementChanged = Signal(int)

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
        number_of_users_per_day:int = 17,
        additional_number_of_users_per_year: int = 2,

        total_waiting_time:float = 0,
        actual_users_served_per_day:int = 17,
        actual_energy_served_per_day:float = 550.8
    ):
        super().__init__()
        self.number_of_users_per_day = number_of_users_per_day
        self.users_per_hour = [0] * 24
        self.num_of_users_per_year = number_of_users_per_day * 365
        self.additional_number_of_users_per_year: int = additional_number_of_users_per_year

        self.state_of_charge_at_entry = state_of_charge_at_entry
        self.state_of_charge_limit = state_of_charge_limit
        self.state_of_charge_to_be_charged = state_of_charge_limit - state_of_charge_at_entry

        self.total_waiting_time = total_waiting_time
        self.actual_users_served_per_day = actual_users_served_per_day
        self.actual_energy_served_per_day = actual_energy_served_per_day

        self.state_of_charge_to_be_charged = self.state_of_charge_limit - self.state_of_charge_at_entry
        self.num_of_users_per_year = self.number_of_users_per_day * 365

        self.numOfUsersPerDayChanged.connect(self.updateUsersPerHour)

        self.stateOfChargeLimitChanged.connect(self.updateStateOfChargeToBeCharged)
        self.stateOfChargeAtEntryChanged.connect(self.updateStateOfChargeToBeCharged)

        self.numOfUsersPerDayChanged.connect(self.updateNumOfUsersPerYear)

    def emitUpdateSignals(self):
        self.numOfUsersPerDayChanged.emit()
        self.numOfUsersPerYearChanged.emit()
        self.additionalNumberOfUsersPerYearChanged.emit()

        self.stateOfChargeAtEntryChanged.emit()
        self.stateOfChargeLimitChanged.emit()
        self.stateOfChargeToBeChargedChanged.emit()

        self.totalWaitingTimeChanged.emit()
        self.actualUsersServedPerDayChanged.emit()
        self.actualEnergyServedPerDayChanged.emit()

        for i in range(24):
            self.usersPerHourElementChanged.emit(i)        

    @Property(str, notify=numOfUsersPerDayChanged) #getter
    def numOfUsersPerDay(self) -> str:
        return str(self.number_of_users_per_day)

    @numOfUsersPerDay.setter
    def numOfUsersPerDay(self, num_of_users_per_day:str):
        self.number_of_users_per_day = int(num_of_users_per_day)
        self.numOfUsersPerDayChanged.emit()

    @Property(list, notify=usersPerHourChanged) #getter
    def usersPerHour(self) -> list:
        return self.users_per_hour

    @usersPerHour.setter
    def usersPerHour(self, users_per_hour:list):
        self.users_per_hour = users_per_hour
        self.usersPerHourChanged.emit()       

    @Slot(int, int)
    def setUsersPerHourElement(self, index:int, number_of_users:int):
        # if self.users_per_hour[index] != number_of_users:
        self.users_per_hour[index] = number_of_users
        self.usersPerHourElementChanged.emit(index)
        self.usersPerHourChanged.emit()

   
    @Property(str, notify=numOfUsersPerYearChanged) #getter
    def numOfUsersPerYear(self) -> str:
        return str(self.num_of_users_per_year)

    @numOfUsersPerYear.setter
    def numOfUsersPerYear(self, num_of_users_per_year:str):
        self.num_of_users_per_year = int(num_of_users_per_year)
        self.numOfUsersPerYearChanged.emit()

    @Property(int, notify=additionalNumberOfUsersPerYearChanged) #getter
    def additionalNumberOfUsersPerYear(self) -> int:
        return self.additional_number_of_users_per_year

    @additionalNumberOfUsersPerYear.setter
    def additionalNumberOfUsersPerYear(self, additional_number_of_users_per_year:int) -> None:
        self.additional_number_of_users_per_year = additional_number_of_users_per_year
        self.additionalNumberOfUsersPerYearChanged.emit()        
    
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
        self.num_of_users_per_year = round(self.number_of_users_per_day * 365, 2)
        self.numOfUsersPerYearChanged.emit()

    @Slot()
    def updateUsersPerHour(self):
        #update in order
        self.setUsersPerHourElement(8, 1 if self.number_of_users_per_day > 0 else 0)
        self.setUsersPerHourElement(7, 1 if self.number_of_users_per_day > 14 else 0)
        self.setUsersPerHourElement(6, 1 if self.number_of_users_per_day > 15 else 0)
        self.setUsersPerHourElement(5, 1 if self.number_of_users_per_day > 16 else 0)
        for i in range(9, 22):
            self.setUsersPerHourElement(i, 1 if self.number_of_users_per_day > i-8 else 0)
        self.setUsersPerHourElement(22, 1 if self.number_of_users_per_day > 17 else 0)
        self.setUsersPerHourElement(23, 1 if self.number_of_users_per_day > 18 else 0)        



