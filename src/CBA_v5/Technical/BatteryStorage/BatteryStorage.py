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
        self._ess_system = EssSystem()
        self._discharge = Discharge()
        self._grid_charging = GridCharging()

        self._ess_system.installedCapacityChanged.connect(self.updateDischargePowerMax)

    def emitUpdateSignals(self):
        self._ess_system.emitUpdateSignals()
        self._discharge.emitUpdateSignals()
        self._grid_charging.emitUpdateSignals()


    @Property(EssSystem, notify=essSystemChanged) #getter
    def essSystem(self) -> EssSystem:
        return self._ess_system

    @Property(Discharge, notify=dischargeChanged) #getter
    def discharge(self) -> Discharge:
        return self._discharge

    @Property(GridCharging, notify=gridChargingChanged) #getter
    def gridCharging(self) -> GridCharging:
        return self._grid_charging

    @Slot()
    def updateDischargePowerMax(self):
        self._discharge._power_max = self._ess_system._installed_capacity_kwh
        self._discharge.powerMaxChanged.emit()