from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Demand(QObject):
    numberOfUsersPerDayChanged = Signal()
    numberOfUsersPerYearChanged = Signal()
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
        state_of_charge_at_entry:float = 0.2,
        state_of_charge_limit:float = 0.8,
        number_of_users_per_day:int = 17
    ):
        super().__init__()
        self.number_of_users_per_day:int = number_of_users_per_day
        self.users_per_hour:list[int] = [0] * 24
        self.number_of_users_per_year:int = number_of_users_per_day * 365
        self.additional_number_of_users_per_year: int = 0

        self.state_of_charge_at_entry:float = state_of_charge_at_entry
        self.state_of_charge_limit:float = state_of_charge_limit
        self.state_of_charge_to_be_charged:float = self.state_of_charge_limit - self.state_of_charge_at_entry

        self.total_waiting_time:float = 0
        self.actual_users_served_per_day:int = 0
        self.actual_energy_served_per_day:int = 0

        '''****************************************
                    CONNECTIONS
        ****************************************'''  
        self.numberOfUsersPerDayChanged.connect(self.updateUsersPerHour)

        self.stateOfChargeLimitChanged.connect(self.updateStateOfChargeToBeCharged)
        self.stateOfChargeAtEntryChanged.connect(self.updateStateOfChargeToBeCharged)

        self.numberOfUsersPerDayChanged.connect(self.updateNumOfUsersPerYear)

    def emitUpdateSignals(self):
        self.numberOfUsersPerDayChanged.emit()
        self.numberOfUsersPerYearChanged.emit()
        self.additionalNumberOfUsersPerYearChanged.emit()
        self.usersPerHourChanged.emit()
        self.stateOfChargeAtEntryChanged.emit()
        self.stateOfChargeLimitChanged.emit()
        self.stateOfChargeToBeChargedChanged.emit()
        self.totalWaitingTimeChanged.emit()
        self.actualUsersServedPerDayChanged.emit()
        self.actualEnergyServedPerDayChanged.emit()

        for i in range(24):
            self.usersPerHourElementChanged.emit(i)        

    @Property(int, notify=numberOfUsersPerDayChanged) #getter
    def numberOfUsersPerDay(self) -> int:
        return self.number_of_users_per_day

    @numberOfUsersPerDay.setter
    def numberOfUsersPerDay(self, num_of_users_per_day:int):
        if self.number_of_users_per_day != num_of_users_per_day:
            self.number_of_users_per_day = num_of_users_per_day
            self.numberOfUsersPerDayChanged.emit()

    @Property(list, notify=usersPerHourChanged) #getter
    def usersPerHour(self) -> list:
        return self.users_per_hour

    @usersPerHour.setter
    def usersPerHour(self, users_per_hour:list):
        self.users_per_hour = users_per_hour
        self.usersPerHourChanged.emit()       

    @Slot(int, int)
    def setUsersPerHourElement(self, index:int, number_of_users:int):
        if self.users_per_hour[index] != number_of_users:
            self.users_per_hour[index] = number_of_users
            self.usersPerHourElementChanged.emit(index)
            self.usersPerHourChanged.emit()

   
    @Property(int, notify=numberOfUsersPerYearChanged) #getter
    def numberOfUsersPerYear(self) -> int:
        return self.number_of_users_per_year

    @numberOfUsersPerYear.setter
    def numberOfUsersPerYear(self, number_of_users_per_year:int):
        if self.number_of_users_per_year != number_of_users_per_year:
            self.number_of_users_per_year = number_of_users_per_year
            self.numberOfUsersPerYearChanged.emit()

    @Property(int, notify=additionalNumberOfUsersPerYearChanged) #getter
    def additionalNumberOfUsersPerYear(self) -> int:
        return self.additional_number_of_users_per_year

    @additionalNumberOfUsersPerYear.setter
    def additionalNumberOfUsersPerYear(self, additional_number_of_users_per_year:int) -> None:
        if self.additional_number_of_users_per_year != additional_number_of_users_per_year:
            self.additional_number_of_users_per_year = additional_number_of_users_per_year
            self.additionalNumberOfUsersPerYearChanged.emit()        
    
    @Property(float, notify=stateOfChargeAtEntryChanged) #getter
    def stateOfChargeAtEntry(self) -> float:
        return self.state_of_charge_at_entry

    @stateOfChargeAtEntry.setter
    def stateOfChargeAtEntry(self, state_of_charge_at_entry:float):
        if self.state_of_charge_at_entry != state_of_charge_at_entry:
            self.state_of_charge_at_entry = state_of_charge_at_entry
            self.stateOfChargeAtEntryChanged.emit()
    
    @Property(float, notify=stateOfChargeLimitChanged) #getter
    def stateOfChargeLimit(self) -> float:
        return self.state_of_charge_limit

    @stateOfChargeLimit.setter
    def stateOfChargeLimit(self, state_of_charge_limit:float):
        if self.state_of_charge_limit != state_of_charge_limit:
            self.state_of_charge_limit = state_of_charge_limit
            self.stateOfChargeLimitChanged.emit()
    
    @Property(float, notify=stateOfChargeToBeChargedChanged) #getter
    def stateOfChargeToBeCharged(self) -> float:
        return self.state_of_charge_to_be_charged

    @stateOfChargeToBeCharged.setter
    def stateOfChargeToBeCharged(self, state_of_charge_to_be_charged:float):
        if self.state_of_charge_to_be_charged != state_of_charge_to_be_charged:
            self.state_of_charge_to_be_charged = state_of_charge_to_be_charged
            self.stateOfChargeToBeChargedChanged.emit()
    
    @Property(float, notify=totalWaitingTimeChanged) #getter
    def totalWaitingTime(self) -> float:
        return self.total_waiting_time

    @totalWaitingTime.setter
    def totalWaitingTime(self, total_waiting_time:float):
        if self.total_waiting_time != total_waiting_time:
            self.total_waiting_time = total_waiting_time
            self.totalWaitingTimeChanged.emit()
    
    @Property(int, notify=actualUsersServedPerDayChanged) #getter
    def actualUsersServedPerDay(self) -> int:
        return self.actual_users_served_per_day

    @actualUsersServedPerDay.setter
    def actualUsersServedPerDay(self, actual_users_served_per_day:int):
        if self.actual_users_served_per_day != actual_users_served_per_day:
            self.actual_users_served_per_day = actual_users_served_per_day
            self.actualUsersServedPerDayChanged.emit()
    
    @Property(float, notify=actualEnergyServedPerDayChanged) #getter
    def actualEnergyServedPerDay(self) -> float:
        return self.actual_energy_served_per_day

    @actualEnergyServedPerDay.setter
    def actualEnergyServedPerDay(self, actual_energy_served_per_day:float):
        if self.actual_energy_served_per_day != actual_energy_served_per_day:
            self.actual_energy_served_per_day = actual_energy_served_per_day
            self.actualEnergyServedPerDayChanged.emit()

    @Slot()
    def updateStateOfChargeToBeCharged(self):
        if (new_value := self.state_of_charge_limit - self.state_of_charge_at_entry) != self.state_of_charge_to_be_charged:
            self.state_of_charge_to_be_charged = new_value
            self.stateOfChargeToBeChargedChanged.emit()

    @Slot()
    def updateNumOfUsersPerYear(self):
        if (new_value := self.number_of_users_per_day * 365) != self.number_of_users_per_year:
            self.number_of_users_per_year = new_value
            self.numberOfUsersPerYearChanged.emit() 

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



