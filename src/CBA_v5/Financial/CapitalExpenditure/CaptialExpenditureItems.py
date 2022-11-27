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

        #optional
        ess_301kwh: float = 816_235,
    ):
        super().__init__()
        self.solar_pv_rectification = solar_pv_rectification
        self.dc_chargers = dc_chargers
        self.pcs_200kw = pcs_200kw

        self.ess_301kwh = ess_301kwh

        self.total_capex = round (
                            solar_pv_rectification \
                                + dc_chargers \
                                + pcs_200kw \
                                + ess_301kwh,
                            2
                        )

    @Property(str, notify=solarPvRectificationChanged) #getter
    def solarPvRectification(self) -> str:
        return str(self.solar_pv_rectification)
 
    @solarPvRectification.setter #setter
    def solarPvRectification(self, solar_pv_rectification:str) -> None:
        self.solar_pv_rectification = float(solar_pv_rectification)
        self.solarPvRectificationChanged.emit()

    @Property(str, notify=dcChargersChanged) #getter
    def dcChargers(self) -> str:
        return str(self.dc_chargers)

    @dcChargers.setter #setter
    def dcChargers(self, dc_chargers:str) -> None:
        self.dc_chargers = float(dc_chargers)
        self.dcChargersChanged.emit()

    @Property(str, notify=pcs200Changed) #getter
    def pcs200kW(self) -> str:
        return str(self.pcs_200kw)

    @pcs200kW.setter #setter
    def pcs200kW(self, pcs200_:str) -> None:
        self.pcs_200kw = float(pcs200_)
        self.pcs200Changed.emit()

    @Property(str, notify=totalCapexChanged) #getter
    def totalCapex(self) -> str:
        return str(self.total_capex)

    @totalCapex.setter #setter
    def totalCapex(self, ess301_:str) -> None:
        self.total_capex = float(ess301_)
        self.totalCapexChanged.emit()
 
    @Property(str, notify=ess301Changed) #getter
    def ess301kWh(self) -> str:
        return str(self.ess_301kwh)

    @ess301kWh.setter #setter
    def ess301kWh(self, ess301_:str) -> None:
        self.ess_301kwh = float(ess301_)
        self.ess301Changed.emit()

    @Slot()
    def updateTotalCapex(self):
        self.total_capex = round (
                    self.solar_pv_rectification \
                        + self.dc_chargers \
                        + self.pcs200kW \
                        + self.ess301kWh,
                    2
                )

        self.totalCapexChanged.emit()

