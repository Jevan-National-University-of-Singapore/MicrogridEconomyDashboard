from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Depreciation(QObject):
    actualEssLifecycleChanged = Signal()
    essCapexPerKwhChanged =Signal()
    essDepreciationChanged = Signal()
    chargerLifecycleCapacityChanged = Signal()
    chargerCapexPerKwChanged = Signal()
    chargerDepreciationChanged = Signal()

    def __init__(self,
        actual_ess_lifecycle: float,
        ess_capex_per_kwh: float,
        ess_depreciation: float,
        charger_lifecycle_capacity: float,
        charger_capex_per_kw: float,
        charger_depreciation: float
    ):
        super().__init__()
        self._actual_ess_lifecycle = actual_ess_lifecycle
        self._ess_capex_per_kwh = ess_capex_per_kwh
        self._ess_depreciation = ess_depreciation
        self._charger_lifecycle_capacity = charger_lifecycle_capacity
        self._charger_capex_per_kw = charger_capex_per_kw
        self._charger_depreciation = charger_depreciation

    @Property(str, notify=actualEssLifecycleChanged) #getter
    def actualEssLifecycle(self) -> str:
        return str(self._actual_ess_lifecycle)

    @actualEssLifecycle.setter
    def actualEssLifecycle(self, value:str) -> None:
        self._actual_ess_lifecycle = float(value)

    @Property(str, notify=essCapexPerKwhChanged) #getter
    def essCapexPerKwh(self) -> str:
        return str(self._ess_capex_per_kwh)

    @essCapexPerKwh.setter
    def essCapexPerKwh(self, value:str) -> None:
        self._ess_capex_per_kwh = float(value)
        
    @Property(str, notify=essDepreciationChanged) #getter
    def essDepreciation(self) -> str:
        return str(self._ess_depreciation)

    @essDepreciation.setter
    def essDepreciation(self, value:str) -> None:
        self._ess_depreciation = float(value)

    @Property(str, notify=chargerLifecycleCapacityChanged) #getter
    def chargerLifecycleCapacity(self) -> str:
        return str(self._charger_lifecycle_capacity)

    @chargerLifecycleCapacity.setter
    def chargerLifecycleCapacity(self, value:str) -> None:
        self._charger_lifecycle_capacity = float(value)

    @Property(str, notify=chargerCapexPerKwChanged) #getter
    def chargerCapexPerKw(self) -> str:
        return str(self._charger_capex_per_kw)

    @chargerCapexPerKw.setter
    def chargerCapexPerKw(self, value:str) -> None:
        self._charger_capex_per_kw = float(value)

    @Property(str, notify=chargerDepreciationChanged) #getter
    def chargerDepreciation(self) -> str:
        return str(self._charger_depreciation)

    @chargerDepreciation.setter
    def chargerDepreciation(self, value:str) -> None:
        self._charger_depreciation = float(value)
