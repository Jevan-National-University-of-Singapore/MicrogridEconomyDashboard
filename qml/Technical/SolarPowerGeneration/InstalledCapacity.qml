import QtQuick

import "../../Templates" as Templates

Templates.Page{
    id: root
    Templates.SubSection {
        id: subsectionItems

        subsection: "Installed Capacity"

        anchors{
            left: parent.left
            leftMargin: Qt.application.font.pixelSize
            
            top: parent.top
            topMargin: Qt.application.font.pixelSize
        }
        
        Templates.LabelledInput {
            id: installedCapacity

            label: "Installed Capacity"
            units: "kWp"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.installedCapacity.installedCapacity = installedCapacity.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.installedCapacity.installedCapacity
        }

    }
}