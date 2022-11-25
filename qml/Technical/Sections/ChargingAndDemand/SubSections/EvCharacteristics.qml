import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "EV Characteristics"

    LabelledInput {
        id: evBatteryVoltage

        label: "EV battery voltage"

        input.onEditingFinished: Scenario.chargingAndDemand.evCharacteristics.evBatteryVoltage = evBatteryVoltage.inputText

    }

    LabelledInput {
        id: capacity

        label: "Capacity (79.2)"

        input.onEditingFinished: Scenario.chargingAndDemand.evCharacteristics.capacity = capacity.inputText

    }

    LabelledInput {
        id: maxKwPowerRating

        label: "Max. kW rating"

        input.onEditingFinished: Scenario.chargingAndDemand.evCharacteristics.maxPowerRating = maxKwPowerRating.inputText

    }

    LabelledText {
        id: ampereHourRating

        labelText: "Ampere-hour rating"

        text: Scenario.chargingAndDemand.evCharacteristics.ampereHourRating
    }

    Component.onCompleted: {
        evBatteryVoltage.inputText = Scenario.chargingAndDemand.evCharacteristics.evBatteryVoltage
        capacity.inputText = Scenario.chargingAndDemand.evCharacteristics.capacity
        maxKwPowerRating.inputText = Scenario.chargingAndDemand.evCharacteristics.maxPowerRating
    }


}