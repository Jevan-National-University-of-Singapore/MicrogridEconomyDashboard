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
        charging_ports = None,
        demand = None,
        load = None,
        excess_to_facility = None,
        ev_characteristics = None
    ):
        super().__init__()
        self.charging_ports: ChargingPorts = ChargingPorts() if charging_ports is None else charging_ports
        self.demand_: Demand = Demand() if demand is None else demand
        self.load_: Load = Load() if load is None else load
        self.excess_to_facility: ExcessToFacility = ExcessToFacility() if excess_to_facility is None else excess_to_facility
        self.ev_characteristics: EvCharacteristics = EvCharacteristics() if ev_characteristics is None else ev_characteristics

        self.charging_ports.dc_1_charging_time_per_user = round(self.demand_.state_of_charge_to_be_charged * self.ev_characteristics.capacity_ / self.charging_ports.dc_charger_1_rating, 2)
        self.charging_ports.dc_2_charging_time_per_user = round(self.demand_.state_of_charge_to_be_charged * self.ev_characteristics.capacity_ / self.charging_ports.dc_charger_2_rating, 2)
        self.demand_.actual_energy_served_per_day = round(self.demand_.actual_users_served_per_day * self.load_.required_energy_per_user, 2)
        self.load_.required_energy_per_user = round(self.demand_.state_of_charge_to_be_charged * self.ev_characteristics.capacity_, 2)
        self.load_.required_energy_per_day = round(self.load_.required_energy_per_user * self.demand_.number_of_users_per_day, 2)

        self.demand_.stateOfChargeToBeChargedChanged.connect(self.updateDc1ChargingTimePerUser)
        self.ev_characteristics.capacityChanged.connect(self.updateDc1ChargingTimePerUser)
        self.charging_ports.dcCharger1RatingChanged.connect(self.updateDc1ChargingTimePerUser)

        self.demand_.stateOfChargeToBeChargedChanged.connect(self.updateDc2ChargingTimePerUser)
        self.ev_characteristics.capacityChanged.connect(self.updateDc2ChargingTimePerUser)
        self.charging_ports.dcCharger2RatingChanged.connect(self.updateDc2ChargingTimePerUser)

        self.demand_.numberOfUsersPerDayChanged.connect(self.updateActualEnergyServedPerDay)
        self.load_.requiredEnergyPerUserChanged.connect(self.updateActualEnergyServedPerDay)

        self.demand_.stateOfChargeToBeChargedChanged.connect(self.updateRequiredEnergyPerUser)
        self.ev_characteristics.capacityChanged.connect(self.updateRequiredEnergyPerUser)

        self.load_.requiredEnergyPerUserChanged.connect(self.updateRequiredEnergyPerDay)
        self.demand_.numberOfUsersPerDayChanged.connect(self.updateRequiredEnergyPerDay)

    def emitUpdateSignals(self):
        self.charging_ports.emitUpdateSignals()
        self.demand_.emitUpdateSignals()
        self.load_.emitUpdateSignals()
        self.excess_to_facility.emitUpdateSignals()
        self.ev_characteristics.emitUpdateSignals()

    @Property(ChargingPorts, notify=chargingPortsChanged) #getter
    def chargingPorts(self) -> ChargingPorts:
        return self.charging_ports
        
    @Property(Demand, notify=demandChanged) #getter
    def demand(self) -> Demand:
        return self.demand_

    @Property(Load, notify=loadChanged) #getter
    def load(self) -> Load:
        return self.load_

    @Property(ExcessToFacility, notify=excessToFacilityChanged) #getter
    def excessToFacility(self) -> ExcessToFacility:
        return self.excess_to_facility

    @Property(EvCharacteristics, notify=evCharacteristicsChanged) #getter
    def evCharacteristics(self) -> EvCharacteristics:
        return self.ev_characteristics

    @Slot()
    def updateDc1ChargingTimePerUser(self):
        self.charging_ports.dc_1_charging_time_per_user = round(self.demand_.state_of_charge_to_be_charged * self.ev_characteristics.capacity_ / self.charging_ports.dc_charger_1_rating, 2)
        self.charging_ports.dc1ChargingTimePerUserChanged.emit()


    @Slot()
    def updateDc2ChargingTimePerUser(self):
        self.charging_ports.dc_2_charging_time_per_user = round(self.demand_.state_of_charge_to_be_charged * self.ev_characteristics.capacity_ / self.charging_ports.dc_charger_2_rating, 2)
        self.charging_ports.dc2ChargingTimePerUserChanged.emit()


    @Slot()
    def updateActualEnergyServedPerDay(self):
        self.demand_.actual_energy_served_per_day = round(self.demand_.actual_users_served_per_day * self.load_.required_energy_per_user, 2)
        self.demand_.actualEnergyServedPerDayChanged.emit()

    @Slot()
    def updateRequiredEnergyPerUser(self):
        self.load_.required_energy_per_user = round(self.demand_.state_of_charge_to_be_charged * self.ev_characteristics.capacity_, 2)
        self.load_.requiredEnergyPerUserChanged.emit()



    @Slot()
    def updateRequiredEnergyPerDay(self):
        self.load_.required_energy_per_day = round(self.load_.required_energy_per_user * self.demand_.number_of_users_per_day, 2)
        self.load_.requiredEnergyPerDayChanged.emit()

