from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class AyerKerohSiteConditions(QObject):
    specificPvPowerOutputPerDayChanged = Signal()
    specificPvPowerOutputPerYearChanged = Signal()

    def __init__(self,
        specific_pv_power_output_per_day: float = 3.58
    ):
        super().__init__()
        self.specific_pv_power_output_per_day: float = specific_pv_power_output_per_day

        self.specific_pv_power_output_per_year = round(self.specific_pv_power_output_per_day * 365, 2)
        self.specificPvPowerOutputPerDayChanged.connect(self.update_specificPvPowerOutputPerYear)

    def emitUpdateSignals(self):
        self.specificPvPowerOutputPerDayChanged.emit()
        self.specificPvPowerOutputPerYearChanged.emit()

    
    @Property(str, notify=specificPvPowerOutputPerDayChanged) #getter
    def specificPvPowerOutputPerDay(self) -> str:
        return str(self.specific_pv_power_output_per_day)

    @specificPvPowerOutputPerDay.setter
    def specificPvPowerOutputPerDay(self, specific_pv_power_output_per_day:str) -> None:
        self.specific_pv_power_output_per_day = round(float(specific_pv_power_output_per_day), 2)
        self.specificPvPowerOutputPerDayChanged.emit()

    @Property(str, notify=specificPvPowerOutputPerYearChanged) #getter
    def specificPvPowerOutputPerYear(self) -> str:
        return str(round(self.specific_pv_power_output_per_year, 2))

    @specificPvPowerOutputPerYear.setter
    def specificPvPowerOutputPerYear(self, specific_pv_power_output_per_year:str) -> None:
        self.specific_pv_power_output_per_year = round(float(specific_pv_power_output_per_year), 2)
        self.specificPvPowerOutputPerYearChanged.emit()

    @Slot()
    def update_specificPvPowerOutputPerYear(self):
        self.specific_pv_power_output_per_year = round(self.specific_pv_power_output_per_day * 365, 2)
        self.specificPvPowerOutputPerYearChanged.emit()




