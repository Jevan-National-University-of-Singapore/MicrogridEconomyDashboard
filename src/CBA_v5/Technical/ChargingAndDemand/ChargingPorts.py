from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class ChargingPorts(QObject):
    dcCharger1RatingChanged = Signal()
    numOfDcCharger1Changed = Signal()
    dc1ChargingTimePerUserChanged = Signal()

    dcCharger2RatingChanged = Signal()
    numOfDcCharger2Changed = Signal()
    dc2ChargingTimePerUserChanged = Signal()

    def __init__(self,
        # required
        dc_1_charging_time_per_user:float = 0.18,
        dc_2_charging_time_per_user:float = 0.65,

        # optional
        dc_charger_1_rating:float=180,
        num_of_dc_charger1:int=1,

        dc_charger_2_rating:float=50, 
        num_of_dc_charger2:int=1
    ):
        super().__init__()
        self.dc_charger_1_rating = dc_charger_1_rating
        self.num_of_dc_charger1 = num_of_dc_charger1
        self.dc_1_charging_time_per_user = dc_1_charging_time_per_user

        self.dc_charger_2_rating = dc_charger_2_rating
        self.num_of_dc_charger2 = num_of_dc_charger2
        self.dc_2_charging_time_per_user = dc_2_charging_time_per_user

    def emitUpdateSignals(self):
        self.dcCharger1RatingChanged.emit()
        self.numOfDcCharger1Changed.emit()
        self.dc1ChargingTimePerUserChanged.emit()

        self.dcCharger2RatingChanged.emit()
        self.numOfDcCharger2Changed.emit()
        self.dc2ChargingTimePerUserChanged.emit()

    @Property(str, notify=dcCharger1RatingChanged) #getter
    def dcCharger1Rating(self) -> str:
        return str(self.dc_charger_1_rating)

    @dcCharger1Rating.setter #setter
    def dcCharger1Rating(self, value:str) -> None:
        self.dc_charger_1_rating = float(value)
        self.dcCharger1RatingChanged.emit()

    @Property(str, notify=numOfDcCharger1Changed) #getter
    def numOfDcCharger1(self) -> str:
        return str(self.num_of_dc_charger1)

    @numOfDcCharger1.setter #setter
    def numOfDcCharger1(self, value:str) -> None:
        self.num_of_dc_charger1 = int(value)
        self.numOfDcCharger1Changed.emit()

    @Property(str, notify=dc1ChargingTimePerUserChanged) #getter
    def dc1ChargingTimePerUser(self) -> str:
        return str(self.dc_1_charging_time_per_user)

    @dc1ChargingTimePerUser.setter #setter
    def dc1ChargingTimePerUser(self, value:str) -> None:
        self.dc_1_charging_time_per_user = float(value)
        self.dc1ChargingTimePerUserChanged.emit()

    @Property(str, notify=dcCharger2RatingChanged) #getter
    def dcCharger2Rating(self) -> str:
        return str(self.dc_charger_2_rating)

    @dcCharger2Rating.setter #setter
    def dcCharger2Rating(self, value:str) -> None:
        self.dc_charger_2_rating = float(value)
        self.dcCharger1RatingChanged.emit()

    @Property(str, notify=numOfDcCharger2Changed) #getter
    def numOfDcCharger2(self) -> str:
        return str(self.num_of_dc_charger2)

    @numOfDcCharger2.setter #setter
    def numOfDcCharger2(self, value:str) -> None:
        self.num_of_dc_charger2 = int(value)
        self.numOfDcCharger2Changed.emit()
    
    @Property(str, notify=dc2ChargingTimePerUserChanged) #getter
    def dc2ChargingTimePerUser(self) -> str:
        return str(self.dc_2_charging_time_per_user)

    @dc2ChargingTimePerUser.setter #setter
    def dc2ChargingTimePerUser(self, value:str) -> None:
        self.dc_2_charging_time_per_user = float(value)
        self.dc2ChargingTimePerUserChanged.emit()