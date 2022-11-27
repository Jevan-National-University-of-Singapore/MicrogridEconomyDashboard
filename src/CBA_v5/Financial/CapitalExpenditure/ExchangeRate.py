from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class ExchangeRate(QObject):
    rmPerUsdChanged = Signal()

    def __init__(self,
        rm_per_usd: float = 4.18
    ):
        super().__init__()
        self.rm_per_usd = rm_per_usd

    @Property(str, notify=rmPerUsdChanged) #getter
    def rmPerUsd(self) -> str:
        return str(self.rm_per_usd)

    @rmPerUsd.setter
    def rmPerUsd(self, rm_per_usd:str) -> None:
        self.rm_per_usd = float(rm_per_usd)
        self.rmPerUsdChanged.emit()