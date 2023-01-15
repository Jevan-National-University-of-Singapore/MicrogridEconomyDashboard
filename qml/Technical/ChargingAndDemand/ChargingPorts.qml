import QtQuick
import "../../Templates" as Templates


Templates.Page{
    id: root
    Templates.SubSection {
        id: subsectionItems

        subsection: "ChargingPorts"

        anchors{
            left: parent.left
            leftMargin: Qt.application.font.pixelSize
            
            top: parent.top
            topMargin: Qt.application.font.pixelSize
        }


        Templates.LabelledInput {
            id: dcCharger1Rating

            label: "DC Charger 1 rating"
            units: "kW"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.dcCharger1Rating = dcCharger1Rating.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.dcCharger1Rating

        }

        Templates.LabelledInput {
            id: numOfDcCharger1

            label: "Number of DC Charger 1"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.numOfDcCharger1 = numOfDcCharger1.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.numOfDcCharger1

        }

        Templates.LabelledText {
            id: dc1ChargingTime

            labelText: "DC 1 Charging Time / user"
            units: "hr"

            text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.dc1ChargingTimePerUser

        }

        Templates.LabelledInput {
            id: dcCharger2Rating

            label: "DC Charger 2 rating"
            units: "kW"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.dcCharger2Rating = dcCharger2Rating.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.dcCharger2Rating

        }

        Templates.LabelledInput {
            id: numOfDcCharger2

            label: "Number of DC Charger 2"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.numOfDcCharger2 = numOfDcCharger2.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.numOfDcCharger2

        }

        Templates.LabelledText {
            id: dc2ChargingTime

            labelText: "DC 2 Charging Time / user"
            units: "hr"

            text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.dc2ChargingTimePerUser

        }

    }
}