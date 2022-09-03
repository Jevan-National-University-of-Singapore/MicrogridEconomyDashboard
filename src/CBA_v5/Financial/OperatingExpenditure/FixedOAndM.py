from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class FixedOAndM(QObject):
    solarPvOAndMChanged = Signal()
    evChargerOAndMChanged = Signal()
    lfpAndMChanged = Signal()

    def __init__(self,
        # all optional
        solar_pv_o_and_m: float = 0,
        ev_charger_o_and_m: float = 0,
        lfp_o_and_m: float = 0
    ):
        super().__init__()
        self._solar_pv_o_and_m = solar_pv_o_and_m
        self._ev_charger_o_and_m = ev_charger_o_and_m
        self._lfp_o_and_m = lfp_o_and_m

    @Property(str, notify=solarPvOAndMChanged) #getter
    def solarPvOAndM(self) -> str:
        return str(self._solar_pv_o_and_m)

    @solarPvOAndM.setter
    def solarPvOAndM(self, value:str) -> None:
        self._solar_pv_o_and_m = float(value)

    @Property(str, notify=evChargerOAndMChanged) #getter
    def evChargerOAndM(self) -> str:
        return str(self._ev_charger_o_and_m)

    @evChargerOAndM.setter
    def evChargerOAndM(self, value:str) -> None:
        self._ev_charger_o_and_m = float(value)

    @Property(str, notify=lfpAndMChanged) #getter
    def lfpAndM(self) -> str:
        return str(self._lfp_o_and_m)

    @lfpAndM.setter
    def lfpAndM(self, value:str) -> None:
        self._lfp_o_and_m = float(value)

    
