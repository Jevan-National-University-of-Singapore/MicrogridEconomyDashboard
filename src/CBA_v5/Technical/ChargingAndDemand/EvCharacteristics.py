from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class EvCharacteristics(QObject):
    evBatteryVoltageChanged = Signal()
    capacityChanged = Signal()
    maxPowerRatingChanged = Signal()
    ampereHourRatingChanged = Signal()

    def __init__(self,
        # required
        ampere_hour_rating:float = 67.5,

        ev_battery_voltage:float = 800,
        capacity:float = 54,
        max_power_rating:float = 270
    ):
        super().__init__()
        self.ev_battery_voltage = ev_battery_voltage
        self.capacity_ = capacity
        self.max_power_rating = max_power_rating
        self.ampere_hour_rating = ampere_hour_rating

        self.ampere_hour_rating = round((self.capacity_ / self.ev_battery_voltage) * 1000)

        self.capacityChanged.connect(self.updateAmpereHourRating)
        self.evBatteryVoltageChanged.connect(self.updateAmpereHourRating)

    def emitUpdateSignals(self):
        self.evBatteryVoltageChanged.emit()
        self.capacityChanged.emit()
        self.maxPowerRatingChanged.emit()
        self.ampereHourRatingChanged.emit()

    @Property(str, notify=evBatteryVoltageChanged) #getter
    def evBatteryVoltage(self) -> str:
        return str(self.ev_battery_voltage)

    @evBatteryVoltage.setter
    def evBatteryVoltage(self, ev_battery_voltage:str):
        self.ev_battery_voltage = round(float(ev_battery_voltage))
        self.evBatteryVoltageChanged.emit()

    @Property(str, notify=capacityChanged) #getter
    def capacity(self) -> str:
        return str(self.capacity_)

    @capacity.setter
    def capacity(self, capacity:str):
        self.capacity_ = round(float(capacity))
        self.capacityChanged.emit()

    @Property(str, notify=maxPowerRatingChanged) #getter
    def maxPowerRating(self) -> str:
        return str(self.max_power_rating)

    @maxPowerRating.setter
    def maxPowerRating(self, max_power_rating:str):
        self.max_power_rating = round(float(max_power_rating))
        self.maxPowerRatingChanged.emit()
    
    @Property(str, notify=ampereHourRatingChanged) #getter
    def ampereHourRating(self) -> str:
        return str(self.ampere_hour_rating)

    @ampereHourRating.setter
    def ampereHourRating(self, ampere_hour_rating:str):
        self.ampere_hour_rating = round(float(ampere_hour_rating))
        self.ampereHourRatingChanged.emit()

    @Slot()
    def updateAmpereHourRating(self):
        self.ampere_hour_rating = round((self.capacity_ / self.ev_battery_voltage) * 1000)
        self.ampereHourRatingChanged.emit()