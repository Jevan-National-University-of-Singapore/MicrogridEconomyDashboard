import sys
import os

from PySide6.QtGui import *
from PySide6.QtQml import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from Scenario.Scenario import Scenario

PWD = dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

if __name__ == '__main__':


    app:QApplication = QApplication(sys.argv)

    scenario:Scenario = Scenario()

    engine:QQmlApplicationEngine = QQmlApplicationEngine()

    engine.rootContext().setContextProperty("applicationDirPath", QDir.currentPath())

    engine.rootContext().setContextProperty("Scenario", scenario)
    engine.quit.connect(app.quit)


    engine.load('qml/main.qml')

    sys.exit(app.exec())
