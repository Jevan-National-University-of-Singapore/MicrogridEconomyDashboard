import QtQuick
import "../../Templates" as Templates

Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "Load"

        anchors{
            left: parent.left
            leftMargin: Qt.application.font.pixelSize
            
            top: parent.top
            topMargin: Qt.application.font.pixelSize
        }


        Templates.LabelledText {
            id: requiredEnergyPerUser

            labelText: "Required energy / user"
            units: "kWh"

            text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.load.requiredEnergyPerUser.toFixed(2)
        }

        Templates.LabelledText {
            id: requiredEnergyPerDay

            labelText: "Required energy / day"
            units: "kWh"

            text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.load.requiredEnergyPerDay.toFixed(2)
        }

        Templates.LabelledText {
            id: requiredEnergyPerYear

            labelText: "Required energy / year"
            units: "kWh"

            text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.load.requiredEnergyPerYear.toFixed(2)
        }

    }
}
