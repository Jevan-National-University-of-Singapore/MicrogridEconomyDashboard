from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .Year import Year


class ChargingAndDemand(QObject):
    yearsChanged = Signal()
    additionalNumberOfUsersPerYearChanged = Signal()

    def __init__(self,
        years: list[Year] = [Year(), Year(), Year(), Year(), Year()],
        additional_number_of_users_per_year: int = 2
    ):
        super().__init__()

        for year_index, year in enumerate(years[1:]):
            year.number_of_users_per_day = years[0].number_of_users_per_day + ((year_index+1) * additional_number_of_users_per_year)
            
        self.years_ = years
        self.additional_number_of_users_per_year: int = additional_number_of_users_per_year

        self.years_[0].numberOfUsersPerDayChanged.connect(self.update_years_numberOfUsersPerDay)
        self.additionalNumberOfUsersPerYearChanged.connect(self.update_years_numberOfUsersPerDay)

    def emitUpdateSignals(self):
        for year in self.years_:
            year.emitUpdateSignals()

        self.yearsChanged.emit()

    @Property(list, notify=yearsChanged) #getter
    def years(self) -> list:
        return self.years_

    @years.setter
    def years(self, years:list[Year]) -> None:
        self.years_ = years
        self.yearsChanged.emit()

    @Property(int, notify=additionalNumberOfUsersPerYearChanged) #getter
    def additionalNumberOfUsersPerYear(self) -> int:
        return self.additional_number_of_users_per_year

    @additionalNumberOfUsersPerYear.setter
    def additionalNumberOfUsersPerYear(self, additional_number_of_users_per_year:int) -> None:
        self.additional_number_of_users_per_year = additional_number_of_users_per_year
        self.additionalNumberOfUsersPerYearChanged.emit()       

    @Slot()
    def update_years_numberOfUsersPerDay(self):
        for year_index, year in enumerate(self.years_[1:]):
            new_value: int = self.years_[0].number_of_users_per_day + ((year_index+1) * self.additional_number_of_users_per_year)
            year.number_of_users_per_day = new_value
            year.numberOfUsersPerDayChanged.emit()
