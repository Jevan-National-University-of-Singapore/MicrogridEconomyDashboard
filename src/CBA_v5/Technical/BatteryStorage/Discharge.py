from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Discharge(QObject):
    ''' ************************************************************************
                                    Discharge

    All properties are read-only, user should not need to input anything here
    ************************************************************************ '''
    powerContinuousChanged = Signal()
    powerMaxChanged = Signal()

    def __init__(self, power_continuous:float=0, power_max:float=0) -> None:
        super().__init__()
        self._power_continuous = power_continuous
        self._power_max = power_max

    # ======== Power Continuous ========
    @Property(str, notify=powerContinuousChanged) #getter
    def powerContinuous(self) -> str:
        return str(self._power_continuous)

    @powerContinuous.setter #setter
    def powerContinuous(self, value:str) -> None:
        self._power_continuous = float(value)

    # ======== Power Max ========
    @Property(str, notify=powerMaxChanged) #getter
    def powerMax(self) -> str:
        return str(self._power_max)

    @powerMax.setter #setter
    def powerMax(self, value:str) -> None:
        self._power_max = float(value)