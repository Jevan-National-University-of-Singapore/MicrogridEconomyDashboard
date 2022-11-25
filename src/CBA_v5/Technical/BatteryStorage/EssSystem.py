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

    # read only signals
    chargeRateChanged = Signal()
    maximumPowerChanged = Signal()
    depthOfDischargePercentageChanged = Signal()

    ''' *****************************
                init
    ******************************** '''
    def __init__(self,
        # required
        charge_rate_cRate: float = 0.51,
        maximum_power_kw: float = 180,

        # optional ()
        installed_capacity: float = 354,
        operational_time_percentage: float = 0.9,
        state_of_charge_upper_limit: float = 0.9,
        state_of_charge_lower_limit: float = 0.1,
        end_of_life_capacity_percentage: float = 0.8,
        ess_nameplate_lifecycle: int = 3059.51
    ):
        super().__init__()

        # user input/assumptions
        self._installed_capacity_kwh = installed_capacity
        self._operational_time_percentage = operational_time_percentage
        self._state_of_charge_upper_limit_percentage = state_of_charge_upper_limit
        self._state_of_charge_lower_limit_percentage = state_of_charge_lower_limit
        self._end_of_life_capacity_percentage = end_of_life_capacity_percentage
        self._ess_nameplate_lifecycle = ess_nameplate_lifecycle

        # read-only/derived variables
        self._charge_rate_cRate = charge_rate_cRate
        self._maximum_power_kw = maximum_power_kw
        self._depth_of_discharge_percentage = state_of_charge_upper_limit - state_of_charge_lower_limit

        self._depth_of_discharge_percentage = self._state_of_charge_upper_limit_percentage - self._state_of_charge_lower_limit_percentage

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
        
    ''' *****************************************************
                QML(UI) getters and setters (front-end)
    ***************************************************** '''
    ### User Assumptions
    # ======== Installed Capacity ========
    @Property(str, notify=installedCapacityChanged) #getter
    def installedCapacity(self):
        return str(self._installed_capacity_kwh)

    @installedCapacity.setter #setter
    def installedCapacity(self, installed_capacity):
        self._installed_capacity_kwh = float(installed_capacity)
        self.installedCapacityChanged.emit()

    # ======== Operational Time ========
    @Property(str, notify=operationalTimeChanged)
    def operationalTime(self):
        return str(self._operational_time_percentage)

    @operationalTime.setter
    def operationalTime(self, operational_time_percentage):
        self._operational_time_percentage = float(operational_time_percentage)
        self.operationalTimeChanged.emit()

    # ======== State of Charge Upper Limit ========
    @Property(str, notify=stateOfChargeUpperLimitChanged)
    def stateOfChargeUpperLimit(self):
        return str(self._state_of_charge_upper_limit_percentage)

    @stateOfChargeUpperLimit.setter
    def stateOfChargeUpperLimit(self, state_of_charge_upper_limit):
        self._state_of_charge_upper_limit_percentage = float(state_of_charge_upper_limit)
        self.stateOfChargeUpperLimitChanged.emit()

    # ======== State of Charge Lower Limit ========
    @Property(str, notify=stateOfChargeLowerLimitChanged)
    def stateOfChargeLowerLimit(self):
        return str(self._state_of_charge_lower_limit_percentage)

    @stateOfChargeLowerLimit.setter
    def stateOfChargeLowerLimit(self, state_of_charge_lower_limit):
        self._state_of_charge_lower_limit_percentage = float(state_of_charge_lower_limit)
        self.stateOfChargeLowerLimitChanged.emit()

    # ======== End of Life Capacity ========
    @Property(str, notify=endOfLifeCapacityChanged)
    def endOfLifeCapacity(self):
        return str(self._end_of_life_capacity_percentage)

    @endOfLifeCapacity.setter
    def endOfLifeCapacity(self, end_of_life_capacity_percentage):
        self._end_of_life_capacity_percentage = float(end_of_life_capacity_percentage)
        self.essNameplateLifecycleChanged.emit()

    # ======== ESS Namplate Lifecycle ========
    @Property(str, notify=essNameplateLifecycleChanged)
    def essNameplateLifecycle(self):
        return str(self._ess_nameplate_lifecycle)

    @essNameplateLifecycle.setter
    def essNameplateLifecycle(self, ess_nameplate_lifecycle):
        self._ess_nameplate_lifecycle = int(ess_nameplate_lifecycle)
        self.essNameplateLifecycleChanged.emit()

    ### Read Only Properties
    # ======== Charge Rate ========
    @Property(str, notify=chargeRateChanged)
    def chargeRate(self):
        return str(self._charge_rate_cRate)

    @chargeRate.setter
    def chargeRate(self, charge_rate_cRate):
        self._charge_rate_cRate = float(charge_rate_cRate)
        self.chargeRateChanged.emit()
    
    # ======== Maximum Power ========
    @Property(str, notify=maximumPowerChanged)
    def maximumPower(self):
        return str(self._maximum_power_kw)

    @maximumPower.setter
    def maximumPower(self, maximum_power_kw):
        self._maximum_power_kw = float(maximum_power_kw)
        self.maximumPowerChanged.emit()

    # ======== Depth of Discharge ========    
    @Property(str, notify=depthOfDischargePercentageChanged)
    def depthOfDischargePercentage(self):
        return str(self._depth_of_discharge_percentage)

    @depthOfDischargePercentage.setter
    def depthOfDischargePercentage(self, depth_of_discharge_percentage):
        self._depth_of_discharge_percentage = float(depth_of_discharge_percentage)
        self.depthOfDischargePercentageChanged.emit()

    @Slot()
    def updateDepthOfDischarge(self):
        self._depth_of_discharge_percentage = self._state_of_charge_upper_limit_percentage - self._state_of_charge_lower_limit_percentage
        self.depthOfDischargePercentageChanged.emit()
