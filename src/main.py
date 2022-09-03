import sys

from PySide6.QtGui import *
from PySide6.QtQml import *

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)

    engine.load('qml/main.qml')

    sys.exit(app.exec())