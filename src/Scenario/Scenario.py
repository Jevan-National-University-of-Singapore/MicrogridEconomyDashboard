from typing import Optional

import numpy_financial as npf

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .Year.Year import Year
from .FiveYearAnalysis.FiveYearAnalysis import FiveYearAnalysis

class Scenario(QObject):
    yearsChanged = Signal()
    currentYearIndexChanged = Signal()
    fiveYearAnalysisChanged = Signal()

    def __init__(self, 
        name: str = None,
        years: Optional[list[Year]] = None,
        five_year_analysis: Optional[FiveYearAnalysis] = None,
    ):
        super().__init__()
        self.current_year_index:int = 0
        
        self.years_: list[Year] = [Year(), Year(), Year(), Year(), Year(), Year()] if years is None else years
        self.five_year_analysis: FiveYearAnalysis = FiveYearAnalysis() if five_year_analysis is None else five_year_analysis

        '''****************************************
                POST ASSIGNMENT UPDATE
        ****************************************'''

        self.years_[0].financial_.capital_expenditure.depreciation_.ess_depreciation = \
            self.years_[0].financial_.capital_expenditure.depreciation_.ess_capex_per_kwh \
            + self.years_[0].financial_.capital_expenditure.depreciation_.actual_ess_lifecycle
        

        '''------- capital expenditure -------''' 
        self.years_[0].financial_.capital_expenditure.depreciation_.actual_ess_lifecycle = \
            self.years_[0].technical_.battery_storage.ess_system.ess_nameplate_lifecycle \
            * self.years_[0].technical_.battery_storage.ess_system.depth_of_discharge_percentage \
            * ( 1 + self.years_[0].technical_.battery_storage.ess_system.end_of_life_capacity_percentage)/2

        self.years_[0].financial_.capital_expenditure.depreciation_.ess_capex_per_kwh = \
            self.years_[0].financial_.capital_expenditure.capital_expenditure_items.ess_301kwh \
            / self.years_[0].technical_.battery_storage.ess_system.installed_capacity_kwh \
        if self.years_[0].technical_.battery_storage.ess_system.installed_capacity_kwh else 0
        

        self.years_[0].financial_.capital_expenditure.depreciation_.charger_lifecycle_capacity = \
            4 * 365 * 10 * 0.9 \
            * self.years_[0].technical_.charging_and_demand.charging_ports.dc_charger_1_rating \
        if self.years_[0].technical_.charging_and_demand.charging_ports.dc_charger_1_rating else 0

        self.years_[0].financial_.capital_expenditure.depreciation_.charger_capex_per_kw = \
            self.years_[0].financial_.capital_expenditure.capital_expenditure_items.dc_chargers \
            /self.years_[0].technical_.charging_and_demand.charging_ports.dc_charger_1_rating \
        if self.years_[0].technical_.charging_and_demand.charging_ports.dc_charger_1_rating else 0

        self.years_[0].financial_.capital_expenditure.depreciation_.charger_depreciation = \
            self.years_[0].financial_.capital_expenditure.depreciation_.charger_capex_per_kw \
            * self.years_[0].technical_.charging_and_demand.charging_ports.dc_charger_1_rating \
            / self.years_[0].financial_.capital_expenditure.depreciation_.charger_lifecycle_capacity \
        if self.years_[0].financial_.capital_expenditure.depreciation_.charger_lifecycle_capacity else 0


        '''****************************************
                    CONNECTIONS
        ****************************************'''
        ''' =========== FINANCIAL ==========='''  
        '''-------- capital expenditure -----------'''    
        #ess capex            
        self.years_[0].financial_.capital_expenditure.capital_expenditure_items.ess301Changed.connect(self.update_allNonZeroYears_financial_capitalExpenditure_depreciation_essCapex)

        self.years_[1].technical_.battery_storage.ess_system.installedCapacityChanged.connect(self.update_year1_financial_capitalExpenditure_depreciation_essCapex)
        self.years_[2].technical_.battery_storage.ess_system.installedCapacityChanged.connect(self.update_year2_financial_capitalExpenditure_depreciation_essCapex)
        self.years_[3].technical_.battery_storage.ess_system.installedCapacityChanged.connect(self.update_year3_financial_capitalExpenditure_depreciation_essCapex)
        self.years_[4].technical_.battery_storage.ess_system.installedCapacityChanged.connect(self.update_year4_financial_capitalExpenditure_depreciation_essCapex)
        self.years_[5].technical_.battery_storage.ess_system.installedCapacityChanged.connect(self.update_year5_financial_capitalExpenditure_depreciation_essCapex)

        #charger capex
        self.years_[0].financial_.capital_expenditure.capital_expenditure_items.dcChargersChanged.connect(self.update_allNonZeroYears_financial_capitalExpenditure_depreciation_chargerCapex)

        self.years_[1].technical_.charging_and_demand.charging_ports.dcCharger1RatingChanged.connect(self.update_year1_financial_capitalExpenditure_depreciation_chargerCapex)
        self.years_[2].technical_.charging_and_demand.charging_ports.dcCharger1RatingChanged.connect(self.update_year2_financial_capitalExpenditure_depreciation_chargerCapex)
        self.years_[3].technical_.charging_and_demand.charging_ports.dcCharger1RatingChanged.connect(self.update_year3_financial_capitalExpenditure_depreciation_chargerCapex)
        self.years_[4].technical_.charging_and_demand.charging_ports.dcCharger1RatingChanged.connect(self.update_year4_financial_capitalExpenditure_depreciation_chargerCapex)
        self.years_[5].technical_.charging_and_demand.charging_ports.dcCharger1RatingChanged.connect(self.update_year5_financial_capitalExpenditure_depreciation_chargerCapex)

        '''present value'''
        self.years_[0].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year0_financial_summary_discountingCashFlows_presentValue)
 
        self.years_[1].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year1_financial_summary_discountingCashFlows_presentValue)
        self.years_[1].financial_.summary_.discounted_cash_flow_section.weightedAverageCostOfCapitalChanged.connect(self.update_year1_financial_summary_discountingCashFlows_presentValue)

        self.years_[2].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year2_financial_summary_discountingCashFlows_presentValue)
        self.years_[2].financial_.summary_.discounted_cash_flow_section.weightedAverageCostOfCapitalChanged.connect(self.update_year2_financial_summary_discountingCashFlows_presentValue)

        self.years_[3].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year3_financial_summary_discountingCashFlows_presentValue)
        self.years_[3].financial_.summary_.discounted_cash_flow_section.weightedAverageCostOfCapitalChanged.connect(self.update_year3_financial_summary_discountingCashFlows_presentValue)

        self.years_[4].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year4_financial_summary_discountingCashFlows_presentValue)
        self.years_[4].financial_.summary_.discounted_cash_flow_section.weightedAverageCostOfCapitalChanged.connect(self.update_year4_financial_summary_discountingCashFlows_presentValue)

        self.years_[5].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year5_financial_summary_discountingCashFlows_presentValue)
        self.years_[5].financial_.summary_.discounted_cash_flow_section.weightedAverageCostOfCapitalChanged.connect(self.update_year5_financial_summary_discountingCashFlows_presentValue)

        '''cumulative cash flow'''
        self.years_[0].financial_.summary_.discounted_cash_flow_section.cumulativeCashFlowChanged.connect(self.update_year0_financial_summary_discountingCashFlows_cumulativeCashFlow)

        self.years_[1].financial_.summary_.discounted_cash_flow_section.cumulativeCashFlowChanged.connect(self.update_nonZeroYear_financial_summary_discountingCashFlows_cumulativeCashFlow)
        self.years_[1].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year1_financial_summary_discountingCashFlows_cumulativeCashFlow)

        self.years_[2].financial_.summary_.discounted_cash_flow_section.cumulativeCashFlowChanged.connect(self.update_nonZeroYear_financial_summary_discountingCashFlows_cumulativeCashFlow)
        self.years_[2].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year2_financial_summary_discountingCashFlows_cumulativeCashFlow)

        self.years_[3].financial_.summary_.discounted_cash_flow_section.cumulativeCashFlowChanged.connect(self.update_nonZeroYear_financial_summary_discountingCashFlows_cumulativeCashFlow)
        self.years_[3].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year3_financial_summary_discountingCashFlows_cumulativeCashFlow)

        self.years_[4].financial_.summary_.discounted_cash_flow_section.cumulativeCashFlowChanged.connect(self.update_nonZeroYear_financial_summary_discountingCashFlows_cumulativeCashFlow)
        self.years_[4].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year4_financial_summary_discountingCashFlows_cumulativeCashFlow)

        self.years_[5].financial_.summary_.discounted_cash_flow_section.cumulativeCashFlowChanged.connect(self.update_nonZeroYear_financial_summary_discountingCashFlows_cumulativeCashFlow)
        self.years_[5].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year5_financial_summary_discountingCashFlows_cumulativeCashFlow)

        '''net profits'''
        self.years_[0].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year0_financial_summary_internalRateOfReturnSection_netProfitsFairValue)

        self.years_[0].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year1_financial_summary_internalRateOfReturnSection_netProfitsFairValue)
        self.years_[1].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year1_financial_summary_internalRateOfReturnSection_netProfitsFairValue)

        self.years_[1].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year2_financial_summary_internalRateOfReturnSection_netProfitsFairValue)
        self.years_[0].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year2_financial_summary_internalRateOfReturnSection_netProfitsFairValue)
        self.years_[2].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year2_financial_summary_internalRateOfReturnSection_netProfitsFairValue)

        self.years_[0].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year3_financial_summary_internalRateOfReturnSection_netProfitsFairValue)
        self.years_[1].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year3_financial_summary_internalRateOfReturnSection_netProfitsFairValue)
        self.years_[2].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year3_financial_summary_internalRateOfReturnSection_netProfitsFairValue)
        self.years_[3].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year3_financial_summary_internalRateOfReturnSection_netProfitsFairValue)        

        self.years_[0].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year4_financial_summary_internalRateOfReturnSection_netProfitsFairValue)
        self.years_[1].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year4_financial_summary_internalRateOfReturnSection_netProfitsFairValue)
        self.years_[2].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year4_financial_summary_internalRateOfReturnSection_netProfitsFairValue)
        self.years_[3].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year4_financial_summary_internalRateOfReturnSection_netProfitsFairValue)
        self.years_[4].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year4_financial_summary_internalRateOfReturnSection_netProfitsFairValue)

        self.years_[0].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_netProfitsFairValue)
        self.years_[1].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_netProfitsFairValue)
        self.years_[2].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_netProfitsFairValue)
        self.years_[3].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_netProfitsFairValue)
        self.years_[4].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_netProfitsFairValue)
        self.years_[5].financial_.summary_.net_income_section.netIncomeChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_netProfitsFairValue)

        '''net present value'''
        self.years_[0].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year0_financial_summary_internalRateOfReturnSection_netPresentValue)

        self.years_[0].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year1_financial_summary_internalRateOfReturnSection_netPresentValue)
        self.years_[1].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year1_financial_summary_internalRateOfReturnSection_netPresentValue)

        self.years_[0].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year2_financial_summary_internalRateOfReturnSection_netPresentValue)
        self.years_[1].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year2_financial_summary_internalRateOfReturnSection_netPresentValue)
        self.years_[2].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year2_financial_summary_internalRateOfReturnSection_netPresentValue)

        self.years_[0].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year3_financial_summary_internalRateOfReturnSection_netPresentValue)
        self.years_[1].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year3_financial_summary_internalRateOfReturnSection_netPresentValue)
        self.years_[2].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year3_financial_summary_internalRateOfReturnSection_netPresentValue)
        self.years_[3].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year3_financial_summary_internalRateOfReturnSection_netPresentValue)

        self.years_[0].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year4_financial_summary_internalRateOfReturnSection_netPresentValue)
        self.years_[1].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year4_financial_summary_internalRateOfReturnSection_netPresentValue)
        self.years_[2].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year4_financial_summary_internalRateOfReturnSection_netPresentValue)
        self.years_[3].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year4_financial_summary_internalRateOfReturnSection_netPresentValue)
        self.years_[4].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year4_financial_summary_internalRateOfReturnSection_netPresentValue)

        self.years_[0].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_netPresentValue)
        self.years_[1].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_netPresentValue)
        self.years_[2].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_netPresentValue)
        self.years_[3].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_netPresentValue)
        self.years_[4].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_netPresentValue)
        self.years_[5].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_netPresentValue)
        
        ''' internal rate of return '''
        self.years_[0].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year0_financial_summary_internalRateOfReturnSection_internalRateOfReturn)

        self.years_[0].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year1_financial_summary_internalRateOfReturnSection_internalRateOfReturn)
        self.years_[1].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year1_financial_summary_internalRateOfReturnSection_internalRateOfReturn)

        self.years_[0].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year2_financial_summary_internalRateOfReturnSection_internalRateOfReturn)
        self.years_[1].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year2_financial_summary_internalRateOfReturnSection_internalRateOfReturn)
        self.years_[2].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year2_financial_summary_internalRateOfReturnSection_internalRateOfReturn)

        self.years_[0].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year3_financial_summary_internalRateOfReturnSection_internalRateOfReturn)
        self.years_[1].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year3_financial_summary_internalRateOfReturnSection_internalRateOfReturn)
        self.years_[2].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year3_financial_summary_internalRateOfReturnSection_internalRateOfReturn)
        self.years_[3].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year3_financial_summary_internalRateOfReturnSection_internalRateOfReturn)

        self.years_[0].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year4_financial_summary_internalRateOfReturnSection_internalRateOfReturn)
        self.years_[1].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year4_financial_summary_internalRateOfReturnSection_internalRateOfReturn)
        self.years_[2].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year4_financial_summary_internalRateOfReturnSection_internalRateOfReturn)
        self.years_[3].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year4_financial_summary_internalRateOfReturnSection_internalRateOfReturn)
        self.years_[4].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year4_financial_summary_internalRateOfReturnSection_internalRateOfReturn)

        self.years_[0].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_internalRateOfReturn)
        self.years_[1].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_internalRateOfReturn)
        self.years_[2].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_internalRateOfReturn)
        self.years_[3].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_internalRateOfReturn)
        self.years_[4].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_internalRateOfReturn)
        self.years_[5].financial_.summary_.free_cash_flow_section.freeCashFlowChanged.connect(self.update_year5_financial_summary_internalRateOfReturnSection_internalRateOfReturn)        
           
        self.emitUpdateSignals()

    def emitUpdateSignals(self):
        self.yearsChanged.emit()
        for year in self.years_:
            year.emitUpdateSignals()

    @Property(list, notify=yearsChanged) #getter
    def years(self) -> list:
        return self.years_

    @years.setter
    def years(self, years_:list) -> None:
        self.years_ = years_
        self.yearsChanged.emit()       

    @Property(int, notify=currentYearIndexChanged) #getter
    def currentYearIndex(self) -> int:
        return self.current_year_index

    @currentYearIndex.setter
    def currentYearIndex(self, current_year_index:int) -> None:
        self.current_year_index = current_year_index
        self.currentYearIndexChanged.emit()     

    @Property(FiveYearAnalysis, notify=fiveYearAnalysisChanged) #getter
    def fiveYearAnalysis(self) -> int:
        return self.five_year_analysis

    @fiveYearAnalysis.setter
    def fiveYearAnalysis(self, five_year_analysis:FiveYearAnalysis) -> None:
        self.five_year_analysis = five_year_analysis
        self.fiveYearAnalysisChanged.emit()                        
    '''****************************************
                    SLOTS
    ****************************************'''

    '''FINANCIAL'''
    '''---------------'''
    @Slot()
    def update_allNonZeroYears_financial_capitalExpenditure_depreciation_essCapex(self):
        for i in range(1,6):
            self._update_nonZeroYear_financial_capitalExpenditure_depreciation_essCapex(year_index=i)

    @Slot()
    def update_year1_financial_capitalExpenditure_depreciation_essCapex(self):
        self._update_nonZeroYear_financial_capitalExpenditure_depreciation_essCapex(year_index=1)

    @Slot()
    def update_year2_financial_capitalExpenditure_depreciation_essCapex(self):
        self._update_nonZeroYear_financial_capitalExpenditure_depreciation_essCapex(year_index=2)

    @Slot()
    def update_year3_financial_capitalExpenditure_depreciation_essCapex(self):
        self._update_nonZeroYear_financial_capitalExpenditure_depreciation_essCapex(year_index=3)

    @Slot()
    def update_year4_financial_capitalExpenditure_depreciation_essCapex(self):
        self._update_nonZeroYear_financial_capitalExpenditure_depreciation_essCapex(year_index=4)

    @Slot()
    def update_year5_financial_capitalExpenditure_depreciation_essCapex(self):
        self._update_nonZeroYear_financial_capitalExpenditure_depreciation_essCapex(year_index=5)        


    def _update_nonZeroYear_financial_capitalExpenditure_depreciation_essCapex(self, year_index:int):
        if (
            new_value := \
                self.years_[0].financial_.capital_expenditure.capital_expenditure_items.ess_301kwh \
                / self.years_[year_index].technical_.battery_storage.ess_system.installed_capacity_kwh \
            if self.years_[year_index].technical_.battery_storage.ess_system.installed_capacity_kwh else 0
        ) != self.years_[year_index].financial_.capital_expenditure.depreciation_.ess_capex_per_kwh:
            self.years_[year_index].financial_.capital_expenditure.depreciation_.ess_capex_per_kwh = new_value
            self.years_[year_index].financial_.capital_expenditure.depreciation_.essCapexPerKwhChanged.emit()  
    '''-------------------'''
    @Slot()
    def update_allNonZeroYears_financial_capitalExpenditure_depreciation_chargerCapex(self):
        for i in range(1,6):
            self._update_nonZeroYear_financial_capitalExpenditure_depreciation_chargerCapex(year_index=i)

    @Slot()
    def update_year1_financial_capitalExpenditure_depreciation_chargerCapex(self):
        self._update_nonZeroYear_financial_capitalExpenditure_depreciation_chargerCapex(year_index=1)

    @Slot()
    def update_year2_financial_capitalExpenditure_depreciation_chargerCapex(self):
        self._update_nonZeroYear_financial_capitalExpenditure_depreciation_chargerCapex(year_index=2)

    @Slot()
    def update_year3_financial_capitalExpenditure_depreciation_chargerCapex(self):
        self._update_nonZeroYear_financial_capitalExpenditure_depreciation_chargerCapex(year_index=3)

    @Slot()
    def update_year4_financial_capitalExpenditure_depreciation_chargerCapex(self):
        self._update_nonZeroYear_financial_capitalExpenditure_depreciation_chargerCapex(year_index=4)

    @Slot()
    def update_year5_financial_capitalExpenditure_depreciation_chargerCapex(self):
        self._update_nonZeroYear_financial_capitalExpenditure_depreciation_chargerCapex(year_index=5)                 

    @Slot()
    def _update_nonZeroYear_financial_capitalExpenditure_depreciation_chargerCapex(self, year_index:int):
        if (
            new_value := \
                self.years_[0].financial_.capital_expenditure.capital_expenditure_items.dc_chargers \
                / self.years_[year_index].technical_.charging_and_demand.charging_ports.dc_charger_1_rating \
            if self.years_[year_index].technical_.charging_and_demand.charging_ports.dc_charger_1_rating else 0
        ) != self.years_[year_index].financial_.capital_expenditure.depreciation_.charger_capex_per_kw:
            self.years_[year_index].financial_.capital_expenditure.depreciation_.charger_capex_per_kw = new_value
            self.years_[year_index].financial_.capital_expenditure.depreciation_.chargerCapexPerKwChanged.emit()            

    @Slot()
    def update_year0_financial_summary_discountingCashFlows_presentValue(self):
        if (new_value := self.years_[0].financial_.summary_.free_cash_flow_section.free_cash_flow) != self.years_[0].financial_.summary_.discounted_cash_flow_section.present_value_of_cash_flow:
            self.years_[0].financial_.summary_.discounted_cash_flow_section.present_value_of_cash_flow = new_value
            self.years_[0].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.emit()


            

    '''--------- Operating Expenditure -----------'''            
    def _update_nonZeroYear_financial_summary_discountingCashFlows_presentValue(self, year_index:int):
        if (
            new_value := \
                self.years_[year_index].financial_.summary_.free_cash_flow_section.free_cash_flow \
                * (1 - self.years_[year_index].financial_.summary_.discounted_cash_flow_section.weighted_average_cost_of_capital )
                ** (year_index-1)
        ) != self.years_[year_index].financial_.summary_.discounted_cash_flow_section.present_value_of_cash_flow:
            self.years_[year_index].financial_.summary_.discounted_cash_flow_section.present_value_of_cash_flow = new_value
            self.years_[year_index].financial_.summary_.discounted_cash_flow_section.presentValueOfCashFlowChanged.emit()

    @Slot()
    def update_year1_financial_summary_discountingCashFlows_presentValue(self):
        self._update_nonZeroYear_financial_summary_discountingCashFlows_presentValue(year_index=1)

    @Slot()
    def update_year2_financial_summary_discountingCashFlows_presentValue(self):
        self._update_nonZeroYear_financial_summary_discountingCashFlows_presentValue(year_index=2)

    @Slot()
    def update_year3_financial_summary_discountingCashFlows_presentValue(self):
        self._update_nonZeroYear_financial_summary_discountingCashFlows_presentValue(year_index=3)

    @Slot()
    def update_year4_financial_summary_discountingCashFlows_presentValue(self):
        self._update_nonZeroYear_financial_summary_discountingCashFlows_presentValue(year_index=4)

    @Slot()
    def update_year5_financial_summary_discountingCashFlows_presentValue(self):
        self._update_nonZeroYear_financial_summary_discountingCashFlows_presentValue(year_index=5)   

    '''cumulative cash flow'''
    @Slot()
    def update_year0_financial_summary_discountingCashFlows_cumulativeCashFlow(self):
        if (new_value := self.years_[0].financial_.summary_.discounted_cash_flow_section.present_value_of_cash_flow) != self.years_[0].financial_.summary_.discounted_cash_flow_section.cumulative_cash_flow:
            self.years_[0].financial_.summary_.discounted_cash_flow_section.cumulative_cash_flow = new_value
            self.years_[0].financial_.summary_.discounted_cash_flow_section.cumulativeCashFlowChanged.emit()

    def _update_nonZeroYear_financial_summary_discountingCashFlows_cumulativeCashFlow(self, year_index:int):
        if (
            new_value := \
                self.years_[year_index-1].financial_.summary_.discounted_cash_flow_section.cumulative_cash_flow \
                + self.years_[year_index].financial_.summary_.discounted_cash_flow_section.present_value_of_cash_flow
        ) != self.years_[year_index].financial_.summary_.discounted_cash_flow_section.cumulative_cash_flow:
            self.years_[year_index].financial_.summary_.discounted_cash_flow_section.cumulative_cash_flow = new_value
            self.years_[year_index].financial_.summary_.discounted_cash_flow_section.cumulativeCashFlowChanged.emit()

    @Slot()
    def update_year1_financial_summary_discountingCashFlows_cumulativeCashFlow(self):
        self._update_nonZeroYear_financial_summary_discountingCashFlows_cumulativeCashFlow(year_index=1)

    @Slot()
    def update_year2_financial_summary_discountingCashFlows_cumulativeCashFlow(self):
        self._update_nonZeroYear_financial_summary_discountingCashFlows_cumulativeCashFlow(year_index=2)

    @Slot()
    def update_year3_financial_summary_discountingCashFlows_cumulativeCashFlow(self):
        self._update_nonZeroYear_financial_summary_discountingCashFlows_cumulativeCashFlow(year_index=3)

    @Slot()
    def update_year4_financial_summary_discountingCashFlows_cumulativeCashFlow(self):
        self._update_nonZeroYear_financial_summary_discountingCashFlows_cumulativeCashFlow(year_index=4)

    @Slot()
    def update_year5_financial_summary_discountingCashFlows_cumulativeCashFlow(self):
        self._update_nonZeroYear_financial_summary_discountingCashFlows_cumulativeCashFlow(year_index=5)               

    @Slot()
    def update_nonZeroYear_financial_summary_discountingCashFlows_cumulativeCashFlow(self):
        for year_index in range(6):
            if (
                new_value := \
                    self.years_[year_index-1].financial_.summary_.discounted_cash_flow_section.cumulative_cash_flow \
                    + self.years_[year_index].financial_.summary_.discounted_cash_flow_section.present_value_of_cash_flow
            ) != self.years_[year_index].financial_.summary_.discounted_cash_flow_section.cumulative_cash_flow:
                self.years_[year_index].financial_.summary_.discounted_cash_flow_section.cumulative_cash_flow = new_value
                self.years_[year_index].financial_.summary_.discounted_cash_flow_section.cumulativeCashFlowChanged.emit()
               


    def _update_year_financial_summary_internalRateOfReturnSection_netPresentValue(self, year_index:int):
        new_value:float = 0
        for year in self.years_[:year_index+1]:
            new_value += year.financial_.summary_.discounted_cash_flow_section.present_value_of_cash_flow
        if self.years_[year_index].financial_.summary_.internal_rate_of_return_section.net_present_value != new_value:
            self.years_[year_index].financial_.summary_.internal_rate_of_return_section.net_present_value = new_value
            self.years_[year_index].financial_.summary_.internal_rate_of_return_section.netPresentValueChanged.emit()
   

    @Slot()
    def update_year0_financial_summary_internalRateOfReturnSection_netPresentValue(self):
        self._update_year_financial_summary_internalRateOfReturnSection_netPresentValue(year_index=0)   

    @Slot()
    def update_year1_financial_summary_internalRateOfReturnSection_netPresentValue(self):
        self._update_year_financial_summary_internalRateOfReturnSection_netPresentValue(year_index=1)   

    @Slot()
    def update_year2_financial_summary_internalRateOfReturnSection_netPresentValue(self):
        self._update_year_financial_summary_internalRateOfReturnSection_netPresentValue(year_index=2)   

    @Slot()
    def update_year3_financial_summary_internalRateOfReturnSection_netPresentValue(self):
        self._update_year_financial_summary_internalRateOfReturnSection_netPresentValue(year_index=3)   

    @Slot()
    def update_year4_financial_summary_internalRateOfReturnSection_netPresentValue(self):
        self._update_year_financial_summary_internalRateOfReturnSection_netPresentValue(year_index=4)   

    @Slot()
    def update_year5_financial_summary_internalRateOfReturnSection_netPresentValue(self):
        self._update_year_financial_summary_internalRateOfReturnSection_netPresentValue(year_index=5)           

    def _update_year_financial_summary_internalRateOfReturnSection_netProfitsFairValue(self, year_index: int):
        new_value:float = 0
        for year in self.years_[:year_index+1]:
            new_value += year.financial_.summary_.net_income_section.net_income
        if self.years_[year_index].financial_.summary_.internal_rate_of_return_section.net_profits_fair_value != new_value:
            self.years_[year_index].financial_.summary_.internal_rate_of_return_section.net_profits_fair_value = new_value
            self.years_[year_index].financial_.summary_.internal_rate_of_return_section.netProfitsFairValueChanged.emit()

    @Slot()
    def update_year0_financial_summary_internalRateOfReturnSection_netProfitsFairValue(self):
        self._update_year_financial_summary_internalRateOfReturnSection_netProfitsFairValue(year_index=0)   

    @Slot()
    def update_year1_financial_summary_internalRateOfReturnSection_netProfitsFairValue(self):
        self._update_year_financial_summary_internalRateOfReturnSection_netProfitsFairValue(year_index=1)   

    @Slot()
    def update_year2_financial_summary_internalRateOfReturnSection_netProfitsFairValue(self):
        self._update_year_financial_summary_internalRateOfReturnSection_netProfitsFairValue(year_index=2)   

    @Slot()
    def update_year3_financial_summary_internalRateOfReturnSection_netProfitsFairValue(self):
        self._update_year_financial_summary_internalRateOfReturnSection_netProfitsFairValue(year_index=3)   

    @Slot()
    def update_year4_financial_summary_internalRateOfReturnSection_netProfitsFairValue(self):
        self._update_year_financial_summary_internalRateOfReturnSection_netProfitsFairValue(year_index=4)               

    @Slot()
    def update_year5_financial_summary_internalRateOfReturnSection_netProfitsFairValue(self):
        self._update_year_financial_summary_internalRateOfReturnSection_netProfitsFairValue(year_index=5)       

    def _update_year_financial_summary_internalRateOfReturnSection_internalRateOfReturn(self, year_index: int):
        new_value = npf.irr([year.financial_.summary_.free_cash_flow_section.free_cash_flow for year in self.years_[:year_index+1]])
        if self.years_[year_index].financial_.summary_.internal_rate_of_return_section.internal_rate_of_return != new_value:
            self.years_[year_index].financial_.summary_.internal_rate_of_return_section.internal_rate_of_return = new_value
            self.years_[year_index].financial_.summary_.internal_rate_of_return_section.internalRateOfReturnChanged.emit()

    @Slot()
    def update_year0_financial_summary_internalRateOfReturnSection_internalRateOfReturn(self):
        self._update_year_financial_summary_internalRateOfReturnSection_internalRateOfReturn(year_index=0)   

    @Slot()
    def update_year1_financial_summary_internalRateOfReturnSection_internalRateOfReturn(self):
        self._update_year_financial_summary_internalRateOfReturnSection_internalRateOfReturn(year_index=1)   

    @Slot()
    def update_year2_financial_summary_internalRateOfReturnSection_internalRateOfReturn(self):
        self._update_year_financial_summary_internalRateOfReturnSection_internalRateOfReturn(year_index=2)   

    @Slot()
    def update_year3_financial_summary_internalRateOfReturnSection_internalRateOfReturn(self):
        self._update_year_financial_summary_internalRateOfReturnSection_internalRateOfReturn(year_index=3)   

    @Slot()
    def update_year4_financial_summary_internalRateOfReturnSection_internalRateOfReturn(self):
        self._update_year_financial_summary_internalRateOfReturnSection_internalRateOfReturn(year_index=4)               

    @Slot()
    def update_year5_financial_summary_internalRateOfReturnSection_internalRateOfReturn(self):
        self._update_year_financial_summary_internalRateOfReturnSection_internalRateOfReturn(year_index=5)    
