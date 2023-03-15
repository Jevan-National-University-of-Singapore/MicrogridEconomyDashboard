from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class GridCharging(QObject):
    gridDrawLimitChanged = Signal()

    offPeakElectricityRequiredChanged = Signal()
    peakElectricityChargedFromGridChanged = Signal()
    gridElectricityRequiredChanged = Signal()

    def __init__(self, grid_draw_limit_kw: float = 28.8): 
        super().__init__()
        self.grid_draw_limit_kw:float = grid_draw_limit_kw

        self.off_peak_electricity_required_kwh_per_day:float = 0
        self.peak_electricity_charged_from_grid_kwh_per_day:float = 0
        self.grid_electricity_required_kwh_per_day: float = 0

        '''****************************************
                    CONNECTIONS
        ****************************************'''   
        self.offPeakElectricityRequiredChanged.connect(self.updateGridElectricityRequiredPerDay)
        self.peakElectricityChargedFromGridChanged.connect(self.updateGridElectricityRequiredPerDay)

    def emitUpdateSignals(self):
        self.offPeakElectricityRequiredChanged.emit()
        self.peakElectricityChargedFromGridChanged.emit()
        self.gridElectricityRequiredChanged.emit()
        self.gridDrawLimitChanged.emit()

    ### User Assumptions
    # ======== Grid Draw Limit ========
    @Property(float, notify=gridDrawLimitChanged) #getter
    def gridDrawLimit(self) -> float:
        return self.grid_draw_limit_kw

    @gridDrawLimit.setter #setter
    def gridDrawLimit(self, value:float) -> None:
        if self.grid_draw_limit_kw != value:
            self.grid_draw_limit_kw = value
            self.gridDrawLimitChanged.emit()

    ### Read Only Properties
    # ======== Off Peak Electricity Required ========
    @Property(float, notify=offPeakElectricityRequiredChanged) #getter
    def offPeakElectricityRequired(self) -> float:
        return self.off_peak_electricity_required_kwh_per_day

    @offPeakElectricityRequired.setter #setter
    def offPeakElectricityRequired(self, value:float) -> None:
        if self.off_peak_electricity_required_kwh_per_day != value:
            self.off_peak_electricity_required_kwh_per_day = value
            self.offPeakElectricityRequiredChanged.emit()

    # ======== Peak Electricity Charged From Grid ========
    @Property(float, notify=peakElectricityChargedFromGridChanged) #getter
    def peakElectricityChargedFromGrid(self) -> float:
        return self.peak_electricity_charged_from_grid_kwh_per_day

    @peakElectricityChargedFromGrid.setter #setter
    def peakElectricityChargedFromGrid(self, value:float) -> None:
        if self.peak_electricity_charged_from_grid_kwh_per_day != value:
            self.peak_electricity_charged_from_grid_kwh_per_day = value
            self.peakElectricityChargedFromGridChanged.emit()

    # ======== Grid Electricity Required ========
    @Property(float, notify=gridElectricityRequiredChanged) #getter
    def gridElectricityRequired(self) -> float:
        return self.grid_electricity_required_kwh_per_day

    @gridElectricityRequired.setter #setter
    def gridElectricityRequired(self, value:float) -> None:
        if self.grid_electricity_required_kwh_per_day != value:
            self.grid_electricity_required_kwh_per_day = value
            self.gridElectricityRequiredChanged.emit()


    @Slot()
    def updateGridElectricityRequiredPerDay(self):
        if (new_value := self.off_peak_electricity_required_kwh_per_day + self.peak_electricity_charged_from_grid_kwh_per_day) != self.grid_electricity_required_kwh_per_day:
            self.grid_electricity_required_kwh_per_day = new_value
            self.gridElectricityRequiredChanged.emit()
