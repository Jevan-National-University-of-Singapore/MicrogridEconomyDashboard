from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .Breakeven.Breakeven import Breakeven
# from .AyerKerohSiteConditions import AyerKerohSiteConditions
# from .SolarEnergyProduction import SolarEnergyProduction
# from .HourlySolarPowerGeneration import HourlySolarPowerGeneration

class FiveYearAnalysis(QObject):
    breakevenChanged = Signal()
    def __init__(self):
        super().__init__()
        self.breakeven_:Breakeven = Breakeven()

    def emitUpdateSignals(self):
        self.breakeven_.emitUpdateSignals
        self.breakevenChanged.emit()

    @Property(Breakeven, notify=breakevenChanged) #getter
    def breakeven(self) -> Breakeven:
        return self.breakeven_         