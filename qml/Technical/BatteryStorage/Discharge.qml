import QtQuick
import QtQuick.Controls.Material
import "../../Templates" as Templates

Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "Discharge"

        anchors{
            left: parent.left
            leftMargin: Qt.application.font.pixelSize
            
            top: parent.top
            topMargin: Qt.application.font.pixelSize
        }

        Templates.LabelledText {
            id: powerContinuous

            labelText: "Power (Continuous, 0.75C)"
            units: "kW"

            text: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.discharge.powerContinuous.toFixed(2)
        }

        Templates.LabelledText {
            id: powerMax

            labelText: "Power (max, 1C)"
            units: "kW"

            text: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.discharge.powerMax.toFixed(2)
        }

    }
}