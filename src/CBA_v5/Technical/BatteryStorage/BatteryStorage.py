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
        ess_system_charge_rate: float,
        ess_system_maximum_power: float,

        discharge_power_continuous: float,
        discharge_power_max: float,

        grid_charging_off_peak_electricity_required: float,
        grid_charging_peak_electricity_charged_from_grid: float,
        grid_charging_grid_electricity_required: float
    ):
        super().__init__()

        self._ess_system = EssSystem (
                                charge_rate_cRate=ess_system_charge_rate,
                                maximum_power_kw=ess_system_maximum_power
                            )

        self._discharge = Discharge (
                                power_continuous=discharge_power_continuous,
                                power_max=discharge_power_max
                            )

        self._grid_charging = GridCharging (
                                off_peak_electricity_required=grid_charging_off_peak_electricity_required,
                                peak_electricity_charged_from_grid=grid_charging_peak_electricity_charged_from_grid,
                                grid_electricity_required=grid_charging_grid_electricity_required
                            )
       
    @Property(EssSystem, notify=essSystemChanged) #getter
    def essSystem(self) -> EssSystem:
        return self._ess_system

    @Property(Discharge, notify=dischargeChanged) #getter
    def discharge(self) -> Discharge:
        return self._discharge

    @Property(GridCharging, notify=gridChargingChanged) #getter
    def gridCharging(self) -> GridCharging:
        return self._grid_charging