import QtQuick
import "../../Templates" as Templates

Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "Ayer Keroh Site Conditions"

        anchors{
            left: parent.left
            leftMargin: Qt.application.font.pixelSize
            
            top: parent.top
            topMargin: Qt.application.font.pixelSize
        }

        Templates.LabelledInput {
            id: specificPvPowerOutputPerDay

            label: "Specific PV power output"
            units: "/day"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.ayerKerohSiteConditions.specificPvPowerOutputPerDay = parseFloat(specificPvPowerOutputPerDay.inputText)

            inputText: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.ayerKerohSiteConditions.specificPvPowerOutputPerDay.toFixed(2)
        }

        Templates.LabelledText {
            id: specificPvPowerOutputPerYear

            labelText: "Specific PV power output"
            units: "/year"

            text: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.ayerKerohSiteConditions.specificPvPowerOutputPerYear.toFixed(2)
        }
    }
}