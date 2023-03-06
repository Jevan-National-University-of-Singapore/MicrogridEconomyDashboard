from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from typing import Optional

from .Depreciation.Depreciation import Depreciation

class EbitSection(QObject):
    depreciationChanged = Signal()
    ebitChanged = Signal()

    def __init__(self,
        depreciation: Optional[Depreciation] = None,
        ebitda: float = 299_357
    ):
        super().__init__()
        self.depreciation_:Depreciation = Depreciation() if depreciation is None else depreciation
        self.ebit_:float = ebitda

    def emitUpdateSignals(self):    
        self.depreciationChanged.emit()
        self.ebitChanged.emit()

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
        self.ebit_ = ebit
        self.ebitChanged.emit()