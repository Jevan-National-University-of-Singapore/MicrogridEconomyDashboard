from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from typing import Optional

from .Depreciation.Depreciation import Depreciation

class EbitSection(QObject):
    depreciationChanged = Signal()
    ebitChanged = Signal()

    def __init__(self, depreciation: Optional[Depreciation] = None):
        super().__init__()
        self.depreciation_:Depreciation = Depreciation() if depreciation is None else depreciation
        self.ebit_:float = 0

    def emitUpdateSignals(self):    
        self.ebitChanged.emit()
        self.depreciation_.emitUpdateSignals()

        self.depreciationChanged.emit()


    @Property(Depreciation, notify=depreciationChanged) #getter
    def depreciation(self) -> Depreciation:
        return self.depreciation_

    @depreciation.setter
    def depreciation(self, depreciation:Depreciation) -> None:
        self.depreciation_ = depreciation
        self.depreciationChanged.emit()

    @Property(float, notify=ebitChanged) #getter
    def ebit(self) -> float:
        return self.ebit_

    @ebit.setter
    def ebit(self, ebit:float) -> None:
        if self.ebit_ != ebit:
            self.ebit_ = ebit
            self.ebitChanged.emit()

