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
        charge_sufficiency: list|None = None,
        charge_status: list|None = None,
        charger_needed: list|None = None,
        reached_ess_state_of_charge : list|None = None,
        availability: list|None = None
    ):
        super().__init__()

        self.charge_sufficiency: list = [True]*24 if charge_sufficiency is None else charge_sufficiency
        self.charge_status: list = (["Charge"]*5)+(["Discharge"]*17)+(["Charge", "Charge"]) if charge_status is None else charge_status
        self.charger_needed: list = ([False]*5)+([True]*17)+([False, False]) if charger_needed is None else charger_needed
        self.reached_ess_state_of_charge: list = [False]*24 if reached_ess_state_of_charge is None else reached_ess_state_of_charge
        self.availability_: list = [True] *24 if availability is None else availability

        self.chargerNeededElementChanged.connect(self.update_availability)
        self.chargeStatusElementChanged.connect(self.update_availability)

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
        return self.availability_

    @availability.setter
    def availability(self, avilability:list) -> None:
        self.availability_ = avilability
        self.avilabilityChanged.emit()

    @Slot(int, float)
    def setAvailabilityElement(self, index:int, avilability_:float):
        self.availability_[index] = avilability_
        self.avilabilityElementChanged.emit(index)
        self.avilabilityChanged.emit()        
    # ================================================================

    @Slot(int)
    def update_availability(self, index:int):
        if not self.charger_needed[index] or self.charge_status[index] == "discharge":
            self.setAvailabilityElement(index, True)
        else:
            self.setAvailabilityElement(index, False)
'''
52:
=IF(charger_needed="YES",
    IF(charge_status="Charge",
        "No",
    else
        "Yes"),
else
    "Yes")
'''