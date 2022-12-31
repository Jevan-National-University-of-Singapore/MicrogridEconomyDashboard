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
=IF(O80>0,IF(O85="NO",IF(O88="NO",N81-O80,N81+O76),N81+O76),IF(O88="NO",N81+O76,N81))

if load_on_ess is 0:
	if insufficient_charge is "NO":
		if reached_ess_soc is "NO":
			N81-O81
			previous_soc_
		else:
			N81 + O76
	else:
		N81 + O76
else:
	if reached_ess_soc is "NO":
		N81 + O76
	else:
		N81
'''