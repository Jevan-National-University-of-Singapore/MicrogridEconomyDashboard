from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Year(QObject):
    numberOfUsersPerDayChanged = Signal()
    
    usersPerHourChanged = Signal()
    usersPerHourElementChanged = Signal(int)

    def __init__(self,
        number_of_users_per_day: int = 17,
    ):
        super().__init__()
        self.number_of_users_per_day:int = number_of_users_per_day
    
        self.users_per_hour = [0] * 24

        self.updateUsersPerHour()

        self.numberOfUsersPerDayChanged.connect(self.updateUsersPerHour)

    def emitUpdateSignals(self):
        self.numberOfUsersPerDayChanged.emit()
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

    @Slot()
    def updateUsersPerHour(self):
        self.setUsersPerHourElement(8, 1 if self.number_of_users_per_day > 0 else 0)
        self.setUsersPerHourElement(7, 1 if self.number_of_users_per_day > 14 else 0)
        self.setUsersPerHourElement(6, 1 if self.number_of_users_per_day > 15 else 0)
        self.setUsersPerHourElement(5, 1 if self.number_of_users_per_day > 16 else 0)
        self.setUsersPerHourElement(22, 1 if self.number_of_users_per_day > 17 else 0)
        self.setUsersPerHourElement(23, 1 if self.number_of_users_per_day > 18 else 0)

        for i in range(9, 22):
            self.setUsersPerHourElement(i, 1 if self.number_of_users_per_day > i-8 else 0)
                
