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
        solar_pv_o_and_m:float = 2_822,
        dc_chargers_o_and_m:float = 3_344,
        ess_o_and_m:float = 6_511,
        grid_electricity:float = 103_936
    ):
        super().__init__()
        self.solar_pv_o_and_m = solar_pv_o_and_m
        self.dc_chargers_o_and_m = dc_chargers_o_and_m
        self.ess_o_and_m = ess_o_and_m
        self.grid_electricity = grid_electricity
        self.total_opex = round(
                            solar_pv_o_and_m \
                                + dc_chargers_o_and_m \
                                + ess_o_and_m \
                                + grid_electricity,
                            2
                        )

        self.solarPvOAndMChanged.connect(self.updateTotalOpex)
        self.dcChargesOAndMChanged.connect(self.updateTotalOpex)
        self.essOAndMChanged.connect(self.updateTotalOpex)
        self.gridElectricityChanged.connect(self.updateTotalOpex)

    def emitUpdateSignals(self):
        self.solarPvOAndMChanged.emit()
        self.dcChargesOAndMChanged.emit()
        self.essOAndMChanged.emit()
        self.gridElectricityChanged.emit()
        self.totalOpexChanged.emit()

    @Property(str, notify=solarPvOAndMChanged) #getter
    def solarPvOAndM(self) -> str:
        return str(self.solar_pv_o_and_m)

    @solarPvOAndM.setter
    def solarPvOAndM(self, value:str) -> None:
        self.solar_pv_o_and_m = round(float(value), 2)
        self.solarPvOAndMChanged.emit()

    @Property(str, notify=dcChargesOAndMChanged) #getter
    def dcChargesOAndM(self) -> str:
        return str(self.dc_chargers_o_and_m)

    @dcChargesOAndM.setter
    def dcChargesOAndM(self, value:str) -> None:
        self.dc_chargers_o_and_m = round(float(value), 2)
        self.dcChargesOAndMChanged.emit()

    @Property(str, notify=essOAndMChanged) #getter
    def essOAndM(self) -> str:
        return str(self.ess_o_and_m)

    @essOAndM.setter
    def essOAndM(self, value:str) -> None:
        self.ess_o_and_m = round(float(value), 2)
        self.essOAndMChanged.emit()

    @Property(str, notify=gridElectricityChanged) #getter
    def gridElectricity(self) -> str:
        return str(self.grid_electricity)

    @gridElectricity.setter
    def gridElectricity(self, value:str) -> None:
        self.grid_electricity = round(float(value), 2)
        self.gridElectricityChanged.emit()

    @Property(str, notify=totalOpexChanged) #getter
    def totalOpex(self) -> str:
        return str(self.total_opex)

    @totalOpex.setter
    def totalOpex(self, value:str) -> None:
        self.total_opex = round(float(value), 2)
        self.totalOpexChanged.emit()

    @Slot()
    def updateTotalOpex(self):
        self.total_opex = round (
                            self.solar_pv_o_and_m \
                            + self.dc_chargers_o_and_m \
                            + self.ess_o_and_m \
                            + self.grid_electricity,
                            2
                        )
        self.totalOpexChanged.emit()