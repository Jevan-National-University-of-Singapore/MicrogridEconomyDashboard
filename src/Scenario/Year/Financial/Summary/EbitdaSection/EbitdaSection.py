from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from typing import Optional

from .Revenue.Revenue import Revenue

class EbitdaSection(QObject):
    revenueChanged = Signal()
    ebitdaChanged = Signal()
    opexChanged = Signal()

    def __init__(self,
        revenue: Optional[Revenue] = None,
        ebitda: float = 299_357,
        opex: float = 116_613
    ):
        super().__init__()
        self.revenue_:Revenue = Revenue() if revenue is None else revenue
        self.ebitda_:float = ebitda
        self.opex_ : float = opex

    def emitUpdateSignals(self):    
        self.revenueChanged.emit()
        self.ebitdaChanged.emit()
        self.opexChanged.emit()

    @Property(Revenue, notify=revenueChanged) #getter
    def revenue(self) -> Revenue:
        return self.revenue_

    @revenue.setter
    def revenue(self, revenue:Revenue) -> None:
        self.revenue_ = revenue
        self.revenueChanged.emit()

    @Property(float, notify=ebitdaChanged) #getter
    def ebitda(self) -> float:
        return self.ebitda_

    @ebitda.setter
    def ebitda(self, ebitda:float) -> None:
        self.ebitda_ = ebitda
        self.ebitdaChanged.emit()

    @Property(float, notify=opexChanged) #getter
    def opex(self) -> float:
        return self.opex_

    @opex.setter
    def opex(self, opex:float) -> None:
        self.opex_ = opex
        self.opexChanged.emit()