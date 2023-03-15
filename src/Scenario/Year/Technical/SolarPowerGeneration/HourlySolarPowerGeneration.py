from typing import Optional

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class HourlySolarPowerGeneration(QObject):
    dailyGenerationChanged = Signal()

    percentageOfMaxKwChanged = Signal()
    percentageOfMaxKwElementChanged = Signal(int)

    totalPercentageOfMaxKwChanged = Signal()

    percentageOfDailyKwhChanged = Signal()
    percentageOfDailyKwhElementChanged = Signal(int)

    estimatedKwhGeneratedChanged = Signal()
    estimatedKwhGeneratedElementChanged = Signal(int)

    def __init__(self,
            percentage_of_max_kw: Optional[list[float]] = None
        ):
        super().__init__()
        self.daily_generation: float = 0
        self.percentage_of_max_kw: list = [0, 0, 0, 0, 0, 0, 0.05, 0.26, 0.54, 0.76, 0.91, 1, 0.98, 0.9, 0.75, 0.53, 0.3, 0.09, 0, 0, 0, 0, 0, 0] if percentage_of_max_kw is None else percentage_of_max_kw

        self.total_percentage_of_max_kw: float = sum(self.percentage_of_max_kw)

        self.percentage_of_daily_kwh: list = [percentage/self.total_percentage_of_max_kw for percentage in self.percentage_of_max_kw]
        self.estimated_kwh_generated: list = [percentage*self.daily_generation for percentage in self.percentage_of_daily_kwh]

        self.percentageOfMaxKwElementChanged.connect(self.updateTotalPercentageOfMaxKw)

        self.totalPercentageOfMaxKwChanged.connect(self.updatePercentageOfDailyKwh)
        self.percentageOfMaxKwElementChanged.connect(self.updatePercentageOfDailyKwhElement)

        self.dailyGenerationChanged.connect(self.updateEstimatedKwhGenerated)
        self.percentageOfDailyKwhElementChanged.connect(self.updateEstimatedKwhGeneratedElement)

    def emitUpdateSignals(self):
        self.dailyGenerationChanged.emit()
        self.percentageOfMaxKwChanged.emit()
        self.totalPercentageOfMaxKwChanged.emit()
        self.percentageOfDailyKwhChanged.emit()
        self.estimatedKwhGeneratedChanged.emit()

        for i in range(24):
            self.percentageOfMaxKwElementChanged.emit(i)
            self.percentageOfDailyKwhElementChanged.emit(i)
            self.estimatedKwhGeneratedElementChanged.emit(i)
    # ================================================================
    @Property(float, notify=dailyGenerationChanged) #getter
    def dailyGeneration(self) -> float:
        return self.daily_generation

    @dailyGeneration.setter
    def dailyGeneration(self, daily_generation:float) -> None:
        if self.daily_generation != daily_generation:
            self.daily_generation = daily_generation
            self.dailyGenerationChanged.emit()

    # ================================================================
    @Property(list, notify=percentageOfMaxKwChanged) #getter
    def percentageOfMaxKw(self) -> list:
        return self.percentage_of_max_kw

    @percentageOfMaxKw.setter
    def percentageOfMaxKw(self, percentage_of_max_kw:list) -> None:
        if self.percentage_of_max_kw != percentage_of_max_kw:
            self.percentage_of_max_kw = percentage_of_max_kw
            self.percentageOfMaxKwChanged.emit()  

    @Slot(int, float)
    def setPercentageOfMaxKwElement(self, index:int, percentage_of_max_kw:float):
        if self.percentage_of_max_kw[index] != percentage_of_max_kw:
            self.percentage_of_max_kw[index] = percentage_of_max_kw
            self.percentageOfMaxKwElementChanged.emit(index) 
            self.percentageOfMaxKwChanged.emit()              

    # ================================================================
    @Property(float, notify=totalPercentageOfMaxKwChanged) #getter
    def totalPercentageOfMaxKw(self) -> float:
        return self.total_percentage_of_max_kw

    @totalPercentageOfMaxKw.setter
    def totalPercentageOfMaxKw(self, total_percentage_of_max_kw:float) -> None:
        if self.total_percentage_of_max_kw != total_percentage_of_max_kw:
            self.total_percentage_of_max_kw = total_percentage_of_max_kw
            self.totalPercentageOfMaxKwChanged.emit()

    # ================================================================
    @Property(list, notify=percentageOfDailyKwhChanged) #getter
    def percentageOfDailyKwh(self) -> list:
        return self.percentage_of_daily_kwh

    @percentageOfDailyKwh.setter
    def percentageOfDailyKwh(self, percentage_of_daily_kwh:list) -> None:
        self.percentage_of_daily_kwh = percentage_of_daily_kwh
        self.percentageOfDailyKwhChanged.emit()     

    @Slot(int, float)
    def setPercentageOfDailyKwhElement(self, index:int, percentage_of_daily_kwh:float):
        if self.percentage_of_daily_kwh[index] != percentage_of_daily_kwh:
            self.percentage_of_daily_kwh[index] = percentage_of_daily_kwh
            self.percentageOfDailyKwhElementChanged.emit(index)
            self.percentageOfDailyKwhChanged.emit()           
  
    # ================================================================
    @Property(list, notify=estimatedKwhGeneratedChanged) #getter
    def estimatedKwhGenerated(self) -> list:
        return self.estimated_kwh_generated

    @estimatedKwhGenerated.setter
    def estimatedKwhGenerated(self, estimated_kwh_generated:list) -> None:
        self.estimated_kwh_generated = estimated_kwh_generated
        self.estimatedKwhGeneratedChanged.emit()  

    @Slot(int, float)
    def setEstimatedKwhGeneratedElement(self, index:int, estimated_kwh_generated:float):
        if self.estimated_kwh_generated[index] != estimated_kwh_generated:
            self.estimated_kwh_generated[index] = estimated_kwh_generated
            self.estimatedKwhGeneratedElementChanged.emit(index)
            self.estimatedKwhGeneratedChanged.emit()              
        
    # ================================================================    
    @Slot()
    def updatePercentageOfDailyKwh(self):
        self.percentage_of_daily_kwh = [percentage/self.total_percentage_of_max_kw for percentage in self.percentage_of_max_kw]
        for i in range(24):
            self.percentageOfDailyKwhElementChanged.emit(i)     
        self.percentageOfDailyKwhChanged.emit()       

    @Slot()
    def updateEstimatedKwhGenerated(self):
        for i in range(24):
            self.updateEstimatedKwhGeneratedElement(index = i)


    @Slot(int)
    def updateEstimatedKwhGeneratedElement(self, index:int):
        new_value: float = self.percentage_of_daily_kwh[index]*self.daily_generation
        self.setEstimatedKwhGeneratedElement(index, new_value)

    @Slot()
    def updateTotalPercentageOfMaxKw(self):
        self.total_percentage_of_max_kw = sum(self.percentage_of_max_kw)
        self.totalPercentageOfMaxKwChanged.emit()

    @Slot(int)
    def updatePercentageOfDailyKwhElement(self, index:int):
        new_value: float = self.percentage_of_max_kw[index]/self.total_percentage_of_max_kw
        self.setPercentageOfDailyKwhElement(index, new_value)
        



