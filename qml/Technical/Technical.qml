import QtQuick
import QtQuick.Controls.Material

import "SolarPowerGeneration"
import "SolarPowerGeneration/HourlySolarPowerGenerationDialog"

import "BatteryStorage"
import "ChargingAndDemand"
// import "Sections/FiveYearsAnalysis"

import "../Templates" as Templates




Page {
    id: root

    function goToInstalledCapacity(){
        swipeView.currentIndex = 0
    }

    function goToAyerKerohSiteConditions(){
        swipeView.currentIndex = 1
    }

    function goToSolarEnergyProduction(){
        swipeView.currentIndex = 2
    }


    SwipeView{
        id: swipeView

        anchors.fill: parent

        orientation: Qt.Vertical

        contentHeight: installedCapacity.height 
                        + ayerKerohSiteConditions.height
                        + solarEnergyProduction.height

        clip: true


        InstalledCapacity{
            id: installedCapacity
        }

        AyerKerohSiteConditions{
            id: ayerKerohSiteConditions

        }
        SolarEnergyProduction {
            id: solarEnergyProduction

        }
        // SolarPowerGeneration{
        //     id: solarPowerGeneration

        //     anchors {
        //         top: batteryStorage.bottom
        //         topMargin: batteryStorage.anchors.topMargin

        //         left: batteryStorage.left
        //     }

        //     onOpenHourlySolarPowerGenerationTriggered: {
        //         swipeView.openDialog()
        //         hourlySolarPowerGenerationDialog.show()
        //     }


        // }

        // BatteryStorage{
        //     id: batteryStorage

        //     anchors {
        //         top: parent.top
        //         topMargin: batteryStorage.label.font.pixelSize

        //         left: parent.left
        //         leftMargin: batteryStorage.label.font.pixelSize
        //     }
        // }


        // ChargingAndDemand {
        //     id: chargingAndDemand
        //     anchors {
        //         top: batteryStorage.top

        //         left: batteryStorage.right
        //         leftMargin: chargingAndDemand.label.font.pixelSize
        //     }

        // }

        // data: HourlySolarPowerGenerationDialog{
        //     id: hourlySolarPowerGenerationDialog

        //     opacity: 0

        //     anchors.centerIn: parent
        // }

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
}




