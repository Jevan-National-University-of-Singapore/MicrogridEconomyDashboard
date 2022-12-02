from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .InstalledCapacity import InstalledCapacity
from .AyerKerohSiteConditions import AyerKerohSiteConditions

class SolarPowerGeneration(QObject):
    dailyGenerationChanged = Signal()
    percentageOfMaxKwChanged = Signal()
    totalPercentageOfMaxKwChanged = Signal()
    percentageOfDailyKwhChanged = Signal()
    estimatedKwhGeneratedChanged = Signal()

    def __init__(self,
        daily_generation: float = 86.99,
        percentage_of_max_kw: list = [0, 0, 0, 0, 0, 0, 0.05, 0.26, 0.54, 0.76, 0.91, 1, 0.98, 0.9, 0.75, 0.53, 0.3, 0.09, 0, 0, 0, 0, 0, 0]
    ):
        super().__init__()
        self.daily_generation: float = daily_generation
        self.percentage_of_max_kw: list = percentage_of_max_kw

        self.total_percentage_of_max_kw: float = sum(percentage_of_max_kw)

        self.percentage_of_daily_kwh: list = [round(percentage/self.total_percentage_of_max_kw, 4) for percentage in self.percentage_of_max_kw]
        self.estimated_kwh_generated: list = [round(percentage*self.daily_generation, 4) for percentage in self.percentage_of_daily_kwh]

        self.totalPercentageOfMaxKwChanged.connect(self.updatePercentageOfDailyKwh)
        self.percentageOfMaxKwChanged.connect(self.updatePercentageOfDailyKwh)

        self.dailyGenerationChanged.connect(self.updateEstimatedKwhGenerated)
        self.percentageOfDailyKwhChanged.connect(self.updateEstimatedKwhGenerated)

    def emitUpdateSignals(self):
        self.dailyGenerationChanged.emit()
        self.percentageOfMaxKwChanged.emit()
        self.totalPercentageOfMaxKwChanged.emit()
        self.percentageOfDailyKwhChanged.emit()
        self.estimatedKwhGeneratedChanged.emit()

    @Property(str, notify=dailyGenerationChanged) #getter
    def dailyGeneration(self) -> str:
        return str(self.daily_generation)

    @dailyGeneration.setter
    def dailyGeneration(self, daily_generation:str) -> None:
        self.daily_generation = round(float(daily_generation), 2)
        self.dailyGenerationChanged.emit()


    @Property(list, notify=percentageOfMaxKwChanged) #getter
    def percentageOfMaxKw(self) -> list:
        return self.percentage_of_max_kw

    @percentageOfMaxKw.setter
    def percentageOfMaxKw(self, percentage_of_max_kw:list) -> None:
        self.percentage_of_max_kw = percentage_of_max_kw
        self.percentageOfMaxKwChanged.emit()     


    @Property(str, notify=totalPercentageOfMaxKwChanged) #getter
    def totalPercentageOfMaxKw(self) -> str:
        return str(round(self.total_percentage_of_max_kw*100, 2))

    @totalPercentageOfMaxKw.setter
    def totalPercentageOfMaxKw(self, total_percentage_of_max_kw:str) -> None:
        self.total_percentage_of_max_kw = round(float(total_percentage_of_max_kw)/100, 4)
        self.totalPercentageOfMaxKwChanged.emit()


    @Property(list, notify=percentageOfDailyKwhChanged) #getter
    def percentageOfDailyKwh(self) -> list:
        return self.percentage_of_daily_kwh

    @percentageOfDailyKwh.setter
    def percentageOfDailyKwh(self, percentage_of_daily_kwh:list) -> None:
        self.percentage_of_daily_kwh = percentage_of_daily_kwh
        self.percentageOfDailyKwhChanged.emit()     
  

    @Property(list, notify=estimatedKwhGeneratedChanged) #getter
    def estimatedKwhGenerated(self) -> list:
        return self.estimated_kwh_generated

    @estimatedKwhGenerated.setter
    def estimatedKwhGenerated(self, estimated_kwh_generated:list) -> None:
        self.estimated_kwh_generated = estimated_kwh_generated
        self.estimatedKwhGeneratedChanged.emit()     
        
    
    @Slot()
    def updatePercentageOfDailyKwh(self):
        self.percentage_of_daily_kwh: list = [round(percentage/self.total_percentage_of_max_kw, 4) for percentage in self.percentage_of_max_kw]
        self.percentageOfDailyKwhChanged.emit()
        

    @Slot()
    def updateEstimatedKwhGenerated(self):
        self.estimated_kwh_generated: list = [round(percentage*self.daily_generation, 4) for percentage in self.percentage_of_daily_kwh]
        self.estimatedKwhGeneratedChanged.emit()

