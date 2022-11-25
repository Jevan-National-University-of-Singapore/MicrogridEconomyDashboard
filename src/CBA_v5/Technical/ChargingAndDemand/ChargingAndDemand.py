from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .ChargingPorts import ChargingPorts
from .Demand import Demand
from .Load import Load
from .ExcessToFacility import ExcessToFacility
from .EvCharacteristics import EvCharacteristics

class ChargingAndDemand(QObject):
    chargingPortsChanged = Signal()
    demandChanged = Signal()
    loadChanged = Signal()
    excessToFacilityChanged = Signal()
    evCharacteristicsChanged = Signal()

    def __init__(self,
        charging_ports = ChargingPorts(),
        demand = Demand(),
        load = Load(),
        excess_to_facility = ExcessToFacility(),
        ev_characteristics = EvCharacteristics()
    ):
        super().__init__()
        self._charging_ports: ChargingPorts = charging_ports
        self._demand: Demand = demand
        self._load: Load = load
        self._excess_to_facility: ExcessToFacility = excess_to_facility
        self._ev_characteristics: EvCharacteristics = ev_characteristics

        self._demand.stateOfChargeToBeChargedChanged.connect(self.updateDc1ChargingTimePerUser)
        self._ev_characteristics.capacityChanged.connect(self.updateDc1ChargingTimePerUser)
        self._charging_ports.dcCharger1RatingChanged.connect(self.updateDc1ChargingTimePerUser)

        self._demand.stateOfChargeToBeChargedChanged.connect(self.updateDc2ChargingTimePerUser)
        self._ev_characteristics.capacityChanged.connect(self.updateDc2ChargingTimePerUser)
        self._charging_ports.dcCharger2RatingChanged.connect(self.updateDc2ChargingTimePerUser)

        self._demand.actualEnergyServedPerDayChanged.connect(self.updateActualEnergyServedPerDay)
        self._load.requiredEnergyPerUserChanged.connect(self.updateActualEnergyServedPerDay)

        self._demand.stateOfChargeToBeChargedChanged.connect(self.updateRequiredEnergyPerUser)
        self._ev_characteristics.capacityChanged.connect(self.updateRequiredEnergyPerUser)

        self._load.requiredEnergyPerUserChanged.connect(self.updateRequiredEnergyPerDay)
        self._demand.numOfUsersPerDayChanged.connect(self.updateRequiredEnergyPerDay)

    def emitUpdateSignals(self):
        self._charging_ports.emitUpdateSignals()
        self._demand.emitUpdateSignals()
        self._load.emitUpdateSignals()
        self._excess_to_facility.emitUpdateSignals()
        self._ev_characteristics.emitUpdateSignals()

    @Property(ChargingPorts, notify=chargingPortsChanged) #getter
    def chargingPorts(self) -> ChargingPorts:
        return self._charging_ports
        
    @Property(Demand, notify=demandChanged) #getter
    def demand(self) -> Demand:
        return self._demand

    @Property(Load, notify=loadChanged) #getter
    def load(self) -> Load:
        return self._load

    @Property(ExcessToFacility, notify=excessToFacilityChanged) #getter
    def excessToFacility(self) -> ExcessToFacility:
        return self._excess_to_facility

    @Property(EvCharacteristics, notify=evCharacteristicsChanged) #getter
    def evCharacteristics(self) -> EvCharacteristics:
        return self._ev_characteristics

    @Slot()
    def updateDc1ChargingTimePerUser(self):
        self._charging_ports._dc_1_charging_time_per_user = self._demand._state_of_charge_to_be_charged * self._ev_characteristics._capacity / self._charging_ports._dc_charger_1_rating
        self._charging_ports.dc1ChargingTimePerUserChanged.emit()

    @Slot()
    def updateDc2ChargingTimePerUser(self):
        self._charging_ports._dc_2_charging_time_per_user = self._demand._state_of_charge_to_be_charged * self._ev_characteristics._capacity / self._charging_ports._dc_charger_2_rating
        self._charging_ports.dc2ChargingTimePerUserChanged.emit()

    @Slot()
    def updateActualEnergyServedPerDay(self):
        self._demand._actual_energy_served_per_day = self._demand._actual_users_served_per_day * self._load._required_energy_per_user
        self._demand.actualEnergyServedPerDayChanged.emit()

    @Slot()
    def updateRequiredEnergyPerUser(self):
        self._load._required_energy_per_user = self._demand._state_of_charge_to_be_charged * self._ev_characteristics._capacity
        self._load.requiredEnergyPerUserChanged.emit()

    @Slot()
    def updateRequiredEnergyPerDay(self):
        self._load._required_energy_per_day = self._load._required_energy_per_user * self._demand._num_of_users_per_day
        self._load.requiredEnergyPerDayChanged.emit()

