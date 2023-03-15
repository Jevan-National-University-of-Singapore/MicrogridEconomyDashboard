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

    def __init__(self) -> None:
        super().__init__()
        self.power_max: float = 0
        self.power_continuous: float = 0.75 * self.power_max

        '''****************************************
                    CONNECTIONS
        ****************************************'''   
        self.powerMaxChanged.connect(self.updatePowerContinuous)

    def emitUpdateSignals(self):
        self.powerContinuousChanged.emit()
        self.powerMaxChanged.emit()
        
    ''' *****************************************************
                QML(UI) getters and setters (front-end)
    ***************************************************** '''
    # ======== Power Continuous ========
    @Property(float, notify=powerContinuousChanged) #getter
    def powerContinuous(self) -> float:
        return self.power_continuous

    @powerContinuous.setter #setter
    def powerContinuous(self, power_continuous:float) -> None:
        if self.power_continuous != power_continuous:
            self.power_continuous = power_continuous
            self.powerContinuousChanged.emit()

    # ======== Power Max ========
    @Property(float, notify=powerMaxChanged) #getter
    def powerMax(self) -> float:
        return self.power_max

    @powerMax.setter #setter
    def powerMax(self, power_max:float) -> None:
        if self.power_max != power_max:
            self.power_max = power_max
            self.powerMaxChanged.emit()

    @Slot()
    def updatePowerContinuous(self):
        if (new_value := self.power_max * 0.75) != self.power_continuous:
            self.power_continuous = new_value
            self.powerContinuousChanged.emit()