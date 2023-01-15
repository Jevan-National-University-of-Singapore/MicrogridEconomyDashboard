import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Material

import "../Delegates"

Item {
    id: root
    property alias solarPowerGeneration: solarPowerGeneration
    property alias batteryStorage: batteryStorage
    property alias chargingAndDemand: chargingAndDemand

    function collapse() {
        solarPowerGeneration.collapse()
        batteryStorage.collapse()
        chargingAndDemand.collapse()
        opacityAnimation.velocity = 5
        opacity = 0
    }    

    function show() {
        solarPowerGeneration.show()
        batteryStorage.show()
        chargingAndDemand.show()
        opacityAnimation.velocity = 2.5
        opacity = 1
    }        

    Behavior on opacity { SmoothedAnimation { id:opacityAnimation; velocity: 5 } }

    Column{
        id: subTreeViews

        clip: true

        height: childrenRect.implicitHeight; width: contentWidth

        SolarPowerGenerationTreeView {
            id: solarPowerGeneration

            onInstalledCapacitySelected: {
                batteryStorage.deselectAll()
                chargingAndDemand.deselectAll()
            }
            onAyerKerohSiteConditionsSelected: {
                batteryStorage.deselectAll()
                chargingAndDemand.deselectAll()
            }
            onSolarEnergyProductionSelected: {
                batteryStorage.deselectAll()
                chargingAndDemand.deselectAll()
            }
            onHourlySolarPowerGenerationSelected: {
                batteryStorage.deselectAll()
                chargingAndDemand.deselectAll()
            }
        }

        BatteryStorageTreeView {
            id: batteryStorage

            onEssSystemSelected:{
                chargingAndDemand.deselectAll()
                solarPowerGeneration.deselectAll()
            }

            onDischargeSelected:{
                chargingAndDemand.deselectAll()
                solarPowerGeneration.deselectAll()
            }

            onGridChargingSelected:{
                chargingAndDemand.deselectAll()
                solarPowerGeneration.deselectAll()
            }

        }

        ChargingAndDemandTreeView {
            id: chargingAndDemand           

            onChargingPortsSelected: {
                solarPowerGeneration.deselectAll()
                batteryStorage.deselectAll()
            }
            onDemandSelected: {
                solarPowerGeneration.deselectAll()
                batteryStorage.deselectAll()
            }
            onLoadSelected: {
                solarPowerGeneration.deselectAll()
                batteryStorage.deselectAll()
            }
            onExcessToFacilitySelected: {
                solarPowerGeneration.deselectAll()
                batteryStorage.deselectAll()
            }
            onEvCharacteristicsSelected: {
                solarPowerGeneration.deselectAll()
                batteryStorage.deselectAll()
            }
            onHourlyDemandSelected: {
                solarPowerGeneration.deselectAll()
                batteryStorage.deselectAll()
            }
        }

    }
}