import QtQuick
import QtQuick.Controls.Material

import "SolarPowerGeneration"
import "SolarPowerGeneration/HourlySolarPowerGeneration"

import "BatteryStorage"

import "ChargingAndDemand"
import "ChargingAndDemand/HourlyDemand"

// import "Sections/FiveYearsAnalysis"

import "../Templates" as Templates

Page {
    id: root

    function goToInstalledCapacity(){swipeView.currentIndex = 0}
    function goToAyerKerohSiteConditions(){swipeView.currentIndex = 1}
    function goToSolarEnergyProduction(){swipeView.currentIndex = 2}
    function goToHourlySolarPowerGeneration(){swipeView.currentIndex = 3}

    function goToEssSystem(){swipeView.currentIndex = 4}
    function goToDischarge(){swipeView.currentIndex = 5}
    function goToGridCharging(){swipeView.currentIndex = 6}

    function goToChargingPorts(){swipeView.currentIndex = 7}
    function goToDemand(){swipeView.currentIndex = 8}
    function goToLoad(){swipeView.currentIndex = 9}
    function goToExcessToFacility(){swipeView.currentIndex = 10}
    function goToEvCharacteristics(){swipeView.currentIndex = 11}
    function goToHourlyDemand(){swipeView.currentIndex = 12}

    SwipeView{
        id: swipeView

        anchors.fill: parent

        orientation: Qt.Vertical

        contentHeight: installedCapacity.height 
                        + ayerKerohSiteConditions.height
                        + solarEnergyProduction.height

        clip: true

        InstalledCapacity{id: installedCapacity}
        AyerKerohSiteConditions{id: ayerKerohSiteConditions}
        SolarEnergyProduction {id: solarEnergyProduction}
        HourlySolarPowerGeneration {id: hourlySolarPowerGeneration}

        EssSystem{id: essSystem}
        Discharge{id: discharge}
        GridCharging{id: gridCharging}

        ChargingPorts {id: chargingPorts}
        Demand{id: demand}
        Load{id: load}
        ExcessToFacility {id: excessToFacility}
        EvCharacteristics {id: evCharacteristics}
        HourlyDemand{id: hourlyDemand; height: root.height; width: root.width; anchors.left: parent.left}
        
    }
}




