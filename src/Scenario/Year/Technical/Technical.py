from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from typing import Optional

from .SolarPowerGeneration.SolarPowerGeneration import SolarPowerGeneration
from .BatteryStorage.BatteryStorage import BatteryStorage
from .ChargingAndDemand.ChargingAndDemand import ChargingAndDemand
from .HourlyBreakdown.HourlyBreakdown import HourlyBreakdown

# from QModels.QTreeNode import QTreeNode

class Technical(QObject):

    treeNodeChanged = Signal()
    
    batteryStorageChanged = Signal()
    chargingAndDemandChanged = Signal()
    solarPowerGenerationChanged = Signal()
    hourBreakdownChanged = Signal()

    # tree_node: QTreeNode = QTreeNode("Technical")
    # tree_node.add_children([
    #     QTreeNode("first"),
    #     QTreeNode("second"),
    #     QTreeNode("third")
    # ])

    # tree:QTreeModel = QTreeModel(root_data="Technical")

    # second_level_nodes:list[QTreeNode] = [QTreeNode("first child"), QTreeNode("second child"), QTreeNode("third child")]
    # tree.root.add_children(second_level_nodes)

    def __init__(self, 
        name: str = None,
        battery_storage:Optional[BatteryStorage] = None,
        solar_power_generation:Optional[SolarPowerGeneration] = None,
        charging_and_demand:Optional[ChargingAndDemand] = None,
        hourly_breakdown:Optional[HourlyBreakdown] = None
    ):
        super().__init__()
        self.battery_storage:BatteryStorage = BatteryStorage() if battery_storage is None else battery_storage
        self.charging_and_demand:ChargingAndDemand = ChargingAndDemand() if charging_and_demand is None else charging_and_demand
        self.solar_power_generation: SolarPowerGeneration = SolarPowerGeneration() if solar_power_generation is None else solar_power_generation
        self.hourly_breakdown:HourlyBreakdown = HourlyBreakdown() if hourly_breakdown is None else hourly_breakdown

        self.battery_storage.ess_system.charge_rate_cRate = \
            self.charging_and_demand.charging_ports.dc_charger_1_rating / self.battery_storage.ess_system.installed_capacity_kwh \
        if self.battery_storage.ess_system.installed_capacity_kwh else 0

        self.solar_power_generation.hourly_solar_power_generation.estimatedKwhGeneratedElementChanged.connect(self.update_chargingAndDemand_excessToFacility_electricityPerDay)

        self.battery_storage.ess_system.maximum_power_kw = min(
                self.charging_and_demand.charging_ports.dc_charger_1_rating,
                self.charging_and_demand.ev_characteristics.max_power_rating,
                self.battery_storage.discharge_.power_max
            )

        self.charging_and_demand.charging_ports.dcCharger2RatingChanged.connect(self.updateBatteryStorageChargeRate)
        self.battery_storage.ess_system.installedCapacityChanged.connect(self.updateBatteryStorageChargeRate)
        
        self.charging_and_demand.charging_ports.dcCharger1RatingChanged.connect(self.updateBatteryStorageMaximumPower)
        self.charging_and_demand.ev_characteristics.maxPowerRatingChanged.connect(self.updateBatteryStorageMaximumPower)
        self.battery_storage.discharge_.powerMaxChanged.connect(self.updateBatteryStorageMaximumPower)

        self.battery_storage.grid_charging.gridDrawLimitChanged.connect(self.updateAll_hourlyBreakdown_totalChargeSupplySection_gridOffPeak)
        self.battery_storage.grid_charging.gridDrawLimitChanged.connect(self.updateAll_hourlyBreakdown_totalChargeSupplySection_gridPeak)

        self.battery_storage.ess_system.installedCapacityChanged.connect(self.updateAll_hourlyBreakdown_dcChargerDemandSection_essStateOfChargeElement)
        self.hourly_breakdown.dc_charger_demand_section.essChargeElementChanged.connect(self.update_hourlyBreakdown_dcChargerDemandSection_essStateOfChargeElement)

        '''
        update_HourlyBreakdown_statusSection_reachedEssStateOfChargeElement
        '''
        self.hourly_breakdown.dc_charger_demand_section.essChargeElementChanged.connect(self.update_hourlyBreakdown_statusSection_reachedEssStateOfChargeElement)
        self.hourly_breakdown.status_section.chargerNeededElementChanged.connect(self.update_hourlyBreakdown_statusSection_reachedEssStateOfChargeElement)
        self.hourly_breakdown.total_charge_supply_section.totalChargeSupplyElementChanged.connect(self.update_hourlyBreakdown_statusSection_reachedEssStateOfChargeElement)
        self.hourly_breakdown.dc_charger_demand_section.dcChargerDemandElementChanged.connect(self.update_hourlyBreakdown_statusSection_reachedEssStateOfChargeElement)

        self.battery_storage.ess_system.installedCapacityChanged.connect(self.updateAll_hourlyBreakdown_statusSection_reachedEssStateOfChargeElement)
        self.battery_storage.ess_system.stateOfChargeUpperLimitChanged.connect(self.updateAll_hourlyBreakdown_statusSection_reachedEssStateOfChargeElement)
        self.battery_storage.ess_system.stateOfChargeLowerLimitChanged.connect(self.updateAll_hourlyBreakdown_statusSection_reachedEssStateOfChargeElement)

        self.hourly_breakdown.total_charge_supply_section.gridOffPeakElementChanged.connect(self.update_batteryStorage_gridCharging_offPeakElectricityRequiredPerDay)
        self.hourly_breakdown.total_charge_supply_section.gridPeakElementChanged.connect(self.update_batteryStorage_gridCharging_peakElectricityRequiredPerDay)

        self.hourly_breakdown.status_section.chargeSufficiencyElementChanged.connect(self.update_chargingAndDemand_demand_totalWaitingTime)
        self.hourly_breakdown.status_section.chargeStatusElementChanged.connect(self.update_chargingAndDemand_demand_actualUsersServedPerDay)

        '''
        update_HourlyBreakdown_statusSection_essChargeWithLoad -> CHARGING STRATEGY
        '''
        self.hourly_breakdown.total_charge_supply_section.totalChargeSupplyElementChanged.connect(self.update_hourlyBreakdown_dcChargerDemandSection_essChargeWithLoad)
        self.hourly_breakdown.dc_charger_demand_section.loadOnEssElementChanged.connect(self.update_hourlyBreakdown_dcChargerDemandSection_essChargeWithLoad)
        self.hourly_breakdown.status_section.chargeSufficiencyElementChanged.connect(self.update_hourlyBreakdown_dcChargerDemandSection_essChargeWithLoad)
        self.hourly_breakdown.status_section. reachedEssStateOfChargeElementChanged.connect(self.update_hourlyBreakdown_dcChargerDemandSection_essChargeWithLoad)
        self.hourly_breakdown.dc_charger_demand_section.essChargeElementChanged.connect(self.update_hourlyBreakdown_dcChargerDemandSection_essChargeWithLoad)

        self.hourly_breakdown.total_charge_supply_section.totalChargeSupplyElementChanged.connect(self.update_hourlyBreakdown_dcChargerDemandSection_essChargeWithLoad)
        self.battery_storage.ess_system.chargingStrategyChanged.connect(self.update_hourlyBreakdown_dcChargerDemandSection_essChargeWithLoad_)

    def emitUpdateSignals(self):
        self.battery_storage.emitUpdateSignals()
        self.charging_and_demand.emitUpdateSignals()
        self.solar_power_generation.emitUpdateSignals()
        self.hourly_breakdown.emitUpdateSignals()

    # @Property(QTreeNode, notify=treeNodeChanged) #getter
    # def treeNode(self) -> QTreeNode:
    #     return self.tree_node

    @Property(SolarPowerGeneration, notify=solarPowerGenerationChanged) #getter
    def solarPowerGeneration(self) -> SolarPowerGeneration:
        return self.solar_power_generation

    @Property(BatteryStorage, notify=batteryStorageChanged) #getter
    def batteryStorage(self) -> BatteryStorage:
        return self.battery_storage

    @Property(ChargingAndDemand, notify=chargingAndDemandChanged) #getter
    def chargingAndDemand(self) -> ChargingAndDemand:
        return self.charging_and_demand

    @Property(HourlyBreakdown, notify=hourBreakdownChanged) #getter
    def hourlyBreakdown(self) -> HourlyBreakdown:
        return self.hourly_breakdown

    @Slot()
    def updateBatteryStorageChargeRate(self):
        if (
            new_value := \
                self.charging_and_demand.charging_ports.dc_charger_1_rating / self.battery_storage.ess_system.installed_capacity_kwh \
            if self.battery_storage.ess_system.installed_capacity_kwh else 0
        ):
            self.battery_storage.ess_system.charge_rate_cRate = new_value
            self.battery_storage.ess_system.chargeRateChanged.emit()

    @Slot()
    def updateBatteryStorageMaximumPower(self):
        if (
            new_value := min(
                self.charging_and_demand.charging_ports.dc_charger_1_rating,
                self.charging_and_demand.ev_characteristics.max_power_rating,
                self.battery_storage.discharge_.power_max
            )
        ) != self.battery_storage.ess_system.maximum_power_kw:
            self.battery_storage.ess_system.maximum_power_kw = new_value
            self.battery_storage.ess_system.maximumPowerChanged.emit()

    @Slot(int)
    def update_batteryStorage_gridCharging_offPeakElectricityRequiredPerDay(self, index): #can throwaway index
        self.battery_storage.grid_charging.off_peak_electricity_required_kwh_per_day = sum(self.hourly_breakdown.total_charge_supply_section.grid_off_peak)
        self.battery_storage.grid_charging.offPeakElectricityRequiredChanged.emit()

    @Slot(int)
    def update_batteryStorage_gridCharging_peakElectricityRequiredPerDay(self, index): #can throwaway index
        self.battery_storage.grid_charging.peak_electricity_charged_from_grid_kwh_per_day = sum(self.hourly_breakdown.total_charge_supply_section.grid_peak)
        self.battery_storage.grid_charging.peakElectricityChargedFromGridChanged.emit()

    @Slot(int)
    def update_chargingAndDemand_demand_totalWaitingTime(self, index): #can throwaway
        self.charging_and_demand.demand_.total_waiting_time = self.hourly_breakdown.status_section.charge_sufficiency[8:22].count(False)
        self.charging_and_demand.demand_.totalWaitingTimeChanged.emit()

    @Slot(int)
    def update_chargingAndDemand_demand_actualUsersServedPerDay(self, index): #can throwaway
        self.charging_and_demand.demand_.actual_users_served_per_day = self.hourly_breakdown.status_section.charge_status.count("discharge")        
        self.charging_and_demand.demand_.actualUsersServedPerDayChanged.emit()


    @Slot(int)
    def update_chargingAndDemand_excessToFacility_electricityPerDay(self, hour_index):     
        self.charging_and_demand.excess_to_facility.electricity_per_day = sum(
            self.solar_power_generation.hourly_solar_power_generation.estimated_kwh_generated
        )
        self.charging_and_demand.excess_to_facility.electricityPerDayChanged.emit()  

    @Slot()
    def updateAll_hourlyBreakdown_totalChargeSupplySection_gridOffPeak(self):
        for hour_index in [0,1,2,3,4,5,6,7,22,23]:
            new_value:float = self.battery_storage.grid_charging.grid_draw_limit_kw
            self.hourly_breakdown.total_charge_supply_section.setGridOffPeakElement(hour_index, new_value)

    @Slot()
    def updateAll_hourlyBreakdown_totalChargeSupplySection_gridPeak(self):
        for hour_index in [8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
            new_value:float = self.battery_storage.grid_charging.grid_draw_limit_kw
            self.hourly_breakdown.total_charge_supply_section.setGridPeakElement(hour_index, new_value)

    @Slot()
    def updateAll_hourlyBreakdown_dcChargerDemandSection_essStateOfChargeElement(self):
        for i in range(24):
            self.update_hourlyBreakdown_dcChargerDemandSection_essStateOfChargeElement(hour_index=i)
        
    @Slot(int)
    def update_hourlyBreakdown_dcChargerDemandSection_essStateOfChargeElement(self, hour_index:int):
        new_value:float =\
            self.hourly_breakdown.dc_charger_demand_section.ess_charge[hour_index] / self.battery_storage.ess_system.installed_capacity_kwh \
        if self.battery_storage.ess_system.installed_capacity_kwh else 0

        self.hourly_breakdown.dc_charger_demand_section.setEssStateOfChargeElement(hour_index, new_value)


    @Slot()
    def updateAll_hourlyBreakdown_statusSection_reachedEssStateOfChargeElement(self):
        for i in range(24):
            self.update_hourlyBreakdown_statusSection_reachedEssStateOfChargeElement(hour_index=i)

    @Slot(int)
    def update_hourlyBreakdown_statusSection_reachedEssStateOfChargeElement(self, hour_index:int):
        if hour_index != 0:
            charger_needed: bool = self.hourly_breakdown.status_section.charger_needed[hour_index]
            ess_charge: float = self.hourly_breakdown.dc_charger_demand_section.ess_charge[hour_index-1]
            total_charge_supply: float = self.hourly_breakdown.total_charge_supply_section.total_charge_supply[hour_index]
            dc_charger_demand: float = self.hourly_breakdown.dc_charger_demand_section.dc_charger_demand[hour_index]

            installed_capacity: float = self.battery_storage.ess_system.installed_capacity_kwh
            soc_upper_limit: float = self.battery_storage.ess_system.state_of_charge_upper_limit_percentage
            soc_lower_limit: float = self.battery_storage.ess_system.state_of_charge_lower_limit_percentage

            if charger_needed:
                new_value:float = ess_charge-(dc_charger_demand-total_charge_supply) < (soc_lower_limit * installed_capacity)
                self.hourly_breakdown.status_section.setReachedEssStateOfChargeElement(hour_index, new_value)                
            else:
                new_value:float = (ess_charge+total_charge_supply) > (soc_upper_limit*installed_capacity)
                self.hourly_breakdown.status_section.setReachedEssStateOfChargeElement(hour_index, new_value)


    '''=============== CHARGING STRATEGY ================='''
    def _update_dcChargerDemandSection_essChargeWithLoad_firstHour(self):
        new_value = self.hourly_breakdown.total_charge_supply_section.total_charge_supply[0] - self.hourly_breakdown.dc_charger_demand_section.dc_charger_demand[0]

        self.hourly_breakdown.dc_charger_demand_section.setEssChargeElement(0, new_value)
       


    def _update_hourlyBreakdown_dcChargerDemandSection_essChargeWithLoad_nonFirstHour(self, hour_index: int):
        total_charge_supply:float = self.hourly_breakdown.total_charge_supply_section.total_charge_supply[hour_index]
        previous_hour_value:float = self.hourly_breakdown.dc_charger_demand_section.ess_charge[hour_index-1]

        new_value:float = previous_hour_value

        if self.hourly_breakdown.dc_charger_demand_section.load_on_ess[hour_index] > 0:
            if self.hourly_breakdown.status_section.charge_sufficiency[hour_index]:
                if self.hourly_breakdown.status_section.reached_ess_state_of_charge[hour_index]:
                    new_value = previous_hour_value + total_charge_supply
                elif self.battery_storage.ess_system.charging_strategy == 1:
                    new_value = previous_hour_value - self.hourly_breakdown.dc_charger_demand_section.load_on_ess[hour_index]
                elif self.battery_storage.ess_system.charging_strategy == 2:
                    new_value = previous_hour_value \
                        - (
                            self.hourly_breakdown.total_charge_supply_section.total_charge_supply[hour_index]
                            - self.hourly_breakdown.dc_charger_demand_section.load_on_ess[hour_index]    
                        )

            else:
                new_value = previous_hour_value + total_charge_supply

        elif self.hourly_breakdown.status_section.reached_ess_state_of_charge[hour_index]:
            new_value = previous_hour_value
        else:
            new_value = previous_hour_value + total_charge_supply
           
        self.hourly_breakdown.dc_charger_demand_section.setEssChargeElement(hour_index, new_value)          

    @Slot(int)
    def update_hourlyBreakdown_dcChargerDemandSection_essChargeWithLoad(self, _: int):
        self._update_dcChargerDemandSection_essChargeWithLoad_firstHour()
        for hour_index in range(23):
            self._update_hourlyBreakdown_dcChargerDemandSection_essChargeWithLoad_nonFirstHour(hour_index+1)        

    @Slot()
    def update_hourlyBreakdown_dcChargerDemandSection_essChargeWithLoad_(self):
        self._update_dcChargerDemandSection_essChargeWithLoad_firstHour()
        for hour_index in range(23):
            self._update_hourlyBreakdown_dcChargerDemandSection_essChargeWithLoad_nonFirstHour(hour_index+1)                       
'''============================================================'''



