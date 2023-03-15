from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class EvCharacteristics(QObject):
    evBatteryVoltageChanged = Signal()
    capacityChanged = Signal()
    maxPowerRatingChanged = Signal()
    ampereHourRatingChanged = Signal()

    def __init__(self,
        ev_battery_voltage:float = 800,
        capacity:float = 54,
        max_power_rating:float = 270
    ):
        super().__init__()
        self.ev_battery_voltage:float = ev_battery_voltage
        self.capacity_:float = capacity
        self.max_power_rating:float = max_power_rating
        self.ampere_hour_rating:float = 0

        '''****************************************
                    CONNECTIONS
        ****************************************'''  
        self.capacityChanged.connect(self.updateAmpereHourRating)
        self.evBatteryVoltageChanged.connect(self.updateAmpereHourRating)

    def emitUpdateSignals(self):
        self.evBatteryVoltageChanged.emit()
        self.capacityChanged.emit()
        self.maxPowerRatingChanged.emit()
        self.ampereHourRatingChanged.emit()

    @Property(float, notify=evBatteryVoltageChanged) #getter
    def evBatteryVoltage(self) -> float:
        return self.ev_battery_voltage

    @evBatteryVoltage.setter
    def evBatteryVoltage(self, ev_battery_voltage:float):
        if self.ev_battery_voltage != ev_battery_voltage:
            self.ev_battery_voltage = ev_battery_voltage
            self.evBatteryVoltageChanged.emit()

    @Property(float, notify=capacityChanged) #getter
    def capacity(self) -> float:
        return self.capacity_

    @capacity.setter
    def capacity(self, capacity:float):
        self.capacity_ = capacity
        self.capacityChanged.emit()

    @Property(float, notify=maxPowerRatingChanged) #getter
    def maxPowerRating(self) -> float:
        return self.max_power_rating

    @maxPowerRating.setter
    def maxPowerRating(self, max_power_rating:float):
        if self.max_power_rating != max_power_rating:
            self.max_power_rating = max_power_rating
            self.maxPowerRatingChanged.emit()
    
    @Property(float, notify=ampereHourRatingChanged) #getter
    def ampereHourRating(self) -> float:
        return self.ampere_hour_rating

    @ampereHourRating.setter
    def ampereHourRating(self, ampere_hour_rating:float):
        if self.ampere_hour_rating != ampere_hour_rating:
            self.ampere_hour_rating = ampere_hour_rating
            self.ampereHourRatingChanged.emit()

    @Slot()
    def updateAmpereHourRating(self):
        if (
            new_value := (self.capacity_ / self.ev_battery_voltage) * 1000 if self.ev_battery_voltage else 0
        ) != self.ampere_hour_rating:
            self.ampere_hour_rating = new_value
            self.ampereHourRatingChanged.emit()