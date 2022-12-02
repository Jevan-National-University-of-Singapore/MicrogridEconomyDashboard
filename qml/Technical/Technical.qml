import QtQuick
import QtQuick.Controls.Material

import "Sections/BatteryStorage"
import "Sections/ChargingAndDemand"
import "Sections/SolarPowerGeneration"

import "../Templates" as Templates

Templates.Page {
    id: root

    bottomMargin: batteryStorage.label.font.pixelSize

    BatteryStorage{
        id: batteryStorage

        anchors {
            top: parent.top
            topMargin: batteryStorage.label.font.pixelSize

            left: parent.left
            leftMargin: batteryStorage.label.font.pixelSize
        }
    }


    SolarPowerGeneration{
        id: solarPowerGeneration

        anchors {
            top: batteryStorage.bottom
            topMargin: batteryStorage.anchors.topMargin

            left: batteryStorage.left
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
