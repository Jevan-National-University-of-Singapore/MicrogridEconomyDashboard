import QtQuick
import QtQuick.Controls.Material

import "SolarPowerGeneration"
import "SolarPowerGeneration/HourlySolarPowerGeneration"

import "BatteryStorage"

import "ChargingAndDemand"
import "ChargingAndDemand/HourlyDemand"


import "../Templates" as Templates

Page {
    id: root

    property alias swipeView: swipeView

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

    // Frame {
    //     height: swipeView.height; width: swipeView.width    

    // }

    SwipeView{
        id: swipeView

        anchors.fill: parent

        orientation: Qt.Vertical

        interactive: false 

        // contentHeight: installedCapacity.height 
        //                 + ayerKerohSiteConditions.height
        //                 + solarEnergyProduction.height
        //                 + hourlySolarPowerGeneration.height
        //                 + essSystem.height
        //                 + discharge.height
        //                 + gridCharging.height
        //                 + chargingPorts.height
        //                 + demand.height
        //                 + load.height
        //                 + excessToFacility.height
        //                 + evCharacteristics.height
        //                 + hourlyDemand.height

        clip: true

        // Frame {implicitHeight: swipeView.implicitHeight; width: swipeView.width}
        // Frame {implicitHeight: swipeView.implicitHeight; width: swipeView.width}
        // Frame {implicitHeight: swipeView.implicitHeight; width: swipeView.width}
        // Frame {implicitHeight: swipeView.implicitHeight; width: swipeView.width}
        // Frame {implicitHeight: swipeView.implicitHeight; width: swipeView.width}
        // Frame {implicitHeight: swipeView.implicitHeight; width: swipeView.width}
        // Frame {implicitHeight: swipeView.implicitHeight; width: swipeView.width}
        // Frame {implicitHeight: swipeView.implicitHeight; width: swipeView.width}
        // Frame {implicitHeight: swipeView.implicitHeight; width: swipeView.width}
        // Frame {implicitHeight: swipeView.implicitHeight; width: swipeView.width}
        // Frame {implicitHeight: swipeView.implicitHeight; width: swipeView.width}
        // Frame {implicitHeight: swipeView.implicitHeight; width: swipeView.width}
        // Frame {implicitHeight: swipeView.implicitHeight; width: swipeView.width}
        // Frame {implicitHeight: swipeView.implicitHeight; width: swipeView.width}

        
        InstalledCapacity{id: installedCapacity
            height: root.height; width: root.width
        }

        AyerKerohSiteConditions{id: ayerKerohSiteConditions
            height: root.height
        }
        SolarEnergyProduction {id: solarEnergyProduction
            height: root.height
        }
        HourlySolarPowerGeneration {id: hourlySolarPowerGeneration
            height: root.height
        }

        EssSystem{id: essSystem
            height: root.height
        }
        Discharge{id: discharge
            height: root.height
        }
        GridCharging{id: gridCharging
            height: root.height
        }

        ChargingPorts {id: chargingPorts
            height: root.height
        }
        Demand{id: demand
            height: root.height
        }
        Load{id: load
            height: root.height
        }
        ExcessToFacility {id: excessToFacility
            height: root.height
        }
        EvCharacteristics {id: evCharacteristics
            height: root.height
        }
        HourlyDemand{id: hourlyDemand; height: root.height; width: root.width; anchors.left: parent.left}
        
    }
}




