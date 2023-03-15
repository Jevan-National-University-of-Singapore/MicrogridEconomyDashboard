from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class CapitalExpenditureItems(QObject):
    solarPvRectificationChanged = Signal()
    dcChargersChanged = Signal()
    ess301Changed = Signal()
    pcs200Changed = Signal()
    totalCapexChanged = Signal()

    def __init__(self,
        solar_pv_rectification:float = 89_460,
        dc_chargers: float = 344_443,
        pcs_200kw: float = 30_000,
        ess_301kwh: float = 816_235
    ):
        super().__init__()
        self.solar_pv_rectification:float = solar_pv_rectification
        self.dc_chargers:float = dc_chargers
        self.pcs_200kw:float = pcs_200kw
        self.ess_301kwh:float = ess_301kwh

        self.total_capex:float = solar_pv_rectification \
                                + dc_chargers \
                                + pcs_200kw \
                                + ess_301kwh
        
        self.solarPvRectificationChanged.connect(self.updateTotalCapex)
        self.dcChargersChanged.connect(self.updateTotalCapex)
        self.ess301Changed.connect(self.updateTotalCapex)
        self.pcs200Changed.connect(self.updateTotalCapex)



    def emitUpdateSignals(self):
        self.solarPvRectificationChanged.emit()
        self.dcChargersChanged.emit()
        self.ess301Changed.emit()
        self.pcs200Changed.emit()
        self.totalCapexChanged.emit()

    @Property(float, notify=solarPvRectificationChanged) #getter
    def solarPvRectification(self) -> float:
        return self.solar_pv_rectification
 
    @solarPvRectification.setter #setter
    def solarPvRectification(self, solar_pv_rectification:float) -> None:
        if self.solar_pv_rectification != solar_pv_rectification:
            self.solar_pv_rectification = solar_pv_rectification
            self.solarPvRectificationChanged.emit()

    @Property(float, notify=dcChargersChanged) #getter
    def dcChargers(self) -> float:
        return self.dc_chargers

    @dcChargers.setter #setter
    def dcChargers(self, dc_chargers:float) -> None:
        if self.dc_chargers != dc_chargers:
            self.dc_chargers = dc_chargers
            self.dcChargersChanged.emit()

    @Property(float, notify=pcs200Changed) #getter
    def pcs200kW(self) -> float:
        return self.pcs_200kw

    @pcs200kW.setter #setter
    def pcs200kW(self, pcs200_:float) -> None:
        if self.pcs_200kw != pcs200_:
            self.pcs_200kw = pcs200_
            self.pcs200Changed.emit()

    @Property(float, notify=totalCapexChanged) #getter
    def totalCapex(self) -> float:
        return self.total_capex

    @totalCapex.setter #setter
    def totalCapex(self, total_capex:float) -> None:
        if self.total_capex != total_capex:
            self.total_capex = total_capex
            self.totalCapexChanged.emit()
 
    @Property(float, notify=ess301Changed) #getter
    def ess301kWh(self) -> float:
        return self.ess_301kwh

    @ess301kWh.setter #setter
    def ess301kWh(self, ess301_:float) -> None:
        if self.ess_301kwh != ess301_:
            self.ess_301kwh = ess301_
            self.ess301Changed.emit()

    @Slot()
    def updateTotalCapex(self):
        if (
            new_value := self.solar_pv_rectification \
                            + self.dc_chargers \
                            + self.pcs_200kw \
                            + self.ess_301kwh
        ) != self.total_capex:
            self.total_capex = new_value
            self.totalCapexChanged.emit()

