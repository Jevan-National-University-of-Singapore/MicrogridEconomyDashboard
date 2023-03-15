from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class OperatingExpenditureItems(QObject):
    solarPvOAndMChanged = Signal()
    dcChargesOAndMChanged = Signal()
    essOAndMChanged = Signal()
    gridElectricityChanged = Signal()
    totalOpexChanged = Signal()

    def __init__(self):
        super().__init__()
        self.solar_pv_o_and_m:float = 0
        self.dc_chargers_o_and_m:float = 0
        self.ess_o_and_m:float = 0
        self.grid_electricity:float = 0
        self.total_opex:float = self.solar_pv_o_and_m \
                                + self.dc_chargers_o_and_m \
                                + self.ess_o_and_m \
                                + self.grid_electricity

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

    @Property(float, notify=solarPvOAndMChanged) #getter
    def solarPvOAndM(self) -> float:
        return self.solar_pv_o_and_m

    @solarPvOAndM.setter
    def solarPvOAndM(self, value:float) -> None:
        if self.solar_pv_o_and_m != value:
            self.solar_pv_o_and_m = value
            self.solarPvOAndMChanged.emit()

    @Property(float, notify=dcChargesOAndMChanged) #getter
    def dcChargesOAndM(self) -> float:
        return self.dc_chargers_o_and_m

    @dcChargesOAndM.setter
    def dcChargesOAndM(self, value:float) -> None:
        if self.dc_chargers_o_and_m != value:
            self.dc_chargers_o_and_m = value
            self.dcChargesOAndMChanged.emit()

    @Property(float, notify=essOAndMChanged) #getter
    def essOAndM(self) -> float:
        return self.ess_o_and_m

    @essOAndM.setter
    def essOAndM(self, value:float) -> None:
        if self.ess_o_and_m != value:
            self.ess_o_and_m = value
            self.essOAndMChanged.emit()

    @Property(float, notify=gridElectricityChanged) #getter
    def gridElectricity(self) -> float:
        return self.grid_electricity

    @gridElectricity.setter
    def gridElectricity(self, value:float) -> None:
        if self.grid_electricity != value:
            self.grid_electricity = value
            self.gridElectricityChanged.emit()

    @Property(float, notify=totalOpexChanged) #getter
    def totalOpex(self) -> float:
        return self.total_opex

    @totalOpex.setter
    def totalOpex(self, value:float) -> None:
        if self.total_opex != value:
            self.total_opex = value
            self.totalOpexChanged.emit()

    @Slot()
    def updateTotalOpex(self):
        if (
            new_value := self.solar_pv_o_and_m \
                            + self.dc_chargers_o_and_m \
                            + self.ess_o_and_m \
                            + self.grid_electricity 
        ) != self.total_opex:
            self.total_opex = new_value
            self.totalOpexChanged.emit()