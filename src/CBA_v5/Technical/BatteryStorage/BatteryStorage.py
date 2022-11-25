from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .EssSystem import EssSystem
from .Discharge import Discharge
from .GridCharging import GridCharging

class BatteryStorage(QObject):
    
    essSystemChanged = Signal()
    dischargeChanged = Signal()
    gridChargingChanged = Signal()

    def __init__(self, 
        ess_system: EssSystem = EssSystem(),
        discharge: Discharge = Discharge(),
        grid_charging: GridCharging = GridCharging()

    ):
        super().__init__()
        self.ess_system = EssSystem()
        self.discharge_ = Discharge()
        self.grid_charging = GridCharging()

        self.ess_system.installedCapacityChanged.connect(self.updateDischargePowerMax)

    def emitUpdateSignals(self):
        self.ess_system.emitUpdateSignals()
        self.discharge_.emitUpdateSignals()
        self.grid_charging.emitUpdateSignals()


    @Property(EssSystem, notify=essSystemChanged) #getter
    def essSystem(self) -> EssSystem:
        return self.ess_system

    @Property(Discharge, notify=dischargeChanged) #getter
    def discharge(self) -> Discharge:
        return self.discharge_

    @Property(GridCharging, notify=gridChargingChanged) #getter
    def gridCharging(self) -> GridCharging:
        return self.grid_charging

    @Slot()
    def updateDischargePowerMax(self):
        self.discharge_.power_max = self.ess_system._installed_capacity_kwh
        self.discharge_.powerMaxChanged.emit()