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
        solar_pv_rectification:float,
        dc_chargers: float,
        pcs200: float,

        #optional
        ess301: float = 0,
    ):
        super().__init__()
        self._solar_pv_rectification = solar_pv_rectification
        self._dc_chargers = dc_chargers
        self._pcs200 = pcs200

        self._ess301 = ess301

        self._total_capex = solar_pv_rectification \
                            + dc_chargers \
                            + pcs200 \
                            + ess301

    @Property(str, notify=solarPvRectificationChanged) #getter
    def solarPvRectification(self) -> str:
        return str(self._solar_pv_rectification)
 
    @solarPvRectification.setter #setter
    def solarPvRectification(self, value:str) -> None:
        self._solar_pv_rectification = float(value)

    @Property(str, notify=dcChargersChanged) #getter
    def dcChargers(self) -> str:
        return str(self._dc_chargers)

    @dcChargers.setter #setter
    def dcChargers(self, value:str) -> None:
        self._dc_chargers = float(value)

    @Property(str, notify=pcs200Changed) #getter
    def pcs200(self) -> str:
        return str(self._pcs200)

    @pcs200.setter #setter
    def pcs200(self, value:str) -> None:
        self._pcs200 = float(value)

    @Property(str, notify=totalCapexChanged) #getter
    def totalCapex(self) -> str:
        return str(self._total_capex)

    @totalCapex.setter #setter
    def totalCapex(self, value:str) -> None:
        self._total_capex = float(value)
 
    @Property(str, notify=ess301Changed) #getter
    def ess301(self) -> str:
        return str(self._ess301)

    @ess301.setter #setter
    def ess301(self, value:str) -> None:
        self._ess301 = float(value)

