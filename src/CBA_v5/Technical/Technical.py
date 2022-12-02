from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .SolarPowerGeneration.SolarPowerGeneration import SolarPowerGeneration
from .BatteryStorage.BatteryStorage import BatteryStorage
from .ChargingAndDemand.ChargingAndDemand import ChargingAndDemand

class Technical(QObject):
    
    batteryStorageChanged = Signal()
    chargingAndDemandChanged = Signal()
    solarPowerGenerationChanged = Signal()

    def __init__(self, 
        name: str = None,
        battery_storage = BatteryStorage(),
        solar_power_generation = SolarPowerGeneration(),
        charging_and_demand = ChargingAndDemand()
    ):
        super().__init__()
        self.battery_storage:BatteryStorage = battery_storage
        self.charging_and_demand:ChargingAndDemand = charging_and_demand
        self.solar_power_generation: SolarPowerGeneration = solar_power_generation

        self.battery_storage.ess_system.charge_rate_cRate = round(self.charging_and_demand.charging_ports.dc_charger_1_rating /  self.battery_storage.ess_system.installed_capacity_kwh, 2)
        self.battery_storage.ess_system.maximum_power_kw = min(
                self.charging_and_demand.charging_ports.dc_charger_1_rating,
                self.charging_and_demand.ev_characteristics.max_power_rating,
                self.battery_storage.discharge_.power_max
            )

        self.charging_and_demand.charging_ports.dcCharger2RatingChanged.connect(self.updateBatteryStorageChargeRate)
        self.battery_storage.ess_system.installedCapacityChanged.connect(self.updateBatteryStorageChargeRate)
        
        self.charging_and_demand.charging_ports.dcCharger1RatingChanged.connect(self.updateBatteryStorageMaximumPower)
        self.charging_and_demand.ev_characteristics.maxPowerRatingChanged.connect(self.updateBatteryStorageMaximumPower)
        self.battery_storage.discharge_.powerMaxChanged.connect(self.updateBatteryStorageMaximumPower)

    def emitUpdateSignals(self):
        self.battery_storage.emitUpdateSignals()
        self.charging_and_demand.emitUpdateSignals()
        self.solar_power_generation.emitUpdateSignals()

    @Property(SolarPowerGeneration, notify=solarPowerGenerationChanged) #getter
    def solarPowerGeneration(self) -> SolarPowerGeneration:
        return self.solar_power_generation

    @Property(BatteryStorage, notify=batteryStorageChanged) #getter
    def batteryStorage(self) -> BatteryStorage:
        return self.battery_storage

    @Property(ChargingAndDemand, notify=chargingAndDemandChanged) #getter
    def chargingAndDemand(self) -> ChargingAndDemand:
        return self.charging_and_demand

    @Slot()
    def updateBatteryStorageChargeRate(self):
        self.battery_storage.ess_system.charge_rate_cRate = round(self.charging_and_demand.charging_ports.dc_charger_1_rating /  self.battery_storage.ess_system.installed_capacity_kwh, 2)
        self.battery_storage.ess_system.chargeRateChanged.emit()

    @Slot()
    def updateBatteryStorageMaximumPower(self):
        self.battery_storage.ess_system.maximum_power_kw = min(
                self.charging_and_demand.charging_ports.dc_charger_1_rating,
                self.charging_and_demand.ev_characteristics.max_power_rating,
                self.battery_storage.discharge_.power_max
            )
        self.battery_storage.ess_system.maximumPowerChanged.emit()
        