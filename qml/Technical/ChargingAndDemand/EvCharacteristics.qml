import QtQuick
import "../../Templates" as Templates

Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "EV Characteristics"

        anchors{
            left: parent.left
            leftMargin: Qt.application.font.pixelSize
            
            top: parent.top
            topMargin: Qt.application.font.pixelSize
        }


        Templates.LabelledInput {
            id: evBatteryVoltage

            label: "EV battery voltage"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.evCharacteristics.evBatteryVoltage = parseFloat(evBatteryVoltage.inputText)
            units: "V"

            inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.evCharacteristics.evBatteryVoltage.toFixed(2)

        }

        Templates.LabelledInput {
            id: capacity

            label: "Capacity (79.2)"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.evCharacteristics.capacity = parseFloat(capacity.inputText)
            units: "kWh"

            inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.evCharacteristics.capacity.toFixed(2)

        }

        Templates.LabelledInput {
            id: maxKwPowerRating

            label: "Max. kW rating"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.evCharacteristics.maxPowerRating = parseFloat(maxKwPowerRating.inputText)
            units: "kW"

            inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.evCharacteristics.maxPowerRating.toFixed(2)

        }

        Templates.LabelledText {
            id: ampereHourRating

            labelText: "Ampere-hour rating"
            units: "Ah"

            text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.evCharacteristics.ampereHourRating.toFixed(2)
        }

    }
}