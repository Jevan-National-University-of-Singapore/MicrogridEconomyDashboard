from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class TotalChargeSupplySection(QObject):
    solarPowerGenerationChanged = Signal()
    solarPowerGenerationElementChanged = Signal(int)

    gridOffPeakChanged = Signal()
    gridOffPeakElementChanged = Signal(int)

    gridPeakChanged = Signal()
    gridPeakElementChanged = Signal(int)
    
    totalChargeSupplyChanged = Signal()
    totalChargeSupplyElementChanged = Signal(int)

    def __init__(self,
        solar_power_generation: list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6, 3.3,	6.6, 9.4, 11.2,	12.3,
                                        12.1, 11.1, 9.3, 6.5, 3.6, 1.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],

        grid_off_peak: list = ([28.8]*8) + ([0]*14) + ([28.8, 28.8]),
        grid_peak: list = ([0]*8) + ([28.8]*14) + ([0,0]),
        total_charge_supply : list = [28.8] * 24
    ):
        super().__init__()

        self.solar_power_generation: list = solar_power_generation
        self.grid_off_peak: list = grid_off_peak
        self.grid_peak: list = grid_peak
        self.total_charge_supply: list = total_charge_supply

        self.total_charge_supply = [grid_off_peak + grid_peak for grid_off_peak, grid_peak in zip(self.grid_off_peak, self.grid_peak)]
        
        self.gridOffPeakElementChanged.connect(self.updateTotalChargeSupply)
        self.gridPeakElementChanged.connect(self.updateTotalChargeSupply)

    def emitUpdateSignals(self):
        self.solarPowerGenerationChanged.emit()
        self.gridOffPeakChanged.emit()
        self.gridPeakChanged.emit()
        self.totalChargeSupplyChanged.emit()

    # ================================================================
    @Property(list, notify=solarPowerGenerationChanged) #getter
    def solarPowerGeneration(self) -> list:
        return self.solar_power_generation

    @solarPowerGeneration.setter
    def solarPowerGeneration(self, solar_power_generation:list) -> None:
        self.solar_power_generation = solar_power_generation
        self.solarPowerGenerationChanged.emit()

    @Slot(int, float)
    def setSolarPowerGenerationElement(self, index:int, solar_power_generation_element:float):
        self.solar_power_generation[index] = solar_power_generation_element
        self.solarPowerGenerationElementChanged.emit(index)
        self.solarPowerGenerationChanged.emit()

    # ================================================================
    @Property(list, notify=gridOffPeakChanged) #getter
    def gridOffPeak(self) -> list:
        return self.grid_off_peak

    @gridOffPeak.setter
    def gridOffPeak(self, grid_off_peak:list) -> None:
        self.grid_off_peak = grid_off_peak
        self.gridOffPeakChanged.emit()    
        
    @Slot(int, float)
    def setGridOffPeakElement(self, index:int, grid_off_peak:float):
        self.grid_off_peak[index] = grid_off_peak
        self.gridOffPeakElementChanged.emit(index)
        self.gridOffPeakChanged.emit()         

    # ================================================================
    @Property(list, notify=gridPeakChanged) #getter
    def gridPeak(self) -> list:
        return self.grid_peak

    @gridPeak.setter
    def gridPeak(self, grid_peak:list) -> None:
        self.grid_peak = grid_peak
        self.gridPeakChanged.emit()     

    @Slot(int, float)
    def setGridPeakElement(self, index:int, grid_peak:float):
        self.grid_peak[index] = grid_peak
        self.gridPeakElementChanged.emit(index)
        self.gridPeakChanged.emit()        

    # ================================================================
    @Property(list, notify=totalChargeSupplyChanged) #getter
    def totalChargeSupply(self) -> list:
        return self.total_charge_supply

    @totalChargeSupply.setter
    def totalChargeSupply(self, total_charge_supply:list) -> None:
        self.total_charge_supply = total_charge_supply
        self.totalChargeSupplyChanged.emit()    

    @Slot(int, float)
    def setTotalChargeSupplyElement(self, index:int, total_charge_supply:float):
        self.total_charge_supply[index] = total_charge_supply
        self.totalChargeSupplyElementChanged.emit(index)
        self.totalChargeSupplyChanged.emit()           

    # ================================================================
    @Slot(int)
    def updateTotalChargeSupply(self, index: int):
        self.setTotalChargeSupplyElement(
            index=index,
            total_charge_supply = self.grid_off_peak[index] + self.grid_peak[index]
        )

