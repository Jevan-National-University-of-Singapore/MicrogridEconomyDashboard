from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class ExchangeRate(QObject):
    rmPerUsdChanged = Signal()

    def __init__(self,
        rm_per_usd: float = 0
    ):
        super().__init__()
        self._rm_per_usd = rm_per_usd

    @Property(str, notify=rmPerUsdChanged) #getter
    def rmPerUsd(self) -> str:
        return str(self._rm_per_usd)

    @rmPerUsd.setter
    def rmPerUsd(self, value:str) -> None:
        self._rm_per_usd = float(value)