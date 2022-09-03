from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from ChargingPorts import ChargingPorts
from Demand import Demand
from Load import Load
from ExcessToFacility import ExcessToFacility
from EvCharacteristics import EvCharacteristics

class ChargingAndDemand(QObject):
    chargingPortsChanged = Signal()
    demandChanged = Signal()
    loadChanged = Signal()
    excessToFacilityChanged = Signal()
    evCharacteristicsChanged = Signal()

    def __init__(self,
        charging_ports: ChargingPorts,
        demand: Demand,
        load: Load,
        excess_to_facility: ExcessToFacility,
        ev_characteristics: EvCharacteristics
    ):
        super().__init__()
        self._charging_ports = charging_ports
        self._demand = demand
        self._load = load
        self._excess_to_facility = excess_to_facility
        self._ev_characteristics = ev_characteristics

    @Property(ChargingPorts, notify=chargingPortsChanged) #getter
    def chargingPorts(self) -> ChargingPorts:
        return self._charging_ports
        
    @Property(Demand, notify=demandChanged) #getter
    def demand(self) -> ChargingPorts:
        return self._demand

    @Property(Load, notify=loadChanged) #getter
    def load(self) -> Load:
        return self._load

    @Property(ExcessToFacility, notify=excessToFacilityChanged) #getter
    def chargingPorts(self) -> ExcessToFacility:
        return self._excess_to_facility

    @Property(EvCharacteristics, notify=evCharacteristicsChanged) #getter
    def chargingPorts(self) -> EvCharacteristics:
        return self._ev_characteristics