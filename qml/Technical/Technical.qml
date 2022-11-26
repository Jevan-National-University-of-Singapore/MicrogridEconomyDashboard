import QtQuick
import QtQuick.Controls.Material

import "Sections/BatteryStorage"
import "Sections/ChargingAndDemand"

Item {
    id: root

    BatteryStorage{
        id: batteryStorage

        anchors {
            top: root.top
            topMargin: root.height/40

            left: root.left
            leftMargin: root.width/40
        }

        height: root.height/1.5
        width: root.width/2.2
    }

    ChargingAndDemand {
        id: chargingAndDemand
        anchors {
            top: root.top
            topMargin: root.height/40

            left: batteryStorage.right
            leftMargin: root.width/40

            bottom: root.bottom
            bottomMargin: root.height/40
        }

        width: root.width/2.2
    }

}