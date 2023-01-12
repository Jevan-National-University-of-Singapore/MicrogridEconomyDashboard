import sys
import os

from PySide6.QtGui import *
from PySide6.QtQml import *
from PySide6.QtWidgets import *

from CBA_v5.Scenario import Scenario

PWD = dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

if __name__ == '__main__':

    app:QApplication = QApplication(sys.argv)

    scenario:Scenario = Scenario()

    engine:QQmlApplicationEngine = QQmlApplicationEngine()

    engine.rootContext().setContextProperty("Scenario", scenario)
    engine.quit.connect(app.quit)


    engine.load('qml/main.qml')

    sys.exit(app.exec())

    # Database.connect(rf"{PWD}\database\database.db")
'''
O52: charger_needed
N46: ess_charge
O41: total_charge_supply
E27: soc_upper_limit
E28: soc_lower_limit
E23: installed_capacity
O44: dc_charger_demand


=IF(charger_needed="NO",
	IF(ess_charge+total_charge_supply>$soc_upper_limit*$installed_capacity,
		"YES",
	else
		 "NO"),
else
	IF(ess_charge-(dc_charger_demand-total_charge_supply)<$soc_lower_limit*$installed_capacity,
		"YES",
	else
		"NO"))
'''