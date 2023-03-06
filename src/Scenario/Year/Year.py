from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .Technical.Technical import Technical
from .Financial.Financial import Financial

class Year(QObject):
    chargingAndDemandChanged = Signal()
    solarPowerGenerationChanged = Signal()
    technicalChanged = Signal()
    financialChanged = Signal()

    def __init__(self, 
        name: str = None,
        technical: Technical|None = None,
        financial: Financial|None = None
    ):
        super().__init__()
        self.technical_: Technical = Technical() if technical is None else technical
        self.financial_: Financial = Financial() if financial is None else financial

        '''****************************************
                POST ASSIGNMENT UPDATE
        ****************************************'''

        '''======= financial ======='''
        '''------- capital expenditure -------''' 
        self.financial_.capital_expenditure.depreciation_.actual_ess_lifecycle = round(
                        self.technical_.battery_storage.ess_system.ess_nameplate_lifecycle \
                            * self.technical_.battery_storage.ess_system.depth_of_discharge_percentage \
                            * ( 1 + self.technical_.battery_storage.ess_system.end_of_life_capacity_percentage)/2,
                        2
                    )    

        self.financial_.capital_expenditure.depreciation_.ess_capex_per_kwh = round (
                                    self.financial_.capital_expenditure.capital_expenditure_items.ess_301kwh \
                                        / self.technical_.battery_storage.ess_system.installed_capacity_kwh,
                                    2
                                )

        self.financial_.capital_expenditure.depreciation_.charger_lifecycle_capacity = round(
                                4 * 365 * 10 * 0.9 \
                                    * self.technical_.charging_and_demand.charging_ports.dc_charger_1_rating,
                                2
                            )        
                            
        self.financial_.capital_expenditure.depreciation_.charger_capex_per_kw = round(
                            self.financial_.capital_expenditure.capital_expenditure_items.dc_chargers \
                                /self.technical_.charging_and_demand.charging_ports.dc_charger_1_rating,
                            2
                        ) 

        self.financial_.capital_expenditure.depreciation_.charger_depreciation = round(
                            self.financial_.capital_expenditure.depreciation_.charger_capex_per_kw \
                                * self.technical_.charging_and_demand.charging_ports.dc_charger_1_rating \
                                / self.financial_.capital_expenditure.depreciation_.charger_lifecycle_capacity,
                            2
                        )   

        '''------- operating expenditure -------'''         
        self.financial_.operating_expenditure.operating_expenditure_items.solar_pv_o_and_m = round(
                            self.financial_.operating_expenditure.fixed_o_and_m.solar_pv_o_and_m \
                                * self.financial_.capital_expenditure.exchange_rate.rm_per_usd \
                                * self.technical_.solar_power_generation.installed_capacity.installed_capacity,
                            2
                        )

        self.financial_.operating_expenditure.operating_expenditure_items.ess_o_and_m = round (
                            self.financial_.operating_expenditure.fixed_o_and_m.lfp_o_and_m \
                                * self.financial_.capital_expenditure.exchange_rate.rm_per_usd \
                                * self.technical_.battery_storage.discharge_.power_max,
                            2
                        )

        self.financial_.operating_expenditure.operating_expenditure_items.grid_electricity = round (
                            (
                                (self.financial_.revenue_.tariff_assumption.peak_tariff_rate * self.technical_.battery_storage.grid_charging.peak_electricity_charged_from_grid_kwh_per_day) \
                                + (self.technical_.battery_storage.grid_charging.off_peak_electricity_required_kwh_per_day * self.financial_.revenue_.tariff_assumption.off_peak_tariff_rate)
                            ) * 365 * 0.9,
                            2
                        ) 

        '''------- revenue -------'''
        # retail to facility
        self.financial_.revenue_.five_year_lifetime.retail_to_facility = round (
                        self.technical_.charging_and_demand.excess_to_facility.electricity_per_year
                            * self.financial_.revenue_.tariff_assumption.electricity_tariff_rate \
                            * self.financial_.revenue_.tariff_assumption.margin_on_electricity_sold_to_facility \
                            * 5,
                        2
                    )

        # price to ev chargers
        self.financial_.revenue_.per_annum.breakeven_price_to_ev_chargers = round (
                        self.financial_.revenue_.per_annum.charging_revenue_required \
                            / (
                                self.technical_.battery_storage.ess_system.operational_time_percentage \
                                    * 365 \
                                    * self.technical_.charging_and_demand.demand_.actual_energy_served_per_day
                            ),
                        2
                    )                                                                                                                   


        '''****************************************
                    CONNECTIONS
        ****************************************'''

        '''======= technical =======''' 

        '''------- five year analysis -------'''
        self.technical_.hourly_breakdown.total_charge_supply_section.solarPowerGenerationElementChanged.connect(
            self.update_technical_hourlyBreakdown_totalChargeSupplySection_solarPowerGeneration
        )

        self.technical_.charging_and_demand.demand_.usersPerHourElementChanged.connect(self.update_technical_hourlyBreakdown_dcChargerDemandSection_dcChargerDemand)
             


        '''======= solar power generation ======='''
        self.technical_.solar_power_generation.solar_energy_production.estimatedGenerationPerDayChanged.connect(self.update_solarPowerGeneration_dailyGeneration)

        '''======= financial ======='''
        '''------- capital expenditure -------''' 
        # actual ess lifecycle
        self.technical_.battery_storage.ess_system.essNameplateLifecycleChanged.connect(self.update_financial_capitalExpenditure_depreciation_actualEssLifecycle)
        self.technical_.battery_storage.ess_system.depthOfDischargePercentageChanged.connect(self.update_financial_capitalExpenditure_depreciation_actualEssLifecycle)
        self.technical_.battery_storage.ess_system.endOfLifeCapacityChanged.connect(self.update_financial_capitalExpenditure_depreciation_actualEssLifecycle)
            
        #ess capex            
        self.financial_.capital_expenditure.capital_expenditure_items.ess301Changed.connect(self.update_financial_capitalExpenditure_depreciation_essCapex)
        self.technical_.battery_storage.ess_system.installedCapacityChanged.connect(self.update_financial_capitalExpenditure_depreciation_essCapex)

        #charger lifecycle capacity
        self.technical_.charging_and_demand.charging_ports.dcCharger1RatingChanged.connect(self.update_financial_capitalExpenditure_depreciation_chargerLifecycleCapacity)

        #charger capex
        self.technical_.charging_and_demand.charging_ports.dcCharger1RatingChanged.connect(self.update_financial_capitalExpenditure_depreciation_chargerCapex)
        self.financial_.capital_expenditure.capital_expenditure_items.dcChargersChanged.connect(self.update_financial_capitalExpenditure_depreciation_chargerCapex)

        #charger depreciation
        self.financial_.capital_expenditure.depreciation_.chargerCapexPerKwChanged.connect(self.update_financial_capitalExpenditure_depreciation_chargerDepreciation)
        self.technical_.charging_and_demand.charging_ports.dcCharger1RatingChanged.connect(self.update_financial_capitalExpenditure_depreciation_chargerDepreciation)
        self.financial_.capital_expenditure.depreciation_.chargerLifecycleCapacityChanged.connect(self.update_financial_capitalExpenditure_depreciation_chargerDepreciation)

        '''------- operating expenditure -------'''   
        # solar pv o&m  
        self.financial_.operating_expenditure.fixed_o_and_m.solarPvOAndMChanged.connect(self.update_financial_operatingExpenditure_operatingExpenditureItems_solarPvOAndM)
        self.financial_.capital_expenditure.exchange_rate.rmPerUsdChanged.connect(self.update_financial_operatingExpenditure_operatingExpenditureItems_solarPvOAndM)
        self.technical_.solar_power_generation.installed_capacity.installedCapacityChanged.connect(self.update_financial_operatingExpenditure_operatingExpenditureItems_solarPvOAndM)

        # ess O&M
        self.financial_.operating_expenditure.fixed_o_and_m.lfpAndMChanged.connect(self.update_financial_operatingExpenditure_operatingExpenditureItems_essOAndM)
        self.financial_.capital_expenditure.exchange_rate.rmPerUsdChanged.connect(self.update_financial_operatingExpenditure_operatingExpenditureItems_essOAndM)
        self.technical_.battery_storage.discharge_.powerMaxChanged.connect(self.update_financial_operatingExpenditure_operatingExpenditureItems_essOAndM)

        # grid electricity
        self.financial_.revenue_.tariff_assumption.peakTariffRateChanged.connect(self.update_financial_operatingExpenditure_operatingExpenditureItems_gridElectricity)
        self.technical_.battery_storage.grid_charging.peakElectricityChargedFromGridChanged.connect(self.update_financial_operatingExpenditure_operatingExpenditureItems_gridElectricity)
        self.technical_.battery_storage.grid_charging.offPeakElectricityRequiredChanged.connect(self.update_financial_operatingExpenditure_operatingExpenditureItems_gridElectricity)
        self.financial_.revenue_.tariff_assumption.offPeakTariffRateChanged.connect(self.update_financial_operatingExpenditure_operatingExpenditureItems_gridElectricity)

        '''------- revenue -------'''
        # retail to facility
        self.technical_.charging_and_demand.excess_to_facility.electricityPerYearChanged.connect(self.update_financial_revenue_fiveYearLifetime_retailToFacility)
        self.financial_.revenue_.tariff_assumption.electricityTariffRateChanged.connect(self.update_financial_revenue_fiveYearLifetime_retailToFacility)
        self.financial_.revenue_.tariff_assumption.marginOnElectricitySoldToFacilityChanged.connect(self.update_financial_revenue_fiveYearLifetime_retailToFacility)

        # price to ev chargers
        self.financial_.revenue_.per_annum.chargingRevenueRequiredChanged.connect(self.update_financial_revenue_perAnnum_priceToEvChargers)
        self.technical_.battery_storage.ess_system.operationalTimeChanged.connect(self.update_financial_revenue_perAnnum_priceToEvChargers)
        self.technical_.charging_and_demand.demand_.actualEnergyServedPerDayChanged.connect(self.update_financial_revenue_perAnnum_priceToEvChargers)

        self.emitUpdateSignals()

    def emitUpdateSignals(self):
        self.technical_.emitUpdateSignals()
        self.financial_.emitUpdateSignals()


    @Property(Technical, notify=technicalChanged) #getter
    def technical(self) -> Technical:
        return self.technical_

    @technical.setter
    def technical(self, technical:Technical):
        self.technical_ = technical

    @Property(Financial, notify=financialChanged) #getter
    def financial(self) -> Financial:
        return self.financial_

    @financial.setter
    def financial(self, financial:Financial):
        self.financial_ = financial

    '''****************************************
                    SLOTS
    ****************************************'''

    '''======= technical ======='''      


    @Slot(int)
    def update_technical_hourlyBreakdown_totalChargeSupplySection_solarPowerGeneration(self, hour_index:int):
        new_value:float = self.technical_.solar_power_generation.hourly_solar_power_generation.estimated_kwh_generated[hour_index]
        self.technical_.hourly_breakdown.total_charge_supply_section.setSolarPowerGenerationElement(hour_index, new_value)


    @Slot(int)
    def update_technical_hourlyBreakdown_dcChargerDemandSection_dcChargerDemand(self, hour_index:int):
        new_value = self.technical_.charging_and_demand.load_.required_energy_per_user if self.technical_.charging_and_demand.demand_.users_per_hour[hour_index] > 0 else 0
        self.technical_.hourly_breakdown.dc_charger_demand_section.setDcChargerDemandElement(hour_index, new_value)

    '''======= solar power generation ======='''
    @Slot()
    def update_solarPowerGeneration_dailyGeneration(self):
        self.technical_.solar_power_generation.hourly_solar_power_generation.daily_generation = self.technical_.solar_power_generation.solar_energy_production.estimated_generation_per_day
        self.technical_.solar_power_generation.hourly_solar_power_generation.dailyGenerationChanged.emit()

    '''======= financial ======='''
    '''------- capital expenditure -------''' 
    @Slot()
    def update_financial_capitalExpenditure_depreciation_actualEssLifecycle(self):
        self.financial_.capital_expenditure.depreciation_.actual_ess_lifecycle = round(
                            self.technical_.battery_storage.ess_system.ess_nameplate_lifecycle \
                                * self.technical_.battery_storage.ess_system.depth_of_discharge_percentage \
                                * ( 1 + self.technical_.battery_storage.ess_system.end_of_life_capacity_percentage)/2,
                            2
                        )    
        self.financial_.capital_expenditure.depreciation_.actualEssLifecycleChanged.emit()

          
    @Slot()
    def update_financial_capitalExpenditure_depreciation_essCapex(self):
        self.financial_.capital_expenditure.depreciation_.ess_capex_per_kwh = round (
                                    self.financial_.capital_expenditure.capital_expenditure_items.ess_301kwh \
                                        / self.technical_.battery_storage.ess_system.installed_capacity_kwh,
                                    2
                                )

        self.financial_.capital_expenditure.depreciation_.essCapexPerKwhChanged.emit()


    @Slot()
    def update_financial_capitalExpenditure_depreciation_chargerLifecycleCapacity(self):    
        self.financial_.capital_expenditure.depreciation_.charger_lifecycle_capacity = round(
                                4 * 365 * 10 * 0.9 \
                                    * self.technical_.charging_and_demand.charging_ports.dc_charger_1_rating,
                                2
                            )
        
        self.financial_.capital_expenditure.depreciation_.chargerLifecycleCapacityChanged.emit()

            

    @Slot()
    def update_financial_capitalExpenditure_depreciation_chargerCapex(self):
        self.financial_.capital_expenditure.depreciation_.charger_capex_per_kw = round(
                            self.financial_.capital_expenditure.capital_expenditure_items.dc_chargers \
                                /self.technical_.charging_and_demand.charging_ports.dc_charger_1_rating,
                            2
                        )

        self.financial_.capital_expenditure.depreciation_.chargerCapexPerKwChanged.emit()

            

    @Slot()
    def update_financial_capitalExpenditure_depreciation_chargerDepreciation(self):    
        self.financial_.capital_expenditure.depreciation_.charger_depreciation = round(
                            self.financial_.capital_expenditure.depreciation_.charger_capex_per_kw \
                                * self.technical_.charging_and_demand.charging_ports.dc_charger_1_rating \
                                / self.financial_.capital_expenditure.depreciation_.charger_lifecycle_capacity,
                            2
                        )

        self.financial_.capital_expenditure.depreciation_.chargerDepreciationChanged.emit()

    '''------- operating expenditure -------'''         
    @Slot()
    def update_financial_operatingExpenditure_operatingExpenditureItems_solarPvOAndM(self):
        self.financial_.operating_expenditure.operating_expenditure_items.solar_pv_o_and_m = round(
            self.financial_.operating_expenditure.fixed_o_and_m.solar_pv_o_and_m \
                * self.financial_.capital_expenditure.exchange_rate.rm_per_usd \
                * self.technical_.solar_power_generation.installed_capacity.installed_capacity,
            2
        )
        self.financial_.operating_expenditure.operating_expenditure_items.solarPvOAndMChanged.emit()
    @Slot()
    def update_financial_operatingExpenditure_operatingExpenditureItems_essOAndM(self):
        self.financial_.operating_expenditure.operating_expenditure_items.ess_o_and_m = round (
            self.financial_.operating_expenditure.fixed_o_and_m.lfp_o_and_m \
                * self.financial_.capital_expenditure.exchange_rate.rm_per_usd \
                * self.technical_.battery_storage.discharge_.power_max,
            2
        )
        self.financial_.operating_expenditure.operating_expenditure_items.essOAndMChanged.emit()

    @Slot()
    def update_financial_operatingExpenditure_operatingExpenditureItems_gridElectricity(self):  
        self.financial_.operating_expenditure.operating_expenditure_items.grid_electricity = round (
            (
                (self.financial_.revenue_.tariff_assumption.peak_tariff_rate * self.technical_.battery_storage.grid_charging.peak_electricity_charged_from_grid_kwh_per_day) \
                + (self.technical_.battery_storage.grid_charging.off_peak_electricity_required_kwh_per_day * self.financial_.revenue_.tariff_assumption.off_peak_tariff_rate)
            ) * 365 * 0.9,
            2
        )
        self.financial_.operating_expenditure.operating_expenditure_items.gridElectricityChanged.emit()

    '''------- revenue -------''' 
    @Slot()
    def update_financial_revenue_fiveYearLifetime_retailToFacility(self):
        self.financial_.revenue_.five_year_lifetime.retail_to_facility = round (
            self.technical_.charging_and_demand.excess_to_facility.electricity_per_year
                * self.financial_.revenue_.tariff_assumption.electricity_tariff_rate \
                * self.financial_.revenue_.tariff_assumption.margin_on_electricity_sold_to_facility \
                * 5,
            2
        )
        self.financial_.revenue_.five_year_lifetime.retailToFacilityChanged.emit()

    @Slot()
    def update_financial_revenue_perAnnum_priceToEvChargers(self):
        self.financial_.revenue_.per_annum.breakeven_price_to_ev_chargers = round (
            self.financial_.revenue_.per_annum.charging_revenue_required \
                / (
                    self.technical_.battery_storage.ess_system.operational_time_percentage \
                        * 365 \
                        * self.technical_.charging_and_demand.demand_.actual_energy_served_per_day
                ),
            2
        )
        self.financial_.revenue_.per_annum.breakevenPriceToEvChargersChanged.emit()
                