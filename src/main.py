import sys
import os

from PySide6.QtGui import *
from PySide6.QtQml import *

from CBA_v5.Scenario import Scenario

PWD = dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    scenario = Scenario()

    engine = QQmlApplicationEngine()

    engine.rootContext().setContextProperty("Scenario", scenario)
    engine.quit.connect(app.quit)


    engine.load('qml/main.qml')

    sys.exit(app.exec())

    # Database.connect(rf"{PWD}\database\database.db")
