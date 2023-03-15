from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from typing import Optional

from .Technical.Technical import Technical
from .Financial.Financial import Financial

class Year(QObject):
    # chargingAndDemandChanged = Signal()
    # solarPowerGenerationChanged = Signal()
    technicalChanged = Signal()
    financialChanged = Signal()

    def __init__(self, 
        name: str = None,
        technical: Optional[Technical] = None,
        financial: Optional[Financial] = None
    ):
        super().__init__()
        self.technical_: Technical = Technical() if technical is None else technical
        self.financial_: Financial = Financial() if financial is None else financial

        '''****************************************
                POST ASSIGNMENT UPDATE
        ****************************************'''

        '''======= financial ======='''
        '''------- operating expenditure -------'''         
        self.financial_.operating_expenditure.operating_expenditure_items.solar_pv_o_and_m = \
                            self.financial_.operating_expenditure.fixed_o_and_m.solar_pv_o_and_m \
                                * self.financial_.capital_expenditure.exchange_rate.rm_per_usd \
                                * self.technical_.solar_power_generation.installed_capacity.installed_capacity


        self.financial_.operating_expenditure.operating_expenditure_items.ess_o_and_m = \
                            self.financial_.operating_expenditure.fixed_o_and_m.lfp_o_and_m \
                                * self.financial_.capital_expenditure.exchange_rate.rm_per_usd \
                                * self.technical_.battery_storage.discharge_.power_max

        self.financial_.operating_expenditure.operating_expenditure_items.grid_electricity = (
                                (
                                    self.financial_.revenue_.tariff_assumption.peak_tariff_rate \
                                    * self.technical_.battery_storage.grid_charging.peak_electricity_charged_from_grid_kwh_per_day
                                ) + (
                                    self.technical_.battery_storage.grid_charging.off_peak_electricity_required_kwh_per_day \
                                    * self.financial_.revenue_.tariff_assumption.off_peak_tariff_rate
                                )
                            ) * 365 * 0.9

        '''------- revenue -------'''
        # chargers
        self.financial_.revenue_.revenue_items.chargers_= \
            self.financial_.revenue_.pricing_.price_to_ev_chargers \
            * self.technical_.charging_and_demand.demand_.actual_energy_served_per_day * 365 \
            * self.technical_.battery_storage.ess_system.operational_time_percentage
        
        # retail to facility
        self.financial_.revenue_.revenue_items.retail_to_facility = \
            self.financial_.revenue_.tariff_assumption.margin_on_electricity_sold_to_facility \
            * self.financial_.revenue_.tariff_assumption.electricity_tariff_rate \
            * self.technical_.charging_and_demand.excess_to_facility.electricity_per_year \
            * self.technical_.battery_storage.ess_system.operational_time_percentage

        '''------- summary -------'''
        self.financial_.summary_.ebitda_section.revenue_.chargers_ = \
            self.financial_.revenue_.pricing_.price_to_ev_chargers \
            * self.technical_.charging_and_demand.demand_.actual_energy_served_per_day * 365 \
            * self.technical_.battery_storage.ess_system.operational_time_percentage


        self.financial_.summary_.ebitda_section.revenue_.retail_to_facility = \
            self.financial_.revenue_.tariff_assumption.margin_on_electricity_sold_to_facility \
            * self.financial_.revenue_.tariff_assumption.electricity_tariff_rate \
            * self.technical_.charging_and_demand.excess_to_facility.electricity_per_year \
            * self.technical_.battery_storage.ess_system.operational_time_percentage
        

        self.financial_.summary_.ebit_section.depreciation_.chargers_ = \
            self.financial_.capital_expenditure.depreciation_.charger_depreciation \
            * self.technical_.charging_and_demand.demand_.actual_energy_served_per_day \
            * 365 * 0.9


        self.financial_.summary_.ebit_section.depreciation_.ess_ = \
            self.financial_.capital_expenditure.depreciation_.ess_depreciation \
            * self.technical_.charging_and_demand.demand_.actual_energy_served_per_day \
            * 365 * 0.9

        '''****************************************
                    CONNECTIONS
        ****************************************'''

        '''======= technical =======''' 

        '''------- summary -------'''
        self.technical_.charging_and_demand.demand_.usersPerHourElementChanged.connect(self.update_technical_hourlyBreakdown_dcChargerDemandSection_dcChargerDemand)

        '''======= solar power generation ======='''
        self.technical_.solar_power_generation.solar_energy_production.estimatedGenerationPerDayChanged.connect(self.update_solarPowerGeneration_dailyGeneration)

        '''======= financial ======='''
        '''------- operating expenditure -------'''   
        # solar pv o&m  
        self.financial_.operating_expenditure.fixed_o_and_m.solarPvOAndMChanged.connect(self.update_financial_operatingExpenditure_operatingExpenditureItems_solarPvOAndM)
        self.financial_.capital_expenditure.exchange_rate.rmPerUsdChanged.connect(self.update_financial_operatingExpenditure_operatingExpenditureItems_solarPvOAndM)
        self.technical_.solar_power_generation.installed_capacity.installedCapacityChanged.connect(self.update_financial_operatingExpenditure_operatingExpenditureItems_solarPvOAndM)

        self.financial_.operating_expenditure.fixed_o_and_m.evChargerOAndMChanged.connect(self.update_financial_operatingExpenditure_operatingExpenditureItems_dcChargersOAndM)
        self.financial_.capital_expenditure.exchange_rate.rmPerUsdChanged.connect(self.update_financial_operatingExpenditure_operatingExpenditureItems_dcChargersOAndM)

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
        # chargers    
        self.financial_.revenue_.pricing_.priceToEvChargersChanged.connect(self.update_financial_revenue_revenueItems_chargers)
        self.technical_.battery_storage.ess_system.operationalTimeChanged.connect(self.update_financial_revenue_revenueItems_chargers)

        # retail to facility
        self.financial_.revenue_.tariff_assumption.marginOnElectricitySoldToFacilityChanged.connect(self.update_financial_revenue_revenueItems_retailToFacility )
        self.financial_.revenue_.tariff_assumption.electricityTariffRateChanged.connect(self.update_financial_revenue_revenueItems_retailToFacility )
        self.technical_.charging_and_demand.excess_to_facility.electricityPerYearChanged.connect(self.update_financial_revenue_revenueItems_retailToFacility )
        self.technical_.battery_storage.ess_system.operationalTimeChanged.connect(self.update_financial_revenue_revenueItems_retailToFacility )
        
        '''------- summary -------'''
        self.financial_.revenue_.revenue_items.chargersChanged.connect(self.update_financial_summary_ebitdaSection_revenue_chargers)

        self.financial_.revenue_.revenue_items.retailToFacilityChanged.connect(self.update_financial_summary_ebitdaSection_revenue_retailToFacility)

        self.financial_.revenue_.revenue_items.totalRevenueChanged.connect(self.update_financial_summary_ebitdaSection_revenue_total)

        self.financial_.capital_expenditure.depreciation_.chargerDepreciationChanged.connect(self.update_financial_summary_ebitSection_depreciation_charger)
        self.technical_.charging_and_demand.demand_.actualEnergyServedPerDayChanged.connect(self.update_financial_summary_ebitSection_depreciation_charger)

        self.financial_.capital_expenditure.depreciation_.essDepreciationChanged.connect(self.update_financial_summary_ebitSection_depreciation_ess)
        self.technical_.charging_and_demand.demand_.actualUsersServedPerDayChanged.connect(self.update_financial_summary_ebitSection_depreciation_ess)

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


    # @Slot(int)
    # def update_technical_hourlyBreakdown_totalChargeSupplySection_solarPowerGeneration(self, hour_index:int):
    #     new_value:float = self.technical_.solar_power_generation.hourly_solar_power_generation.estimated_kwh_generated[hour_index]
    #     self.technical_.hourly_breakdown.total_charge_supply_section.setSolarPowerGenerationElement(hour_index, new_value)


    @Slot(int)
    def update_technical_hourlyBreakdown_dcChargerDemandSection_dcChargerDemand(self, hour_index:int):
        new_value = self.technical_.charging_and_demand.load_.required_energy_per_user if self.technical_.charging_and_demand.demand_.users_per_hour[hour_index] > 0 else 0
        self.technical_.hourly_breakdown.dc_charger_demand_section.setDcChargerDemandElement(hour_index, new_value)

    '''======= solar power generation ======='''
    @Slot()
    def update_solarPowerGeneration_dailyGeneration(self):
        if (
            new_value := self.technical_.solar_power_generation.solar_energy_production.estimated_generation_per_day
        ) != self.technical_.solar_power_generation.hourly_solar_power_generation.daily_generation:
            self.technical_.solar_power_generation.hourly_solar_power_generation.daily_generation = new_value
            self.technical_.solar_power_generation.hourly_solar_power_generation.dailyGenerationChanged.emit()

    '''======= financial ======='''

    '''------- operating expenditure -------'''         
    @Slot()
    def update_financial_operatingExpenditure_operatingExpenditureItems_solarPvOAndM(self):
        if (
            new_value := \
                self.financial_.operating_expenditure.fixed_o_and_m.solar_pv_o_and_m \
                * self.financial_.capital_expenditure.exchange_rate.rm_per_usd \
                * self.technical_.solar_power_generation.installed_capacity.installed_capacity
        ):
            self.financial_.operating_expenditure.operating_expenditure_items.solar_pv_o_and_m = new_value
            self.financial_.operating_expenditure.operating_expenditure_items.solarPvOAndMChanged.emit()

    @Slot()
    def update_financial_operatingExpenditure_operatingExpenditureItems_dcChargersOAndM(self):
        if (
            new_value := \
                self.financial_.operating_expenditure.fixed_o_and_m.ev_charger_o_and_m \
                * self.financial_.capital_expenditure.exchange_rate.rm_per_usd * 2
        ):
            self.financial_.operating_expenditure.operating_expenditure_items.dc_chargers_o_and_m = new_value
            self.financial_.operating_expenditure.operating_expenditure_items.dcChargesOAndMChanged.emit()

    @Slot()
    def update_financial_operatingExpenditure_operatingExpenditureItems_essOAndM(self):
        if (
            new_value := \
                self.financial_.operating_expenditure.fixed_o_and_m.lfp_o_and_m \
                * self.financial_.capital_expenditure.exchange_rate.rm_per_usd \
                * self.technical_.battery_storage.discharge_.power_max
        ) != self.financial_.operating_expenditure.operating_expenditure_items.ess_o_and_m:
            self.financial_.operating_expenditure.operating_expenditure_items.ess_o_and_m = new_value
            self.financial_.operating_expenditure.operating_expenditure_items.essOAndMChanged.emit()

    @Slot()
    def update_financial_operatingExpenditure_operatingExpenditureItems_gridElectricity(self):  
        if (new_value := (
                (self.financial_.revenue_.tariff_assumption.peak_tariff_rate * self.technical_.battery_storage.grid_charging.peak_electricity_charged_from_grid_kwh_per_day) \
                + (self.technical_.battery_storage.grid_charging.off_peak_electricity_required_kwh_per_day * self.financial_.revenue_.tariff_assumption.off_peak_tariff_rate)
            ) * 365 * 0.9
        ) != self.financial_.operating_expenditure.operating_expenditure_items.grid_electricity:
            self.financial_.operating_expenditure.operating_expenditure_items.grid_electricity = new_value 
            self.financial_.operating_expenditure.operating_expenditure_items.gridElectricityChanged.emit()

    '''------- revenue -------''' 
    @Slot()
    def update_financial_revenue_revenueItems_chargers(self):
        if (
            new_value:= \
                self.financial_.revenue_.pricing_.price_to_ev_chargers \
                * self.technical_.charging_and_demand.demand_.actual_energy_served_per_day * 365 \
                * self.technical_.battery_storage.ess_system.operational_time_percentage
        ) != self.financial_.revenue_.revenue_items.chargers_:
            self.financial_.revenue_.revenue_items.chargers_ = new_value
            self.financial_.revenue_.revenue_items.chargersChanged.emit()


    @Slot()
    def update_financial_revenue_revenueItems_retailToFacility(self):
        if (
            new_value := \
                self.financial_.revenue_.tariff_assumption.margin_on_electricity_sold_to_facility \
                * self.financial_.revenue_.tariff_assumption.electricity_tariff_rate \
                * self.technical_.charging_and_demand.excess_to_facility.electricity_per_year \
                * self.technical_.battery_storage.ess_system.operational_time_percentage
        ) != self.financial_.revenue_.revenue_items.retail_to_facility:
            self.financial_.revenue_.revenue_items.retail_to_facility = new_value
            self.financial_.revenue_.revenue_items.retailToFacilityChanged.emit()    


    '''------- summary -------'''   
    @Slot()
    def update_financial_summary_ebitdaSection_revenue_chargers(self):
        if (
            new_value := self.financial_.revenue_.revenue_items.chargers_
        ) != self.financial_.summary_.ebitda_section.revenue_.chargers_:
            self.financial_.summary_.ebitda_section.revenue_.chargers_ = new_value
            self.financial_.summary_.ebitda_section.revenue_.chargersChanged.emit()

    @Slot()
    def update_financial_summary_ebitdaSection_revenue_retailToFacility(self):
        if (
            new_value := self.financial_.revenue_.revenue_items.retail_to_facility
        ) != self.financial_.summary_.ebitda_section.revenue_.retail_to_facility:
            self.financial_.summary_.ebitda_section.revenue_.retail_to_facility = new_value
            self.financial_.summary_.ebitda_section.revenue_.retailToFacilityChanged.emit()

    @Slot()
    def update_financial_summary_ebitdaSection_revenue_total(self):
        if (
            new_value := self.financial_.revenue_.revenue_items.total_revenue
        ) != self.financial_.summary_.ebitda_section.revenue_.total_:
            self.financial_.summary_.ebitda_section.revenue_.total_ = new_value
            self.financial_.summary_.ebitda_section.revenue_.totalChanged.emit()


    @Slot()
    def update_financial_summary_ebitSection_depreciation_charger(self):
        if (
            new_value := \
                self.financial_.capital_expenditure.depreciation_.charger_depreciation \
                * self.technical_.charging_and_demand.demand_.actual_energy_served_per_day \
                * 365 * 0.9
        ) != self.financial_.summary_.ebit_section.depreciation_.chargers_:
            self.financial_.summary_.ebit_section.depreciation_.chargers_ = new_value
            self.financial_.summary_.ebit_section.depreciation_.chargersChanged.emit()

    @Slot()
    def update_financial_summary_ebitSection_depreciation_ess(self):
        if (
            new_value := \
                self.financial_.capital_expenditure.depreciation_.ess_depreciation \
                * self.technical_.charging_and_demand.demand_.actual_energy_served_per_day \
                * 365 * 0.9
        ) != self.financial_.summary_.ebit_section.depreciation_.ess_:
            self.financial_.summary_.ebit_section.depreciation_.ess_ = new_value
            self.financial_.summary_.ebit_section.depreciation_.chargersChanged.emit()        
