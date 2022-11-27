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
        actual_ess_lifecycle: float = 2_203,
        ess_capex_per_kwh: float = 2_306,
        charger_lifecycle_capacity: float = 2_365_200,
        charger_capex_per_kw: float = 1_914,
        charger_depreciation: float = 0.15
    ):
        super().__init__()
        self.actual_ess_lifecycle = actual_ess_lifecycle
        self.ess_capex_per_kwh = ess_capex_per_kwh
        self.charger_lifecycle_capacity = charger_lifecycle_capacity
        self.charger_capex_per_kw = charger_capex_per_kw
        self.charger_depreciation = charger_depreciation

        self.ess_depreciation = round(self.ess_capex_per_kwh/self.actual_ess_lifecycle, 2)

    @Property(str, notify=actualEssLifecycleChanged) #getter
    def actualEssLifecycle(self) -> str:
        return str(self.actual_ess_lifecycle)

    @actualEssLifecycle.setter
    def actualEssLifecycle(self, actual_ess_lifecycle:str) -> None:
        self.actual_ess_lifecycle = float(actual_ess_lifecycle)
        self.actualEssLifecycleChanged.emit()

    @Property(str, notify=essCapexPerKwhChanged) #getter
    def essCapexPerKwh(self) -> str:
        return str(self.ess_capex_per_kwh)

    @essCapexPerKwh.setter
    def essCapexPerKwh(self, ess_capex_per_kwh:str) -> None:
        self.ess_capex_per_kwh = float(ess_capex_per_kwh)
        self.essCapexPerKwhChanged.emit()
        
    @Property(str, notify=essDepreciationChanged) #getter
    def essDepreciation(self) -> str:
        return str(self.ess_depreciation)

    @essDepreciation.setter
    def essDepreciation(self, ess_depreciation:str) -> None:
        self.ess_depreciation = float(ess_depreciation)
        self.essDepreciationChanged.emit()

    @Property(str, notify=chargerLifecycleCapacityChanged) #getter
    def chargerLifecycleCapacity(self) -> str:
        return str(self.charger_lifecycle_capacity)

    @chargerLifecycleCapacity.setter
    def chargerLifecycleCapacity(self, charger_lifecycle_capacity:str) -> None:
        self.charger_lifecycle_capacity = float(charger_lifecycle_capacity)
        self.chargerLifecycleCapacityChanged.emit()

    @Property(str, notify=chargerCapexPerKwChanged) #getter
    def chargerCapexPerKw(self) -> str:
        return str(self.charger_capex_per_kw)

    @chargerCapexPerKw.setter
    def chargerCapexPerKw(self, charger_capex_per_kw:str) -> None:
        self.charger_capex_per_kw = float(charger_capex_per_kw)
        self.chargerCapexPerKwChanged.emit()

    @Property(str, notify=chargerDepreciationChanged) #getter
    def chargerDepreciation(self) -> str:
        return str(self.charger_depreciation)

    @chargerDepreciation.setter
    def chargerDepreciation(self, charger_depreciation:str) -> None:
        self.charger_depreciation = float(charger_depreciation)
        self.chargerDepreciationChanged.emit()

    @Slot()
    def updateEssDepreciation(self):
        self.ess_depreciation = round(self.ess_capex_per_kwh/self.actual_ess_lifecycle, 2)
        self.essDepreciationChanged.emit()
