from typing import Optional

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class EssSystem(QObject):
    ''' *****************************
    Energy Storage System Calculations

    - signals
    - init
    - properties
    ******************************** '''
    ''' *****************************
            property signals
    ******************************** '''
    # user assumptions signals
    installedCapacityChanged = Signal()
    operationalTimeChanged = Signal()
    stateOfChargeUpperLimitChanged = Signal()
    stateOfChargeLowerLimitChanged = Signal()
    endOfLifeCapacityChanged = Signal()
    essNameplateLifecycleChanged = Signal()

    chargingStrategyChanged = Signal()

    # read only signals
    chargeRateChanged = Signal()
    maximumPowerChanged = Signal()
    depthOfDischargePercentageChanged = Signal()

    ''' *****************************
                init
    ******************************** '''
    def __init__(self,
        installed_capacity: float = 354,
        operational_time_percentage: float = 0.9,
        state_of_charge_upper_limit: float = 0.9,
        state_of_charge_lower_limit: float = 0.1,
        end_of_life_capacity_percentage: float = 0.8,
        ess_nameplate_lifecycle: float = 3059.51,

        charging_strategy: int = 1
    ):
        super().__init__()
        self.installed_capacity_kwh:float = installed_capacity
        self.operational_time_percentage:float = operational_time_percentage
        self.state_of_charge_upper_limit_percentage:float = state_of_charge_upper_limit
        self.state_of_charge_lower_limit_percentage:float = state_of_charge_lower_limit
        self.end_of_life_capacity_percentage:float = end_of_life_capacity_percentage
        self.ess_nameplate_lifecycle:float = ess_nameplate_lifecycle

        self.charging_strategy: int = charging_strategy

        self.charge_rate_cRate: float = 0
        self.maximum_power_kw: float = 0
        self.depth_of_discharge_percentage: float = 0

        '''****************************************
                    CONNECTIONS
        ****************************************'''   
        self.stateOfChargeLowerLimitChanged.connect(self.updateDepthOfDischarge)
        self.stateOfChargeUpperLimitChanged.connect(self.updateDepthOfDischarge)

    def emitUpdateSignals(self):
        self.installedCapacityChanged.emit()
        self.operationalTimeChanged.emit()
        self.stateOfChargeUpperLimitChanged.emit()
        self.stateOfChargeLowerLimitChanged.emit()
        self.endOfLifeCapacityChanged.emit()
        self.essNameplateLifecycleChanged.emit()

        self.chargeRateChanged.emit()
        self.maximumPowerChanged.emit()
        self.depthOfDischargePercentageChanged.emit()
        self.chargingStrategyChanged.emit()
        
    ''' *****************************************************
                QML(UI) getters and setters (front-end)
    ***************************************************** '''
    ### User Assumptions
    # ======== Installed Capacity ========
    @Property(float, notify=installedCapacityChanged) #getter
    def installedCapacity(self) -> float:
        return self.installed_capacity_kwh

    @installedCapacity.setter #setter
    def installedCapacity(self, installed_capacity:float):
        if self.installed_capacity_kwh != installed_capacity:
            self.installed_capacity_kwh = installed_capacity
            self.installedCapacityChanged.emit()

    # ======== Operational Time ========
    @Property(float, notify=operationalTimeChanged)
    def operationalTime(self) -> float:
        return self.operational_time_percentage

    @operationalTime.setter
    def operationalTime(self, operational_time_percentage):
        if self.operational_time_percentage != operational_time_percentage:
            self.operational_time_percentage = operational_time_percentage
            self.operationalTimeChanged.emit()

    # ======== State of Charge Upper Limit ========
    @Property(float, notify=stateOfChargeUpperLimitChanged)
    def stateOfChargeUpperLimit(self) -> float:
        return self.state_of_charge_upper_limit_percentage

    @stateOfChargeUpperLimit.setter
    def stateOfChargeUpperLimit(self, state_of_charge_upper_limit):
        if self.state_of_charge_upper_limit_percentage != state_of_charge_upper_limit:
            self.state_of_charge_upper_limit_percentage = state_of_charge_upper_limit
            self.stateOfChargeUpperLimitChanged.emit()

    # ======== State of Charge Lower Limit ========
    @Property(float, notify=stateOfChargeLowerLimitChanged)
    def stateOfChargeLowerLimit(self)->float:
        return self.state_of_charge_lower_limit_percentage

    @stateOfChargeLowerLimit.setter
    def stateOfChargeLowerLimit(self, state_of_charge_lower_limit:float):
        if self.state_of_charge_lower_limit_percentage != state_of_charge_lower_limit:
            self.state_of_charge_lower_limit_percentage = state_of_charge_lower_limit
            self.stateOfChargeLowerLimitChanged.emit()

    # ======== End of Life Capacity ========
    @Property(float, notify=endOfLifeCapacityChanged)
    def endOfLifeCapacity(self)->float:
        return self.end_of_life_capacity_percentage

    @endOfLifeCapacity.setter
    def endOfLifeCapacity(self, end_of_life_capacity_percentage: float):
        if self.end_of_life_capacity_percentage != end_of_life_capacity_percentage:
            self.end_of_life_capacity_percentage = end_of_life_capacity_percentage
            self.essNameplateLifecycleChanged.emit()

    # ======== ESS Namplate Lifecycle ========
    @Property(float, notify=essNameplateLifecycleChanged)
    def essNameplateLifecycle(self)->float:
        return self.ess_nameplate_lifecycle

    @essNameplateLifecycle.setter
    def essNameplateLifecycle(self, ess_nameplate_lifecycle: float):
        if self.ess_nameplate_lifecycle != ess_nameplate_lifecycle:
            self.ess_nameplate_lifecycle = ess_nameplate_lifecycle
            self.essNameplateLifecycleChanged.emit()

    ### Read Only Properties
    # ======== Charge Rate ========
    @Property(float, notify=chargeRateChanged)
    def chargeRate(self)->float:
        return self.charge_rate_cRate

    @chargeRate.setter
    def chargeRate(self, charge_rate_cRate):
        if self.charge_rate_cRate != charge_rate_cRate:
            self.charge_rate_cRate = charge_rate_cRate
            self.chargeRateChanged.emit()
    
    # ======== Maximum Power ========
    @Property(float, notify=maximumPowerChanged)
    def maximumPower(self)->float:
        return self.maximum_power_kw

    @maximumPower.setter
    def maximumPower(self, maximum_power_kw):
        if self.maximum_power_kw != maximum_power_kw:
            self.maximum_power_kw = maximum_power_kw
            self.maximumPowerChanged.emit()

    # ======== Depth of Discharge ========    
    @Property(float, notify=depthOfDischargePercentageChanged)
    def depthOfDischargePercentage(self)->float:
        return self.depth_of_discharge_percentage

    @depthOfDischargePercentage.setter
    def depthOfDischargePercentage(self, depth_of_discharge_percentage):
        if self.depth_of_discharge_percentage != depth_of_discharge_percentage:
            self.depth_of_discharge_percentage = depth_of_discharge_percentage
            self.depthOfDischargePercentageChanged.emit()

    @Property(int, notify=chargingStrategyChanged) #getter
    def chargingStrategy(self) -> int:
        return self.charging_strategy
    
    @chargingStrategy.setter
    def chargingStrategy(self, charging_strategy:int):
        if charging_strategy != self.charging_strategy and charging_strategy:
            self.charging_strategy = charging_strategy
            self.chargingStrategyChanged.emit()

    # @Property(float, notify=chargingStrategyChanged) #getter
    # def powerContinuous(self) -> float:
    #     return self.power_continuous

    # @powerContinuous.setter #setter
    # def powerContinuous(self, power_continuous:float) -> None:
    #     if self.power_continuous != power_continuous:
    #         self.power_continuous = power_continuous
    #         self.powerContinuousChanged.emit()

    @Slot()
    def updateDepthOfDischarge(self):
        if (new_value := self.state_of_charge_upper_limit_percentage - self.state_of_charge_lower_limit_percentage) != self.depth_of_discharge_percentage:
            self.depth_of_discharge_percentage = new_value
            self.depthOfDischargePercentageChanged.emit()
