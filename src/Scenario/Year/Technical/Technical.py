from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .SolarPowerGeneration.SolarPowerGeneration import SolarPowerGeneration
from .BatteryStorage.BatteryStorage import BatteryStorage
from .ChargingAndDemand.ChargingAndDemand import ChargingAndDemand
from .HourlyBreakdown.HourlyBreakdown import HourlyBreakdown

from QModels.QTreeNode import QTreeNode

class Technical(QObject):

    treeNodeChanged = Signal()
    
    batteryStorageChanged = Signal()
    chargingAndDemandChanged = Signal()
    solarPowerGenerationChanged = Signal()
    hourBreakdownChanged = Signal()

    tree_node: QTreeNode = QTreeNode("Technical")
    tree_node.add_children([
        QTreeNode("first"),
        QTreeNode("second"),
        QTreeNode("third")
    ])

    # tree:QTreeModel = QTreeModel(root_data="Technical")

    # second_level_nodes:list[QTreeNode] = [QTreeNode("first child"), QTreeNode("second child"), QTreeNode("third child")]
    # tree.root.add_children(second_level_nodes)

    def __init__(self, 
        name: str = None,
        battery_storage = BatteryStorage(),
        solar_power_generation = SolarPowerGeneration(),
        charging_and_demand = ChargingAndDemand(),
        hourly_breakdown = HourlyBreakdown()
    ):
        super().__init__()
        self.battery_storage:BatteryStorage = battery_storage
        self.charging_and_demand:ChargingAndDemand = charging_and_demand
        self.solar_power_generation: SolarPowerGeneration = solar_power_generation
        self.hourly_breakdown:HourlyBreakdown = hourly_breakdown

        self.battery_storage.ess_system.charge_rate_cRate = round(self.charging_and_demand.charging_ports.dc_charger_1_rating /  self.battery_storage.ess_system.installed_capacity_kwh, 2)
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


    def emitUpdateSignals(self):
        self.battery_storage.emitUpdateSignals()
        self.charging_and_demand.emitUpdateSignals()
        self.solar_power_generation.emitUpdateSignals()
        self.hourly_breakdown.emitUpdateSignals()

    @Property(QTreeNode, notify=treeNodeChanged) #getter
    def treeNode(self) -> QTreeNode:
        return self.tree_node

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
        self.battery_storage.ess_system.charge_rate_cRate = round(self.charging_and_demand.charging_ports.dc_charger_1_rating /  self.battery_storage.ess_system.installed_capacity_kwh, 2)
        self.battery_storage.ess_system.chargeRateChanged.emit()

    @Slot()
    def updateBatteryStorageMaximumPower(self):
        self.battery_storage.ess_system.maximum_power_kw = min(
                self.charging_and_demand.charging_ports.dc_charger_1_rating,
                self.charging_and_demand.ev_characteristics.max_power_rating,
                self.battery_storage.discharge_.power_max
            )
        self.battery_storage.ess_system.maximumPowerChanged.emit()
                           
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
        new_value:float = self.hourly_breakdown.dc_charger_demand_section.ess_charge[hour_index] / self.battery_storage.ess_system.installed_capacity_kwh
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

