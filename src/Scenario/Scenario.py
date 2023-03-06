from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .Year.Year import Year

class Scenario(QObject):
    yearsChanged = Signal()
    currentYearIndexChanged = Signal()

    def __init__(self, 
        name: str = None,
        years: list[Year]|None = None,
    ):
        super().__init__()
        self.current_year_index:int = 0

        self.years_: list[Year] = [Year()]*6 if years is None else years

        '''****************************************
                POST ASSIGNMENT UPDATE
        ****************************************'''
                                                           

        '''****************************************
                    CONNECTIONS
        ****************************************'''

    def emitUpdateSignals(self):
        self.yearsChanged.emit()
        for year in self.years_:
            year.emitUpdateSignals()

    @Property(list, notify=yearsChanged) #getter
    def years(self) -> list:
        return self.years_

    @years.setter
    def years(self, years_:list) -> None:
        self.years_ = years_
        self.yearsChanged.emit()       

    @Property(int, notify=currentYearIndexChanged) #getter
    def currentYearIndex(self) -> int:
        return self.current_year_index

    @currentYearIndex.setter
    def currentYearIndex(self, current_year_index:int) -> None:
        self.current_year_index = current_year_index
        self.currentYearIndexChanged.emit()                  
    '''****************************************
                    SLOTS
    ****************************************'''
   