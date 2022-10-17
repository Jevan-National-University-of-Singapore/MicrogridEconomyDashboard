from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from EssSystem import EssSystem
from Discharge import Discharge
from GridCharging import GridCharging

class BatteryStorage(QObject):
    
    essSystemChanged = Signal()
    dischargeChanged = Signal()
    gridChargingChanged = Signal()

    def __init__(self, 
        ess_system: EssSystem = None,
        discharge: Discharge = None,
        grid_charging: GridCharging = None

    ):
        super().__init__()
        self._ess_system = EssSystem() if ess_system is None else ess_system
        self._discharge = Discharge() if discharge is None else discharge
        self._grid_charging = GridCharging() if grid_charging is None else grid_charging

        self._ess_system.installedCapacityChanged.connect(self.updateDischargePowerMax)

        if self._discharge.power_max is None:
            self._discharge.powerMax = self._ess_system.installed_capacity

    @Property(EssSystem, notify=essSystemChanged) #getter
    def essSystem(self) -> EssSystem:
        return self._ess_system

    @Property(Discharge, notify=dischargeChanged) #getter
    def discharge(self) -> Discharge:
        return self._discharge

    @Property(GridCharging, notify=gridChargingChanged) #getter
    def gridCharging(self) -> GridCharging:
        return self._grid_charging

    @Slot
    def updateDischargePowerMax(self):
        self._discharge.powerMax = self._ess_system.installed_capacity