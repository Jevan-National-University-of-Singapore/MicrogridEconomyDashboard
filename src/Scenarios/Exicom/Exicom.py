import sys
import os

pwd = os.getcwd()
if pwd not in sys.path:
    sys.path.append(pwd)

from Scenario.Scenario import Scenario
from Scenario.FiveYearAnalysis.FiveYearAnalysis import FiveYearAnalysis

from .Year0 import year0
from .Year1 import year1
from .Year2 import year2
from .Year3 import year3
from .Year4 import year4
from .Year5 import year5



exicom = Scenario(
        years = [year0,year1,year2,year3,year4,year5],
        five_year_analysis=FiveYearAnalysis(
                net_present_value = 0,
                internal_rate_of_return = 0,
                net_profits = 0,
                initial_investment = 0
        )
    
)