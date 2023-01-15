import QtQuick
import "../../Templates" as Templates

Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "Per Annum"


        Templates.LabelledText {
            id: chargingRevenueRequired

            labelText: "Charging revenue required"
            units: "RM in 1st year"

            text: Scenario.years[Scenario.currentYearIndex].financial.revenue.perAnnum.chargingRevenueRequired
        }


        Templates.LabelledText {
            id: priceToEvChargers

            labelText: "Price to EV chargers"
            units: "RM/kWh"

            text: Scenario.years[Scenario.currentYearIndex].financial.revenue.perAnnum.priceToEvChargers
        }


    }
}