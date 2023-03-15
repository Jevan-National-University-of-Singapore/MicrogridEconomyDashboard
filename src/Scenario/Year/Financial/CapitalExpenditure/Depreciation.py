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
        self.actual_ess_lifecycle:float = actual_ess_lifecycle
        self.ess_capex_per_kwh:float = ess_capex_per_kwh
        self.charger_lifecycle_capacity:float = charger_lifecycle_capacity
        self.charger_capex_per_kw:float = charger_capex_per_kw
        self.charger_depreciation:float = charger_depreciation

        self.ess_depreciation:float = self.ess_capex_per_kwh/self.actual_ess_lifecycle if self.actual_ess_lifecycle else 0

        self.essCapexPerKwhChanged.connect(self.updateEssDepreciation)
        self.actualEssLifecycleChanged.connect(self.updateEssDepreciation)

    def emitUpdateSignals(self):
        self.actualEssLifecycleChanged.emit()
        self.essCapexPerKwhChanged.emit()
        self.essDepreciationChanged.emit()
        self.chargerLifecycleCapacityChanged.emit()
        self.chargerCapexPerKwChanged.emit()
        self.chargerDepreciationChanged.emit()

    @Property(float, notify=actualEssLifecycleChanged) #getter
    def actualEssLifecycle(self) -> float:
        return self.actual_ess_lifecycle

    @actualEssLifecycle.setter
    def actualEssLifecycle(self, actual_ess_lifecycle:float) -> None:
        self.actual_ess_lifecycle = actual_ess_lifecycle
        self.actualEssLifecycleChanged.emit()

    @Property(float, notify=essCapexPerKwhChanged) #getter
    def essCapexPerKwh(self) -> float:
        return self.ess_capex_per_kwh

    @essCapexPerKwh.setter
    def essCapexPerKwh(self, ess_capex_per_kwh:float) -> None:
        self.ess_capex_per_kwh = ess_capex_per_kwh
        self.essCapexPerKwhChanged.emit()
        
    @Property(float, notify=essDepreciationChanged) #getter
    def essDepreciation(self) -> float:
        return self.ess_depreciation

    @essDepreciation.setter
    def essDepreciation(self, ess_depreciation:float) -> None:
        self.ess_depreciation = ess_depreciation
        self.essDepreciationChanged.emit()

    @Property(float, notify=chargerLifecycleCapacityChanged) #getter
    def chargerLifecycleCapacity(self) -> float:
        return self.charger_lifecycle_capacity

    @chargerLifecycleCapacity.setter
    def chargerLifecycleCapacity(self, charger_lifecycle_capacity:float) -> None:
        self.charger_lifecycle_capacity = charger_lifecycle_capacity
        self.chargerLifecycleCapacityChanged.emit()

    @Property(float, notify=chargerCapexPerKwChanged) #getter
    def chargerCapexPerKw(self) -> float:
        return self.charger_capex_per_kw

    @chargerCapexPerKw.setter
    def chargerCapexPerKw(self, charger_capex_per_kw:float) -> None:
        self.charger_capex_per_kw = charger_capex_per_kw
        self.chargerCapexPerKwChanged.emit()

    @Property(float, notify=chargerDepreciationChanged) #getter
    def chargerDepreciation(self) -> float:
        return self.charger_depreciation

    @chargerDepreciation.setter
    def chargerDepreciation(self, charger_depreciation:float) -> None:
        self.charger_depreciation = charger_depreciation
        self.chargerDepreciationChanged.emit()

    @Slot()
    def updateEssDepreciation(self):
        if (new_value := self.ess_capex_per_kwh/self.actual_ess_lifecycle if self.actual_ess_lifecycle else 0):
            self.ess_depreciation = new_value
            self.essDepreciationChanged.emit()
