from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class ChargingAndDemand(QObject):
    numberOfUsersPerDayChanged = Signal()
    additionalNumberOfUsersPerYearChanged = Signal()
    usersPerHourChanged = Signal()

    def __init__(self,
        number_of_users_per_day: int = 17,
        additional_number_of_users_per_year: int = 0
    ):
        super().__init__()
        self.number_of_users_per_day:int = number_of_users_per_day
        self.additional_number_of_users_per_year: int = additional_number_of_users_per_year
    
        self.users_per_hour = [0] * 24

        self.updateUsersPerHour()

        self.numberOfUsersPerDayChanged.connect(self.updateUsersPerHour)

    def emitUpdateSignals(self):
        self.numberOfUsersPerDayChanged.emit()
        self.additionalNumberOfUsersPerYearChanged.emit()
        self.usersPerHourChanged.emit()


    @Property(str, notify=numberOfUsersPerDayChanged) #getter
    def numberOfUsersPerDay(self) -> str:
        return str(self.number_of_users_per_day)

    @numberOfUsersPerDay.setter
    def numberOfUsersPerDay(self, number_of_users_per_day:str):
        num = int(number_of_users_per_day)
        if num != self.number_of_users_per_day:
            self.number_of_users_per_day = num
            self.numberOfUsersPerDayChanged.emit()
        
    @Property(str, notify=additionalNumberOfUsersPerYearChanged) #getter
    def additionalNumberOfUsersPerYear(self) -> str:
        return str(self.additional_number_of_users_per_year)

    @additionalNumberOfUsersPerYear.setter
    def additionalNumberOfUsersPerYear(self, additional_number_of_users_per_year:str):
        self.additional_number_of_users_per_year = int(additional_number_of_users_per_year)
        self.additionalNumberOfUsersPerYearChanged.emit()

    @Property(list, notify=usersPerHourChanged) #getter
    def usersPerHour(self) -> list:
        return self.users_per_hour

    @usersPerHour.setter
    def usersPerHour(self, users_per_hour:list):
        self.users_per_hour = users_per_hour
        self.usersPerHourChanged.emit()        

    @Slot()
    def updateUsersPerHour(self):
        self.users_per_hour[8] = 1 if self.number_of_users_per_day > 0 else 0
        self.users_per_hour[7] = 1 if self.number_of_users_per_day > 14 else 0
        self.users_per_hour[6] = 1 if self.number_of_users_per_day > 15 else 0
        self.users_per_hour[5] = 1 if self.number_of_users_per_day > 16 else 0
        self.users_per_hour[22] = 1 if self.number_of_users_per_day > 17 else 0
        self.users_per_hour[23] = 1 if self.number_of_users_per_day > 18 else 0

        for i in range(9, 22):
            self.users_per_hour[i] = 1 if self.number_of_users_per_day > i-8 else 0
                
        self.usersPerHourChanged.emit()

