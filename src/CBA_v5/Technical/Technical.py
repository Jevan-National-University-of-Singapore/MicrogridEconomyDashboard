from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .BatteryStorage.BatteryStorage import BatteryStorage
from .ChargingAndDemand.ChargingAndDemand import ChargingAndDemand

class Technical(QObject):
    
    batteryStorageChanged = Signal()
    chargingAndDemandChanged = Signal()

    def __init__(self, 
        name: str = None,
        battery_storage = BatteryStorage(),
        charging_and_demand = ChargingAndDemand(),
    ):
        super().__init__()
        self._battery_storage:BatteryStorage = battery_storage
        self._charging_and_demand:ChargingAndDemand = charging_and_demand

        self._charging_and_demand._charging_ports.dcCharger2RatingChanged.connect(self.updateBatteryStorageChargeRate)
        self._battery_storage._ess_system.installedCapacityChanged.connect(self.updateBatteryStorageChargeRate)
        
        self._charging_and_demand._charging_ports.dcCharger1RatingChanged.connect(self.updateBatteryStorageMaximumPower)
        self._charging_and_demand._ev_characteristics.maxPowerRatingChanged.connect(self.updateBatteryStorageMaximumPower)
        self._battery_storage._discharge.powerMaxChanged.connect(self.updateBatteryStorageMaximumPower)

    def emitUpdateSignals(self):
        self._battery_storage.emitUpdateSignals()
        self._charging_and_demand.emitUpdateSignals()

    @Property(BatteryStorage, notify=batteryStorageChanged) #getter
    def batteryStorage(self) -> BatteryStorage:
        return self._battery_storage

    @Property(ChargingAndDemand, notify=chargingAndDemandChanged) #getter
    def chargingAndDemand(self) -> ChargingAndDemand:
        return self._charging_and_demand

    @Slot()
    def updateBatteryStorageChargeRate(self):
        self._battery_storage._ess_system._charge_rate_cRate = self._charging_and_demand._charging_ports._dc_charger_1_rating /  self._battery_storage._ess_system._installed_capacity_kwh
        self._battery_storage._ess_system.chargeRateChanged.emit()

    @Slot()
    def updateBatteryStorageMaximumPower(self):
        self._battery_storage._ess_system._maximum_power_kw = min(
                self._charging_and_demand._charging_ports._dc_charger_1_rating,
                self._charging_and_demand._ev_characteristics._max_power_rating,
                self._battery_storage._discharge._power_max
            )
        self._battery_storage._ess_system.maximumPowerChanged.emit()
        