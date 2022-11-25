import sys
import os

from PySide6.QtGui import *
from PySide6.QtQml import *

from CBA_v5.Technical.Technical import Technical

PWD = dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)

    technical = Technical()

    engine = QQmlApplicationEngine()

    engine.rootContext().setContextProperty("Scenario", technical)
    engine.quit.connect(app.quit)


    engine.load('qml/main.qml')

    sys.exit(app.exec())

    # Database.connect(rf"{PWD}\database\database.db")
