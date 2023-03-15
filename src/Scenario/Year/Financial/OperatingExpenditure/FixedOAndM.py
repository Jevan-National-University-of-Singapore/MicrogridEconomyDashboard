from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class FixedOAndM(QObject):
    solarPvOAndMChanged = Signal()
    evChargerOAndMChanged = Signal()
    lfpAndMChanged = Signal()

    def __init__(self,
        solar_pv_o_and_m: float = 25,
        ev_charger_o_and_m: float = 400,
        lfp_o_and_m: float = 4.4
    ):
        super().__init__()
        self.solar_pv_o_and_m:float = solar_pv_o_and_m
        self.ev_charger_o_and_m:float = ev_charger_o_and_m
        self.lfp_o_and_m:float = lfp_o_and_m

    def emitUpdateSignals(self):
        self.solarPvOAndMChanged.emit()
        self.evChargerOAndMChanged.emit()
        self.lfpAndMChanged.emit()

    @Property(float, notify=solarPvOAndMChanged) #getter
    def solarPvOAndM(self) -> float:
        return self.solar_pv_o_and_m

    @solarPvOAndM.setter
    def solarPvOAndM(self, solar_pv_o_and_m:float) -> None:
        if self.solar_pv_o_and_m != solar_pv_o_and_m:
            self.solar_pv_o_and_m = solar_pv_o_and_m
            self.solarPvOAndMChanged.emit()

    @Property(float, notify=evChargerOAndMChanged) #getter
    def evChargerOAndM(self) -> float:
        return self.ev_charger_o_and_m

    @evChargerOAndM.setter
    def evChargerOAndM(self, ev_charger_o_and_m:float) -> None:
        if self.ev_charger_o_and_m != ev_charger_o_and_m:
            self.ev_charger_o_and_m = ev_charger_o_and_m
            self.evChargerOAndMChanged.emit()

    @Property(float, notify=lfpAndMChanged) #getter
    def lfpAndM(self) -> float:
        return self.lfp_o_and_m

    @lfpAndM.setter
    def lfpAndM(self, lfp_o_and_m:float) -> None:
        if self.lfp_o_and_m != lfp_o_and_m:
            self.lfp_o_and_m = lfp_o_and_m
            self.lfpAndMChanged.emit()

    
