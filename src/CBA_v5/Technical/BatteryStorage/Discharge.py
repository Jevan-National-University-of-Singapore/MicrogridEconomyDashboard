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

    def __init__(self, power_max:float=None) -> None:
        super().__init__()
        self._power_max = power_max
        self._power_continuous = 0.75 * power_max

    ''' *********************************************
            Python getters and setters (Backend)
    ********************************************* '''
    @property
    def power_max(self) -> float:
        return self._power_max

    @power_max.setter
    def power_max(self, value:float):
        self._power_max = value
        self.powerContinuous = 0.75 * value

    @property
    def power_continuous(self) -> float:
        return self._power_continuous

    @power_continuous.setter
    def power_continuous(self, value:float):
        self._power_continuous = value
        
    ''' *****************************************************
                QML(UI) getters and setters (front-end)
    ***************************************************** '''
    # ======== Power Continuous ========
    @Property(str, notify=powerContinuousChanged) #getter
    def powerContinuous(self) -> str:
        return str(self._power_continuous)

    @powerContinuous.setter #setter
    def powerContinuous(self, value:str) -> None:
        self._power_continuous = float(value)
        self.powerContinuous = 0.75 * value

    # ======== Power Max ========
    @Property(str, notify=powerMaxChanged) #getter
    def powerMax(self) -> str:
        return str(self._power_max)

    @powerMax.setter #setter
    def powerMax(self, value:str) -> None:
        self._power_max = float(value)