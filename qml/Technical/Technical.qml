import QtQuick
import QtQuick.Controls.Material

import "Sections/BatteryStorage"
import "Sections/ChargingAndDemand"

Item {
    id: root

    height: childrenRect.height
    width: childrenRect.width

    BatteryStorage{
        id: batteryStorage

        anchors {
            top: root.top
            topMargin: batteryStorage.label.font.pixelSize

            left: root.left
            leftMargin: batteryStorage.label.font.pixelSize
        }
    }

    ChargingAndDemand {
        id: chargingAndDemand
        anchors {
            top: batteryStorage.top

            left: batteryStorage.right
            leftMargin: chargingAndDemand.label.font.pixelSize
        }

    }

}