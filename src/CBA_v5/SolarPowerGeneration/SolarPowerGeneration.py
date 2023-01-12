from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class SolarPowerGeneration(QObject):
    dailyGenerationChanged = Signal()

    percentageOfMaxKwChanged = Signal()
    percentageOfMaxKwElementChanged = Signal(int)
    percentageOfMaxKwElementsChanged = Signal()

    totalPercentageOfMaxKwChanged = Signal()

    percentageOfDailyKwhChanged = Signal()
    percentageOfDailyKwhElementChanged = Signal(int)
    percentageOfDailyKwhElementsChanged = Signal()

    estimatedKwhGeneratedChanged = Signal()
    estimatedKwhGeneratedElementChanged = Signal(int)
    estimatedKwhGeneratedElementsChanged = Signal()


    def __init__(self,
        daily_generation: float = 86.99,
        percentage_of_max_kw: list|None = None
    ):
        super().__init__()
        self.daily_generation: float = daily_generation
        self.percentage_of_max_kw: list = [0, 0, 0, 0, 0, 0, 0.05, 0.26, 0.54, 0.76, 0.91, 1, 0.98, 0.9, 0.75, 0.53, 0.3, 0.09, 0, 0, 0, 0, 0, 0] if percentage_of_max_kw is None else percentage_of_max_kw

        self.total_percentage_of_max_kw: float = round(sum(self.percentage_of_max_kw), 4)

        self.percentage_of_daily_kwh: list = [round(percentage/self.total_percentage_of_max_kw, 4) for percentage in self.percentage_of_max_kw]
        self.estimated_kwh_generated: list = [round(percentage*self.daily_generation, 4) for percentage in self.percentage_of_daily_kwh]

        self.percentageOfMaxKwElementChanged.connect(self.updateTotalPercentageOfMaxKw)

        self.totalPercentageOfMaxKwChanged.connect(self.updatePercentageOfDailyKwh)
        self.percentageOfMaxKwElementsChanged.connect(self.updatePercentageOfDailyKwh)
        self.percentageOfMaxKwElementChanged.connect(self.updatePercentageOfDailyKwhElement)

        self.dailyGenerationChanged.connect(self.updateEstimatedKwhGenerated)
        self.percentageOfDailyKwhElementsChanged.connect(self.updateEstimatedKwhGenerated)
        self.percentageOfDailyKwhElementChanged.connect(self.updateEstimatedKwhGeneratedElement)

    def emitUpdateSignals(self):
        self.dailyGenerationChanged.emit()
        self.percentageOfMaxKwChanged.emit()
        self.totalPercentageOfMaxKwChanged.emit()
        self.percentageOfDailyKwhChanged.emit()
        self.estimatedKwhGeneratedChanged.emit()
    # ================================================================
    @Property(str, notify=dailyGenerationChanged) #getter
    def dailyGeneration(self) -> str:
        return str(self.daily_generation)

    @dailyGeneration.setter
    def dailyGeneration(self, daily_generation:str) -> None:
        self.daily_generation = round(float(daily_generation), 2)
        self.dailyGenerationChanged.emit()

    # ================================================================
    @Property(list, notify=percentageOfMaxKwChanged) #getter
    def percentageOfMaxKw(self) -> list:
        return self.percentage_of_max_kw

    @percentageOfMaxKw.setter
    def percentageOfMaxKw(self, percentage_of_max_kw:list) -> None:
        self.percentage_of_max_kw = percentage_of_max_kw
        self.percentageOfMaxKwChanged.emit()  

    @Slot(int, float)
    def setPercentageOfMaxKwElement(self, index:int, percentage_of_max_kw:float): #investigating main
        self.percentage_of_max_kw[index] = percentage_of_max_kw
        self.percentageOfMaxKwElementChanged.emit(index) 
        self.percentageOfMaxKwChanged.emit()              

    # ================================================================
    @Property(str, notify=totalPercentageOfMaxKwChanged) #getter
    def totalPercentageOfMaxKw(self) -> str:
        return str(round(self.total_percentage_of_max_kw*100, 2))

    @totalPercentageOfMaxKw.setter
    def totalPercentageOfMaxKw(self, total_percentage_of_max_kw:str) -> None:
        self.total_percentage_of_max_kw = round(float(total_percentage_of_max_kw)/100, 4)
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
        self.estimated_kwh_generated[index] = estimated_kwh_generated
        self.estimatedKwhGeneratedElementChanged.emit(index)
        self.estimatedKwhGeneratedChanged.emit()              
        
    # ================================================================    
    @Slot()
    def updatePercentageOfDailyKwh(self):
        self.percentage_of_daily_kwh = [round(percentage/self.total_percentage_of_max_kw, 4) for percentage in self.percentage_of_max_kw]
        self.percentageOfDailyKwhElementsChanged.emit()
        

    @Slot()
    def updateEstimatedKwhGenerated(self):
        self.estimated_kwh_generated = [round(percentage*self.daily_generation, 4) for percentage in self.percentage_of_daily_kwh]
        self.estimatedKwhGeneratedElementsChanged.emit()

    @Slot()
    def updateTotalPercentageOfMaxKw(self):
        self.total_percentage_of_max_kw = round(sum(self.percentage_of_max_kw), 4)
        self.totalPercentageOfMaxKwChanged.emit()

    @Slot(int)
    def updatePercentageOfDailyKwhElement(self, index:int): #investigating
        new_value: float = round(
                self.percentage_of_max_kw[index]/self.total_percentage_of_max_kw,
                4
            ) 
        self.setPercentageOfDailyKwhElement(index, new_value)
        

    @Slot(int)
    def updateEstimatedKwhGeneratedElement(self, index:int):
        new_value: float = round(
            self.percentage_of_daily_kwh[index]*self.daily_generation,
            4
        )
        self.setEstimatedKwhGeneratedElement(index, new_value)

