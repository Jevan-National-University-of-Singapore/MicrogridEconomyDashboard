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
        dc_1_charging_time_per_user:float,
        dc_2_charging_time_per_user:float,

        # optional
        dc_charger_1_rating:float=0,
        num_of_dc_charger1:int=0,

        dc_charger_2_rating:float=0, 
        num_of_dc_charger2:int=0
    ):
        super().__init__()
        self._dc_charger_1_rating = dc_charger_1_rating
        self._num_of_dc_charger1 = num_of_dc_charger1
        self._dc_1_charging_time_per_user = dc_1_charging_time_per_user

        self._dc_charger_2_rating = dc_charger_2_rating
        self._num_of_dc_charger2 = num_of_dc_charger2
        self._dc_2_charging_time_per_user = dc_2_charging_time_per_user

    @Property(str, notify=dcCharger1RatingChanged) #getter
    def dcCharger1Rating(self) -> str:
        return str(self._dc_charger_1_rating)

    @dcCharger1Rating.setter #setter
    def dcCharger1Rating(self, value:str) -> None:
        self._dc_charger_1_rating = float(value)

    @Property(str, notify=numOfDcCharger1Changed) #getter
    def numOfDcCharger1(self) -> str:
        return str(self._num_of_dc_charger1)

    @numOfDcCharger1.setter #setter
    def numOfDcCharger1(self, value:str) -> None:
        self._num_of_dc_charger1 = int(value)
    
    @Property(str, notify=dc1ChargingTimePerUserChanged) #getter
    def dc1ChargingTimePerUser(self) -> str:
        return str(self._dc_1_charging_time_per_user)

    @dc1ChargingTimePerUser.setter #setter
    def dc1ChargingTimePerUser(self, value:str) -> None:
        self._dc_1_charging_time_per_user = float(value)

    @Property(str, notify=dcCharger2RatingChanged) #getter
    def dcCharger2Rating(self) -> str:
        return str(self._dc_charger_2_rating)

    @dcCharger2Rating.setter #setter
    def dcCharger2Rating(self, value:str) -> None:
        self._dc_charger_2_rating = float(value)

    @Property(str, notify=numOfDcCharger2Changed) #getter
    def numOfDcCharger2(self) -> str:
        return str(self._num_of_dc_charger2)

    @numOfDcCharger2.setter #setter
    def numOfDcCharger2(self, value:str) -> None:
        self._num_of_dc_charger2 = int(value)
    
    @Property(str, notify=dc2ChargingTimePerUserChanged) #getter
