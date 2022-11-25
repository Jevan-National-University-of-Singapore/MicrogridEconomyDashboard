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

    def __init__(self, power_max:float=354) -> None:
        super().__init__()
        self.power_max = power_max
        self.power_continuous = 0.75 * power_max

    def emitUpdateSignals(self):
        self.powerContinuousChanged.emit()
        self.powerMaxChanged.emit()
        
    ''' *****************************************************
                QML(UI) getters and setters (front-end)
    ***************************************************** '''
    # ======== Power Continuous ========
    @Property(str, notify=powerContinuousChanged) #getter
    def powerContinuous(self) -> str:
        return str(self.power_continuous)

    @powerContinuous.setter #setter
    def powerContinuous(self, value:str) -> None:
        self.power_continuous = float(value)
        self.powerContinuousChanged.emit()

    # ======== Power Max ========
    @Property(str, notify=powerMaxChanged) #getter
    def powerMax(self) -> str:
        return str(self.power_max)

    @powerMax.setter #setter
    def powerMax(self, value:str) -> None:
        self.power_max = float(value)
        self.powerMaxChanged.emit()

    @Slot()
    def updatePowerContinuous(self):
        self.powerContinuous = self.power_max * 0.75