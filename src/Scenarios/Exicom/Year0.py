import sys
import os

pwd = os.getcwd()
if pwd not in sys.path:
    sys.path.append(pwd)

from Scenario.Year.Year import Year
''' ***********************************
            Technical 
*************************************'''
from Scenario.Year.Technical.Technical import Technical

'''Battery Storage'''
from Scenario.Year.Technical.BatteryStorage.BatteryStorage import BatteryStorage
from Scenario.Year.Technical.BatteryStorage.Discharge import Discharge
from Scenario.Year.Technical.BatteryStorage.EssSystem import EssSystem
from Scenario.Year.Technical.BatteryStorage.GridCharging import GridCharging

'''ChargingAndDemand'''
from Scenario.Year.Technical.ChargingAndDemand.ChargingAndDemand import ChargingAndDemand
from Scenario.Year.Technical.ChargingAndDemand.ChargingPorts import ChargingPorts
from Scenario.Year.Technical.ChargingAndDemand.Demand import Demand
from Scenario.Year.Technical.ChargingAndDemand.EvCharacteristics import EvCharacteristics
from Scenario.Year.Technical.ChargingAndDemand.ExcessToFacility import ExcessToFacility
from Scenario.Year.Technical.ChargingAndDemand.Load import Load

'''HourlyBreakdown'''
from Scenario.Year.Technical.HourlyBreakdown.HourlyBreakdown import HourlyBreakdown
from Scenario.Year.Technical.HourlyBreakdown.DcChargerDemandSection import DcChargerDemandSection
from Scenario.Year.Technical.HourlyBreakdown.StatusSection import StatusSection
from Scenario.Year.Technical.HourlyBreakdown.TotalChargeSupplySection import TotalChargeSupplySection

'''Solar Power Generation'''
from Scenario.Year.Technical.SolarPowerGeneration.SolarPowerGeneration import SolarPowerGeneration
from Scenario.Year.Technical.SolarPowerGeneration.AyerKerohSiteConditions import AyerKerohSiteConditions
from Scenario.Year.Technical.SolarPowerGeneration.InstalledCapacity import InstalledCapacity
from Scenario.Year.Technical.SolarPowerGeneration.SolarEnergyProduction import SolarEnergyProduction
from Scenario.Year.Technical.SolarPowerGeneration.HourlySolarPowerGeneration import HourlySolarPowerGeneration

''' ***********************************
            Financial 
*************************************'''
from Scenario.Year.Financial.Financial import Financial

'''Capital Expenditure'''
from Scenario.Year.Financial.CapitalExpenditure.CapitalExpenditure import CapitalExpenditure
from Scenario.Year.Financial.CapitalExpenditure.CapitalExpenditureItems import CapitalExpenditureItems
from Scenario.Year.Financial.CapitalExpenditure.Depreciation import Depreciation as DepreciationFinancial
from Scenario.Year.Financial.CapitalExpenditure.ExchangeRate import ExchangeRate

'''OperatingExpenditure'''
from Scenario.Year.Financial.OperatingExpenditure.OperatingExpenditure import OperatingExpenditure
from Scenario.Year.Financial.OperatingExpenditure.FixedOAndM import FixedOAndM
from Scenario.Year.Financial.OperatingExpenditure.OperatingExpenditureItems import OperatingExpenditureItems

'''Revenue'''
from Scenario.Year.Financial.Revenue.Revenue import Revenue as RevenueFinancial
from Scenario.Year.Financial.Revenue.RevenueItems import RevenueItems
from Scenario.Year.Financial.Revenue.Pricing import Pricing
from Scenario.Year.Financial.Revenue.TariffAssumption import TariffAssumption

'''Summary'''
from Scenario.Year.Financial.Summary.Summary import Summary
# Discounted Cash Flow Section
from Scenario.Year.Financial.Summary.DiscountedCashFlowsSection.DiscountedCashFlowsSection import DiscountedCashFlowsSection
# EBITDA Section
from Scenario.Year.Financial.Summary.EbitdaSection.EbitdaSection import EbitdaSection
from Scenario.Year.Financial.Summary.EbitdaSection.Revenue.Revenue import Revenue as RevenueFinancialSummary
# EBIT Section
from Scenario.Year.Financial.Summary.EbitSection.EbitSection import EbitSection
from Scenario.Year.Financial.Summary.EbitSection.Depreciation.Depreciation import Depreciation as DepreciationFinancialSummary
# Free Cash Flow Section
from Scenario.Year.Financial.Summary.FreeCashFlowSection.FreeCashFlowSection import FreeCashFlowSection
# Net Income Section
from Scenario.Year.Financial.Summary.NetIncomeSection.NetIncomeSection import NetIncomeSection


year0 = Year(

    technical=Technical(
        battery_storage=BatteryStorage(
            ess_system=EssSystem(
                installed_capacity = 0,
                operational_time_percentage = 0,
                state_of_charge_upper_limit = 0,
                state_of_charge_lower_limit = 0,
                end_of_life_capacity_percentage = 0,
                ess_nameplate_lifecycle = 0
            ),
            discharge=Discharge(),
            grid_charging=GridCharging(grid_draw_limit_kw = 0)
        ),
        solar_power_generation=SolarPowerGeneration(
            installed_capacity = InstalledCapacity(installed_capacity=0),
            ayer_keroh_site_conditions = AyerKerohSiteConditions(specific_pv_power_output_per_day=0),
            solar_energy_production = SolarEnergyProduction(boost_inverter_efficiency=0),
            hourly_solar_power_generation = HourlySolarPowerGeneration(
                percentage_of_max_kw=[0, 0, 0, 0, 0, 0, 0.05, 0.26, 0.54, 0.76, 0.91, 1, 0.98, 0.9, 0.75, 0.53, 0.3, 0.09, 0, 0, 0, 0, 0, 0]
            )
        ),

        charging_and_demand=ChargingAndDemand(
            charging_ports = ChargingPorts(
                dc_charger_1_rating = 0,
                num_of_dc_charger1 = 0,

                dc_charger_2_rating = 0, 
                num_of_dc_charger2 = 0
            ),
            demand = Demand(
                state_of_charge_at_entry = 0,
                state_of_charge_limit = 0,

                number_of_users_per_day = 0
            ),
            load = Load(),
            excess_to_facility = ExcessToFacility(),
            ev_characteristics = EvCharacteristics(
                ev_battery_voltage = 0,
                capacity = 0,
                max_power_rating = 0
            )
        ),
        hourly_breakdown=HourlyBreakdown()        
    ),



    financial = Financial(
        capital_expenditure = CapitalExpenditure(
            capital_expenditure_items = CapitalExpenditureItems(
                solar_pv_rectification = 89_460,
                dc_chargers = 344_443,
                pcs_200kw = 816_235,
                ess_301kwh = 30_000,
            ),
            depreciation = DepreciationFinancial(
                actual_ess_lifecycle = 0,
                ess_capex_per_kwh = 0,
                charger_lifecycle_capacity = 0,
                charger_capex_per_kw = 0,
                charger_depreciation = 0
            ),
            exchange_rate = ExchangeRate(rm_per_usd=4.18)
        ),
        operating_expenditure = OperatingExpenditure(
            operating_expenditure_items = OperatingExpenditureItems(
                solar_pv_o_and_m = 0,
                dc_chargers_o_and_m = 0,
                ess_o_and_m = 0,
                grid_electricity = 0
            ),
            fixed_o_and_m = FixedOAndM(
                solar_pv_o_and_m = 0,
                ev_charger_o_and_m = 0,
                lfp_o_and_m = 0
            )
        ),
        revenue = RevenueFinancial(
            revenue_items = RevenueItems(
                chargers=0,
                retail_to_facility = 0,
                total_revenue = 0
            ),
            pricing = Pricing(
                price_to_ev_chargers = 0
            ),
            tariff_assumption = TariffAssumption(
                electricity_tariff_rate = 0.53,
                margin_on_electricity_sold_to_facility = 0.8,
                peak_tariff_rate = 0.58,
                off_peak_tariff_rate = 0.28
            )
        ),
        summary = Summary(
            ebitda_section = EbitdaSection(
                revenue = RevenueFinancialSummary(
                    chargers = 0,
                    retail_to_facility = 0,
                    total = 0
                ),
                ebitda = 0,
                opex = 0
            ),
            ebit_section = EbitSection(
                depreciation=DepreciationFinancialSummary(
                    chargers = 0,
                    ess = 0,
                    total = 0
                ),
                ebit=0
            ),
            net_income_section = NetIncomeSection(
                tax_expense=0,
                net_income=0
            ),
            free_cash_flow_section = FreeCashFlowSection(
                operating_cash_flow = 0,
                capex = 1_280_138,
                change_in_net_working_capital = 0,
                free_cash_flow = -1_280_138
            ),
            discounted_cash_flow_section = DiscountedCashFlowsSection(
                cumulative_cash_flow = -1_280_138,
                present_value_of_cash_flow = -1_280_138,
                weighted_average_cost_of_capital = 0
            )   
        )
    )
)