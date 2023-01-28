from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class FixedOAndM(QObject):
    solarPvOAndMChanged = Signal()
    evChargerOAndMChanged = Signal()
    lfpAndMChanged = Signal()

    def __init__(self,
        # all optional
        solar_pv_o_and_m: float = 25,
        ev_charger_o_and_m: float = 400,
        lfp_o_and_m: float = 4.4
    ):
        super().__init__()
        self.solar_pv_o_and_m = solar_pv_o_and_m
        self.ev_charger_o_and_m = ev_charger_o_and_m
        self.lfp_o_and_m = lfp_o_and_m

    def emitUpdateSignals(self):
        self.solarPvOAndMChanged.emit()
        self.evChargerOAndMChanged.emit()
        self.lfpAndMChanged.emit()

    @Property(str, notify=solarPvOAndMChanged) #getter
    def solarPvOAndM(self) -> str:
        return str(self.solar_pv_o_and_m)

    @solarPvOAndM.setter
    def solarPvOAndM(self, solar_pv_o_and_m:str) -> None:
        self.solar_pv_o_and_m = round(float(solar_pv_o_and_m), 2)
        self.solarPvOAndMChanged.emit()

    @Property(str, notify=evChargerOAndMChanged) #getter
    def evChargerOAndM(self) -> str:
        return str(self.ev_charger_o_and_m)

    @evChargerOAndM.setter
    def evChargerOAndM(self, ev_charger_o_and_m:str) -> None:
        self.ev_charger_o_and_m = round(float(ev_charger_o_and_m), 2)
        self.evChargerOAndMChanged.emit()

    @Property(str, notify=lfpAndMChanged) #getter
    def lfpAndM(self) -> str:
        return str(self.lfp_o_and_m)

    @lfpAndM.setter
    def lfpAndM(self, lfp_o_and_m:str) -> None:
        self.lfp_o_and_m = round(float(lfp_o_and_m), 2)
        self.lfpAndMChanged.emit()

    
