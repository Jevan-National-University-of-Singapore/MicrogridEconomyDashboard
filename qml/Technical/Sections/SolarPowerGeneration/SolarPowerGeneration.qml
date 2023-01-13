import QtQuick
import QtQuick.Controls.Material
import "../../../Templates"
import "../../../Templates/Separators"

import "SubSections"


Section {
    id: root

    section: "Solar Power Generation"

    signal openHourlySolarPowerGenerationTriggered

    InstalledCapacity {
        id: installedCapacity
    }

    HorizontalSeparator {
        id: installedCapacitySeparator

        anchors {
            top: installedCapacity.bottom
            topMargin: installedCapacity.label.font.pixelSize
            horizontalCenter: installedCapacity.horizontalCenter
        }

        length: installedCapacity.width - installedCapacity.label.font.pixelSize
    }

    AyerKerohSiteConditions {
        id: ayerKerohSiteConditions

        anchors {
            top: installedCapacitySeparator.bottom
            topMargin: ayerKerohSiteConditions.label.font.pixelSize

            left: installedCapacity.left
        }
    }

    VerticalSeparator {
        id: verticalSeparator

        anchors {
            left: installedCapacity.right
            leftMargin: ayerKerohSiteConditions.label.font.pixelSize
        }

        length: (ayerKerohSiteConditions.height + ayerKerohSiteConditions.y - installedCapacity.y) - ayerKerohSiteConditions.label.font.pixelSize
    }

    SolarEnergyProduction {
        id: solarEnergyProduction

        anchors {
            left: verticalSeparator.right
            leftMargin: solarEnergyProduction.label.font.pixelSize
        }
    }

    Button {
        id: hourlySolarPowerGenerationButton

        text: "Hourly Generation"

        anchors {
            top: solarEnergyProduction.bottom
            topMargin: solarEnergyProduction.label.font.pixelSize/2

            horizontalCenter: solarEnergyProduction.horizontalCenter
        }

        onClicked: root.openHourlySolarPowerGenerationTriggered()
    }

    

}