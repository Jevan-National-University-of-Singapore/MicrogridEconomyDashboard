import QtQuick
import QtQuick.Controls.Material

import "Sections/SolarPowerGeneration"
import "Sections/SolarPowerGeneration/HourlySolarPowerGenerationDialog"

import "Sections/BatteryStorage"
import "Sections/ChargingAndDemand"
// import "Sections/FiveYearsAnalysis"

import "../Templates" as Templates

Templates.Page {
    id: root

    bottomMargin: batteryStorage.label.font.pixelSize

    // Component.onCompleted: console.log(Scenario.currentYearIndex)
    onOutsideDialogAreaClicked: hourlySolarPowerGenerationDialog.close()


    SolarPowerGeneration{
        id: solarPowerGeneration

        anchors {
            top: batteryStorage.bottom
            topMargin: batteryStorage.anchors.topMargin

            left: batteryStorage.left
        }

        onOpenHourlySolarPowerGenerationTriggered: {
            root.openDialog()
            hourlySolarPowerGenerationDialog.show()
        }


    }

    BatteryStorage{
        id: batteryStorage

        anchors {
            top: parent.top
            topMargin: batteryStorage.label.font.pixelSize

            left: parent.left
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

    data: HourlySolarPowerGenerationDialog{
        id: hourlySolarPowerGenerationDialog

        opacity: 0

        anchors.centerIn: parent
    }

    // Rectangle {
    //     anchors.centerIn: parent

    //     height: 500
    //     width: height
    // }

    // FiveYearsAnalysis {
    //     id: fiveYearsAnalysis

    //     anchors {
    //         top: solarPowerGeneration.bottom
    //         topMargin: solarPowerGeneration.anchors.topMargin

    //         left: solarPowerGeneration.left
    //     }
    // }

    


}
