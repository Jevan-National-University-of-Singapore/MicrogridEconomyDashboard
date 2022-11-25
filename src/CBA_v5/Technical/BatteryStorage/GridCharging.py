from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class GridCharging(QObject):
    gridDrawLimitChanged = Signal()

    offPeakElectricityRequiredChanged = Signal()
    peakElectricityChargedFromGridChanged = Signal()
    gridElectricityRequiredChanged = Signal()

    def __init__(self,
        off_peak_electricity_required_kwh_per_day: float = 288,
        peak_electricity_charged_from_grid_kwh_per_day: float = 403.2,

        grid_draw_limit_kw: float = 28.8
    ): 
        super().__init__()
        self._grid_draw_limit_kw = grid_draw_limit_kw

        self._off_peak_electricity_required_kwh_per_day = off_peak_electricity_required_kwh_per_day
        self._peak_electricity_charged_from_grid_kwh_per_day = peak_electricity_charged_from_grid_kwh_per_day
        self._grid_electricity_required_kwh_per_day = off_peak_electricity_required_kwh_per_day + peak_electricity_charged_from_grid_kwh_per_day

        self.offPeakElectricityRequiredChanged.connect(self.updateGridElectricityRequiredPerDay)
        self.peakElectricityChargedFromGridChanged.connect(self.updateGridElectricityRequiredPerDay)

    def emitUpdateSignals(self):
        self.offPeakElectricityRequiredChanged.emit()
        self.peakElectricityChargedFromGridChanged.emit()
        self.gridElectricityRequiredChanged.emit()


    ''' *********************************************
            Python getters and setters (Backend)
    ********************************************* '''
    # @property
    # def grid_draw_limit(self) -> float:
    #     return self._grid_draw_limit_kw

    # @grid_draw_limit.setter
    # def grid_draw_limit(self, value:float):
    #     self._grid_draw_limit_kw = value
    #     self.gridDrawLimitChanged.emit()

    # @property
    # def off_peak_electricity_required(self)->float:
    #     return self._off_peak_electricity_required_kwh_per_day

    # @off_peak_electricity_required.setter
    # def off_peak_electricity_required(self, value:float):
    #     self._off_peak_electricity_required_kwh_per_day = value
    #     self.offPeakElectricityRequiredChanged.emit()
    #     self._grid_electricity_required_kwh_per_day = self._off_peak_electricity_required_kwh_per_day + self._peak_electricity_charged_from_grid_kwh_per_day

    # @property
    # def peak_electricity_charged_from_grid(self)->float:
    #     return self._peak_electricity_charged_from_grid_kwh_per_day

    # @peak_electricity_charged_from_grid.setter
    # def peak_electricity_charged_from_grid(self, value:float):
    #     self._peak_electricity_charged_from_grid_kwh_per_day = value
    #     self.peakElectricityChargedFromGridChanged.emit()

    # @property
    # def grid_electricity_required(self) -> float:
    #     return self._grid_electricity_required_kwh_per_day

    # @grid_electricity_required.setter
    # def grid_electricity_required(self, value:float):
    #     self._grid_electricity_required_kwh_per_day = value
    #     self.gridElectricityRequiredChanged.emit()

    ### User Assumptions
    # ======== Grid Draw Limit ========
    @Property(str, notify=gridDrawLimitChanged) #getter
    def gridDrawLimit(self) -> str:
        return str(self._grid_draw_limit_kw)

    @gridDrawLimit.setter #setter
    def gridDrawLimit(self, value:str) -> None:
        self._grid_draw_limit_kw = float(value)
        self.gridDrawLimitChanged.emit()

    ### Read Only Properties
    # ======== Off Peak Electricity Required ========
    @Property(str, notify=offPeakElectricityRequiredChanged) #getter
    def offPeakElectricityRequired(self) -> str:
        return str(self._off_peak_electricity_required_kwh_per_day)

    @offPeakElectricityRequired.setter #setter
    def offPeakElectricityRequired(self, value:str) -> None:
        self._off_peak_electricity_required_kwh_per_day = float(value)
        self.offPeakElectricityRequiredChanged.emit()

    # ======== Peak Electricity Charged From Grid ========
    @Property(str, notify=peakElectricityChargedFromGridChanged) #getter
    def peakElectricityChargedFromGrid(self) -> str:
        return str(self._peak_electricity_charged_from_grid_kwh_per_day)

    @peakElectricityChargedFromGrid.setter #setter
    def peakElectricityChargedFromGrid(self, value:str) -> None:
        self._peak_electricity_charged_from_grid_kwh_per_day = float(value)
        self.peakElectricityChargedFromGridChanged.emit()

    # ======== Grid Electricity Required ========
    @Property(str, notify=gridElectricityRequiredChanged) #getter
    def gridElectricityRequired(self) -> str:
        return str(self._grid_electricity_required_kwh_per_day)

    @gridElectricityRequired.setter #setter
    def gridElectricityRequired(self, value:str) -> None:
        self._grid_electricity_required_kwh_per_day = float(value)
        self.gridElectricityRequiredChanged.emit()


    @Slot()
    def updateGridElectricityRequiredPerDay(self):
        self._grid_electricity_required_kwh_per_day = self._off_peak_electricity_required_kwh_per_day + self._peak_electricity_charged_from_grid_kwh_per_day
        self.gridElectricityRequiredChanged.emit()
