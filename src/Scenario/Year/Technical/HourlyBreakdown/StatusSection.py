from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class StatusSection(QObject):
    chargeSufficiencyChanged = Signal()
    chargeSufficiencyElementChanged = Signal(int)

    chargeStatusChanged = Signal()
    chargeStatusElementChanged = Signal(int)

    chargerNeededChanged = Signal()
    chargerNeededElementChanged = Signal(int)

    reachedEssStateOfChargeChanged = Signal()
    reachedEssStateOfChargeElementChanged = Signal(int)

    avilabilityChanged = Signal()
    avilabilityElementChanged = Signal(int)

    def __init__(self,
        charge_sufficiency: list = [True]*24,
        charge_status: list = (["Charge"]*5)+(["Discharge"]*17)+(["Charge", "Charge"]),
        charger_needed: list = ([False]*5)+([True]*17)+([False, False]),
        reached_ess_state_of_charge : list = [False]*24,
        availability: list = [True] *24
    ):
        super().__init__()

        self.charge_sufficiency: list = charge_sufficiency.copy()
        self.charge_status: list = charge_status.copy()
        self.charger_needed: list = charger_needed.copy()
        self.reached_ess_state_of_charge: list = reached_ess_state_of_charge.copy()
        self.avilability_: list = availability.copy()

    def emitUpdateSignals(self):
        self.chargeSufficiencyChanged.emit()
        self.chargeStatusChanged.emit()
        self.chargerNeededChanged.emit()
        self.reachedEssStateOfChargeChanged.emit()

        for i in range(24):
            self.chargeSufficiencyElementChanged.emit(i)
            self.chargeStatusElementChanged.emit(i)
            self.chargerNeededElementChanged.emit(i)
            self.reachedEssStateOfChargeElementChanged.emit(i)
            self.avilabilityElementChanged.emit(i)

    # ================================================================
    @Property(list, notify=chargeSufficiencyChanged) #getter
    def chargeSufficiency(self) -> list:
        return self.charge_sufficiency

    @chargeSufficiency.setter
    def chargeSufficiency(self, charge_sufficiency:list) -> None:
        self.charge_sufficiency = charge_sufficiency
        self.chargeSufficiencyChanged.emit()

    @Slot(int, float)
    def setChargeSufficiencyElement(self, index:int, charge_sufficiency:float):
        if self.charge_sufficiency[index] != charge_sufficiency:
            self.charge_sufficiency[index] = charge_sufficiency
            self.chargeSufficiencyElementChanged.emit(index)
            self.chargeSufficiencyChanged.emit()

    # ================================================================
    @Property(list, notify=chargeStatusChanged) #getter
    def chargeStatus(self) -> list:
        return self.charge_status

    @chargeStatus.setter
    def chargeStatus(self, charge_status:list) -> None:
        self.charge_status = charge_status
        self.chargeStatusChanged.emit()   

    @Slot(int, float)
    def setChargeStatusElement(self, index:int, charge_status:float):
        self.charge_status[index] = charge_status
        self.chargeStatusElementChanged.emit(index)
        self.chargeStatusChanged.emit()        

    # ================================================================
    @Property(list, notify=chargerNeededChanged) #getter
    def chargerNeeded(self) -> list:
        return self.charger_needed

    @chargerNeeded.setter
    def chargerNeeded(self, charger_needed:list) -> None:
        self.charger_needed = charger_needed
        self.chargerNeededChanged.emit()

    @Slot(int, float)
    def setChargerNeededElement(self, index:int, charger_needed:float):
        self.charger_needed[index] = charger_needed
        self.chargerNeededElementChanged.emit(index)
        self.chargerNeededChanged.emit()        

    # ================================================================
    @Property(list, notify=reachedEssStateOfChargeChanged) #getter
    def reachedEssStateOfCharge(self) -> list:
        return self.reached_ess_state_of_charge

    @reachedEssStateOfCharge.setter
    def reachedEssStateOfCharge(self, reached_ess_state_of_charge:list) -> None:
        self.reached_ess_state_of_charge = reached_ess_state_of_charge
        self.reachedEssStateOfChargeChanged.emit()     

    @Slot(int, float)
    def setReachedEssStateOfChargeElement(self, index:int, reached_ess_state_of_charge:float):
        self.reached_ess_state_of_charge[index] = reached_ess_state_of_charge
        self.reachedEssStateOfChargeElementChanged.emit(index)
        self.reachedEssStateOfChargeChanged.emit()        
    # ================================================================
    @Property(list, notify=avilabilityChanged) #getter
    def availability(self) -> list:
        return self.avilability_

    @availability.setter
    def availability(self, avilability:list) -> None:
        self.avilability_ = avilability
        self.avilabilityChanged.emit()

    @Slot(int, float)
    def setAvailabilityElement(self, index:int, avilability_:float):
        self.avilability_[index] = avilability_
        self.avilabilityElementChanged.emit(index)
        self.avilabilityChanged.emit()        
    # ================================================================

'''
Unavilable

O52: Charger needed
O51: 
=IF(O52="YES",IF(O51="Charge","NO","YES"),"YES")



'''