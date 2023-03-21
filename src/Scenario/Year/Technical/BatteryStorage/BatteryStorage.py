from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from typing import Optional

from .EssSystem import EssSystem
from .Discharge import Discharge
from .GridCharging import GridCharging

class BatteryStorage(QObject):
    
    essSystemChanged = Signal()
    dischargeChanged = Signal()
    gridChargingChanged = Signal()

    chargingStrategyChanged = Signal()

    def __init__(self, 
        ess_system: Optional[EssSystem] = None,
        discharge: Optional[Discharge] = None,
        grid_charging: Optional[GridCharging] = None,

        charging_strategy: Optional[int] = None

    ):
        super().__init__()
        self.ess_system:EssSystem = EssSystem() if ess_system is None else ess_system
        self.discharge_:Discharge = Discharge() if discharge is None else discharge
        self.grid_charging:GridCharging = GridCharging() if grid_charging is None else grid_charging

        self.charging_strategy: int = 1 if charging_strategy is None else charging_strategy
        assert self.charging_strategy in [1,2]
        '''****************************************
                    CONNECTIONS
        ****************************************'''        

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
        if self.discharge_.power_max != self.ess_system.installed_capacity_kwh:
            self.discharge_.power_max = self.ess_system.installed_capacity_kwh
            self.discharge_.powerMaxChanged.emit()