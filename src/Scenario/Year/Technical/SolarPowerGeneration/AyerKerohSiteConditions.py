from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class AyerKerohSiteConditions(QObject):
    specificPvPowerOutputPerDayChanged = Signal()
    specificPvPowerOutputPerYearChanged = Signal()

    def __init__(self, specific_pv_power_output_per_day: float = 3.58):
        super().__init__()
        self.specific_pv_power_output_per_day: float = specific_pv_power_output_per_day
        self.specific_pv_power_output_per_year:float = self.specific_pv_power_output_per_day * 365
        
        self.specificPvPowerOutputPerDayChanged.connect(self.update_specificPvPowerOutputPerYear)

    def emitUpdateSignals(self):
        self.specificPvPowerOutputPerDayChanged.emit()
        self.specificPvPowerOutputPerYearChanged.emit()

    
    @Property(float, notify=specificPvPowerOutputPerDayChanged) #getter
    def specificPvPowerOutputPerDay(self) -> float:
        return self.specific_pv_power_output_per_day

    @specificPvPowerOutputPerDay.setter
    def specificPvPowerOutputPerDay(self, specific_pv_power_output_per_day:float) -> None:
        if self.specific_pv_power_output_per_day != specific_pv_power_output_per_day:
            self.specific_pv_power_output_per_day = specific_pv_power_output_per_day
            self.specificPvPowerOutputPerDayChanged.emit()

    @Property(float, notify=specificPvPowerOutputPerYearChanged) #getter
    def specificPvPowerOutputPerYear(self) -> float:
        return self.specific_pv_power_output_per_year

    @specificPvPowerOutputPerYear.setter
    def specificPvPowerOutputPerYear(self, specific_pv_power_output_per_year:float) -> None:
        if self.specific_pv_power_output_per_year != specific_pv_power_output_per_year:
            self.specific_pv_power_output_per_year = specific_pv_power_output_per_year
            self.specificPvPowerOutputPerYearChanged.emit()

    @Slot()
    def update_specificPvPowerOutputPerYear(self):
        if (new_value := self.specific_pv_power_output_per_day * 365) != self.specific_pv_power_output_per_year:
            self.specific_pv_power_output_per_year = new_value
            self.specificPvPowerOutputPerYearChanged.emit()




