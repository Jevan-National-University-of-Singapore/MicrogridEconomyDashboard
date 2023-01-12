from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .Year.Year import Year

class FiveYearsAnalysis(QObject):
    yearsChanged = Signal()

    def __init__(self,
        years: list[Year]|None = None,# = [Year(), Year(), Year(), Year(), Year()],
    ):
        super().__init__()
        self.years_: list[Year] = [Year(), Year(), Year(), Year(), Year()] if years is None else years

    def emitUpdateSignals(self):
        for year in self.years_:
            year.emitUpdateSignals()

    @Property(list, notify=yearsChanged) #getter
    def years(self) -> list:
        return self.years_

    @years.setter
    def years(self, years_:list) -> None:
        self.years_ = years_
        self.yearsChanged.emit()     

