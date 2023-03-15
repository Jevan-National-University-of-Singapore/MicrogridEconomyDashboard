from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from typing import Optional

from .Revenue.Revenue import Revenue

class EbitdaSection(QObject):
    revenueChanged = Signal()
    ebitdaChanged = Signal()
    opexChanged = Signal()

    def __init__(self, revenue: Optional[Revenue] = None):
        super().__init__()
        self.revenue_:Revenue = Revenue() if revenue is None else revenue
        self.opex_ :float = 0
        self.ebitda_:float = self.revenue_.total_ - self.opex_

        self.revenue_.totalChanged.connect(self.update_ebitda)
        self.opexChanged.connect(self.update_ebitda)

    def emitUpdateSignals(self):    
        self.ebitdaChanged.emit()
        self.revenue_.emitUpdateSignals()
        self.opexChanged.emit()

        self.revenueChanged.emit()


    @Property(Revenue, notify=revenueChanged) #getter
    def revenue(self) -> Revenue:
        return self.revenue_

    @revenue.setter
    def revenue(self, revenue:Revenue) -> None:
        if self.revenue_ != revenue:
            self.revenue_ = revenue
            self.revenueChanged.emit()

    @Property(float, notify=ebitdaChanged) #getter
    def ebitda(self) -> float:
        return self.ebitda_

    @ebitda.setter
    def ebitda(self, ebitda:float) -> None:
        if self.ebitda_ != ebitda:
            self.ebitda_ = ebitda
            self.ebitdaChanged.emit()

    @Property(float, notify=opexChanged) #getter
    def opex(self) -> float:
        return self.opex_

    @opex.setter
    def opex(self, opex:float) -> None:
        if self.opex_ != opex:
            self.opex_ = opex
            self.opexChanged.emit()

    @Slot()
    def update_ebitda(self):
        if (new_value := self.revenue_.total_ - self.opex_) != self.ebitda_:
            self.ebitda_ = new_value
            self.ebitdaChanged.emit()