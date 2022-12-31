from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class DcChargerDemandSection(QObject):
    dcChargerDemandChanged = Signal()
    dcChargerDemandElementChanged = Signal(int, name="index")

    loadOnEssChanged = Signal()
    loadOnEssElementChanged = Signal(int, name="index")

    essChargeChanged = Signal()
    essChargeElementChanged = Signal(int, name="index")

    essStateOfChargeChanged = Signal()
    essStateOfChargeElementChanged = Signal(int, name="index")


    def __init__(self,
        dc_charger_demand: list = ([0.0]*5) + ([32.4] * 17) + [0.0, 0.0],
        load_on_ess: list = ([0.0]*5) + ([3.6] * 17) + [0.0, 0.0],
        ess_charge: list = [28.8, 57.6, 86.4, 115.2, 144.0, 140.4, 136.8, 133.2, 129.6, 126.0, 122.4, 118.8,
        	                115.2, 111.6, 108.0, 104.4, 100.8, 97.2, 93.6, 90.0, 86.4, 82.8, 111.6, 140.4],
        ess_state_of_charge : list = [0.8, 0.16, 0.24, 0.33, 0.41, 0.40, 0.39, 0.38, 0.37, 0.36, 0.35, 0.34,
                                    0.33, 0.32, 0.31, 0.29, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23, 0.32, 0.40]
    ):
        super().__init__()

        self.dc_charger_demand: list = dc_charger_demand
        self.load_on_ess: list = load_on_ess
        self.ess_charge: list = ess_charge
        self.ess_state_of_charge: list = ess_state_of_charge

    def emitUpdateSignals(self):
        self.dcChargerDemandChanged.emit()
        self.loadOnEssChanged.emit()
        self.essChargeChanged.emit()
        self.essStateOfChargeChanged.emit()

# ================================================================
    @Property(list, notify=dcChargerDemandChanged) #getter
    def dcChargerDemand(self) -> list:
        return self.dc_charger_demand

    @dcChargerDemand.setter
    def dcChargerDemand(self, dc_charger_demand:list) -> None:
        self.dc_charger_demand = dc_charger_demand
        self.dcChargerDemandChanged.emit()

    @Slot(int, float)
    def setDcChargerDemandElement(self, index:int, dc_charger_demand:float):
        self.dc_charger_demand[index] = dc_charger_demand
        self.dcChargerDemandElementChanged.emit(index)
        self.dcChargerDemandChanged.emit()            

# ================================================================
    @Property(list, notify=loadOnEssChanged) #getter
    def loadOnEss(self) -> list:
        return self.load_on_ess

    @loadOnEss.setter
    def loadOnEss(self, load_on_ess:list) -> None:
        self.load_on_ess = load_on_ess
        self.loadOnEssChanged.emit()

    @Slot(int, float)
    def setLoadOnEssElement(self, index:int, load_on_ess:float):
        self.load_on_ess[index] = load_on_ess
        self.loadOnEssElementChanged.emit(index)
        self.loadOnEssChanged.emit()            

# ================================================================
    @Property(list, notify=essChargeChanged) #getter
    def essCharge(self) -> list:
        return self.ess_charge

    @loadOnEss.setter
    def essCharge(self, ess_charge:list) -> None:
        self.ess_charge = ess_charge
        self.essChargeChanged.emit()

    @Slot(int, float)
    def setEssChargeElement(self, index:int, ess_charge:float):
        self.ess_charge[index] = ess_charge
        self.essChargeElementChanged.emit(index)
        self.essChargeChanged.emit()            

# ================================================================
    @Property(list, notify=essStateOfChargeChanged) #getter
    def essStateOfCharge(self) -> list:
        return self.ess_state_of_charge

    @essStateOfCharge.setter
    def essStateOfCharge(self, ess_state_of_charge:list) -> None:
        self.ess_state_of_charge = ess_state_of_charge
        self.essStateOfChargeChanged.emit()

    @Slot(int, float)
    def setEssStateOfChargeElement(self, index:int, ess_state_of_charge:float):
        self.ess_state_of_charge[index] = ess_state_of_charge
        self.essStateOfChargeElementChanged.emit(index)
        self.essStateOfChargeChanged.emit()            



