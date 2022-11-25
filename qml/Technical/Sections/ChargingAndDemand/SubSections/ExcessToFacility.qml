import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Excess to Facility"

    LabelledInput {
        id: electricityPerDay

        label: "Electricity / day"

        input.onEditingFinished: Scenario.chargingAndDemand.excessToFacility.electricityPerDay = electricityPerDay.inputText

    }

    LabelledText {
        id: electricityPerYear

        labelText: "Electricity / year"

        text: Scenario.chargingAndDemand.excessToFacility.electricityPerYear
    }

    Component.onCompleted: {
        electricityPerDay.inputText = Scenario.chargingAndDemand.excessToFacility.electricityPerDay
    }

}