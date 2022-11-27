import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Per Annum"


    LabelledText {
        id: chargingRevenueRequired

        labelText: "Charging revenue required"
        units: "RM in 1st year"

        text: Scenario.financial.revenue.perAnnum.chargingRevenueRequired
    }


    LabelledText {
        id: priceToEvChargers

        labelText: "Price to EV chargers"
        units: "RM/kWh"

        text: Scenario.financial.revenue.perAnnum.priceToEvChargers
    }


}
