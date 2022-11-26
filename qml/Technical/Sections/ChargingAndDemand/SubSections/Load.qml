import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Load"

    LabelledText {
        id: requiredEnergyPerUser

        labelText: "Required energy / user"
        units: "kWh"

        text: Scenario.technical.chargingAndDemand.load.requiredEnergyPerUser
    }

    LabelledText {
        id: requiredEnergyPerDay

        labelText: "Required energy / day"
        units: "kWh"

        text: Scenario.technical.chargingAndDemand.load.requiredEnergyPerDay
    }

    LabelledText {
        id: requiredEnergyPerYear

        labelText: "Required energy / year"
        units: "kWh"

        text: Scenario.technical.chargingAndDemand.load.requiredEnergyPerYear
    }

}
