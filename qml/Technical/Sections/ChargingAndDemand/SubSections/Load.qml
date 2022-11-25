import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Load"

    LabelledText {
        id: requiredEnergyPerUser

        labelText: "Required energy / user"

        text: Scenario.chargingAndDemand.load.requiredEnergyPerUser
    }

    LabelledText {
        id: requiredEnergyPerDay

        labelText: "Required energy / day"

        text: Scenario.chargingAndDemand.load.requiredEnergyPerDay
    }

    LabelledText {
        id: requiredEnergyPerYear

        labelText: "Required energy / year"

        text: Scenario.chargingAndDemand.load.requiredEnergyPerYear
    }

}
