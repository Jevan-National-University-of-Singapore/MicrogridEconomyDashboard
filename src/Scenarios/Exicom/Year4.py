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


year4 = Year(

    technical=Technical(
        battery_storage=BatteryStorage(
            ess_system=EssSystem(
                installed_capacity = 354,
                operational_time_percentage = 0.9,
                state_of_charge_upper_limit = 0.9,
                state_of_charge_lower_limit = 0.1,
                end_of_life_capacity_percentage = 0.8,
                ess_nameplate_lifecycle = 3059.5088
            ),
            discharge=Discharge(),
            grid_charging=GridCharging(grid_draw_limit_kw = 28.8)
        ),
        solar_power_generation=SolarPowerGeneration(
            installed_capacity = InstalledCapacity(installed_capacity=27),
            ayer_keroh_site_conditions = AyerKerohSiteConditions(specific_pv_power_output_per_day=3.58),
            solar_energy_production = SolarEnergyProduction(boost_inverter_efficiency=0.9),
            hourly_solar_power_generation = HourlySolarPowerGeneration(
                percentage_of_max_kw=[0, 0, 0, 0, 0, 0, 0.05, 0.26, 0.54, 0.76, 0.91, 1, 0.98, 0.9, 0.75, 0.53, 0.3, 0.09, 0, 0, 0, 0, 0, 0]
            )
        ),

        charging_and_demand=ChargingAndDemand(
            charging_ports = ChargingPorts(

                dc_charger_1_rating = 180,
                num_of_dc_charger1 = 1,

                dc_charger_2_rating = 50, 
                num_of_dc_charger2 = 1
            ),
            demand = Demand(
                state_of_charge_at_entry = 0.2,
                state_of_charge_limit = 0.8,

                number_of_users_per_day = 23
            ),
            load = Load(),
            excess_to_facility = ExcessToFacility(),
            ev_characteristics = EvCharacteristics(
                ev_battery_voltage = 800,
                capacity = 54,
                max_power_rating = 270
            )
        ),
        hourly_breakdown=HourlyBreakdown()        
    ),





    financial = Financial(
        capital_expenditure = CapitalExpenditure(
            capital_expenditure_items = CapitalExpenditureItems(
                solar_pv_rectification = 0,
                dc_chargers = 0,
                pcs_200kw = 0,
                ess_301kwh = 0,
            ),
            exchange_rate = ExchangeRate(rm_per_usd=4.18)
        ),
        operating_expenditure = OperatingExpenditure(
            fixed_o_and_m = FixedOAndM(
                solar_pv_o_and_m = 26.5302,
                ev_charger_o_and_m = 424.4832,
                lfp_o_and_m = 4.6693152
            )
        ),
        revenue = RevenueFinancial(
            pricing = Pricing(price_to_ev_chargers = 2),
            tariff_assumption = TariffAssumption(
                electricity_tariff_rate = 0.528,
                margin_on_electricity_sold_to_facility = 0.8,
                peak_tariff_rate = 0.584,
                off_peak_tariff_rate = 0.281
            )
        )
    )
)