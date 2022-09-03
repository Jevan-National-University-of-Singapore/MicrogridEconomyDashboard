from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class OperatingExpenditureItems(QObject):
    solarPvOAndMChanged = Signal()
    dcChargesOAndMChanged = Signal()
    essOAndMChanged = Signal()
    gridElectricityChanged = Signal()
    totalOpexChanged = Signal()

    def __init__(self,
        solar_pv_o_and_m:float = 0,
        dc_chargers_o_and_m:float = 0,
        ess_o_and_m:float = 0,
        grid_electricity:float = 0
    ):
        super().__init__()
        self._solar_pv_o_and_m = solar_pv_o_and_m
        self._dc_chargers_o_and_m = dc_chargers_o_and_m
        self._ess_o_and_m = ess_o_and_m
        self._grid_electricity = grid_electricity
        self._total_opex = solar_pv_o_and_m \
                            + dc_chargers_o_and_m \
                            + ess_o_and_m \
                            + grid_electricity

    @Property(str, notify=solarPvOAndMChanged) #getter
    def solarPvOAndM(self) -> str:
        return str(self._solar_pv_o_and_m)

    @solarPvOAndM.setter
    def solarPvOAndM(self, value:str) -> None:
        self._solar_pv_o_and_m = float(value)

    @Property(str, notify=dcChargesOAndMChanged) #getter
    def dcChargesOAndM(self) -> str:
        return str(self._dc_chargers_o_and_m)

    @dcChargesOAndM.setter
    def dcChargesOAndM(self, value:str) -> None:
        self._dc_chargers_o_and_m = float(value)

    @Property(str, notify=essOAndMChanged) #getter
    def essOAndM(self) -> str:
        return str(self._ess_o_and_m)

    @essOAndM.setter
    def essOAndM(self, value:str) -> None:
        self._ess_o_and_m = float(value)

    @Property(str, notify=gridElectricityChanged) #getter
    def gridElectricity(self) -> str:
        return str(self._grid_electricity)

    @gridElectricity.setter
    def gridElectricity(self, value:str) -> None:
        self._grid_electricity = float(value)

    @Property(str, notify=totalOpexChanged) #getter
    def totalOpex(self) -> str:
        return str(self._total_opex)

    @totalOpex.setter
    def totalOpex(self, value:str) -> None:
        self._total_opex = float(value)