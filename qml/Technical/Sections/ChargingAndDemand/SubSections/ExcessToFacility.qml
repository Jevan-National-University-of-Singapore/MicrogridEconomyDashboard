import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Excess to Facility"

    LabelledInput {
        id: electricityPerDay

        label: "Electricity / day"
        units: "kWh"

        input.onEditingFinished: Scenario.technical.chargingAndDemand.excessToFacility.electricityPerDay = electricityPerDay.inputText

        inputText: Scenario.technical.chargingAndDemand.excessToFacility.electricityPerDay

    }

    LabelledText {
        id: electricityPerYear

        labelText: "Electricity / year"
        units: "kWh"

        text: Scenario.technical.chargingAndDemand.excessToFacility.electricityPerYear
    }

    // Component.onCompleted: {
    //     electricityPerDay.inputText = Scenario.chargingAndDemand.excessToFacility.electricityPerDay
    // }

}