from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

'''
IGNORE THIS FILE, NOT COMPLETED
'''

class Target(QObject):
    boundingBoxChanged = Signal()
    confChanged = Signal()
    idChanged = Signal()

    def __init__(self, installed_capacity, class_id, conf, bounding_box, parent = None):
        super().__init__(parent)

        self._id = id
        self._class_id = class_id
        self._conf = conf
        self._bounding_box = bounding_box

    @Property(str, notify=idChanged)
    def id(self):
        return str(int(self._id))

    @Property(str)
    def classId(self):
        return str(self._class_id)

    @Property(str, notify=confChanged)
    def conf(self):
        return str(np.around(self._conf,2))

    @Property(QRect, notify=boundingBoxChanged)
    def boundingBox(self):
        return self._bounding_box
    