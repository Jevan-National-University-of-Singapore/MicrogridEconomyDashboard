import QtQuick
import "../../Templates" as Templates

Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "Excess to Facility"

        anchors{
            left: parent.left
            leftMargin: Qt.application.font.pixelSize
            
            top: parent.top
            topMargin: Qt.application.font.pixelSize
        }


        Templates.LabelledInput {
            id: electricityPerDay

            label: "Electricity / day"
            units: "kWh"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.excessToFacility.electricityPerDay = electricityPerDay.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.excessToFacility.electricityPerDay

        }

        Templates.LabelledText {
            id: electricityPerYear

            labelText: "Electricity / year"
            units: "kWh"

            text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.excessToFacility.electricityPerYear
        }

    }
}