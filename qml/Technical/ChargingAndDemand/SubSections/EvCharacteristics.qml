import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "EV Characteristics"

    LabelledInput {
        id: evBatteryVoltage

        label: "EV battery voltage"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.evCharacteristics.evBatteryVoltage = evBatteryVoltage.inputText
        units: "V"

        inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.evCharacteristics.evBatteryVoltage

    }

    LabelledInput {
        id: capacity

        label: "Capacity (79.2)"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.evCharacteristics.capacity = capacity.inputText
        units: "kWh"

        inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.evCharacteristics.capacity

    }

    LabelledInput {
        id: maxKwPowerRating

        label: "Max. kW rating"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.evCharacteristics.maxPowerRating = maxKwPowerRating.inputText
        units: "kW"

        inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.evCharacteristics.maxPowerRating

    }

    LabelledText {
        id: ampereHourRating

        labelText: "Ampere-hour rating"
        units: "Ah"

        text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.evCharacteristics.ampereHourRating
    }

    // Component.onCompleted: {
    //     evBatteryVoltage.inputText = Scenario.chargingAndDemand.evCharacteristics.evBatteryVoltage
    //     capacity.inputText = Scenario.chargingAndDemand.evCharacteristics.capacity
    //     maxKwPowerRating.inputText = Scenario.chargingAndDemand.evCharacteristics.maxPowerRating
    // }


}