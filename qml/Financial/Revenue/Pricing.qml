import QtQuick
import "../../Templates" as Templates

Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "Pricing"

        // Templates.LabelledText {
        //     id: breakevenPriceToEvChargers

        //     labelText: "Breakeven Price to EV chargers"
        //     units: "RM/kWh"

        //     text: Scenario.years[Scenario.currentYearIndex].financial.revenue.pricing.breakevenPriceToEvChargers
        // }


        Templates.LabelledText {
            id: priceToEvChargers

            labelText: "Price to EV chargers"
            units: "RM/kWh"

            text: Scenario.years[Scenario.currentYearIndex].financial.revenue.pricing.priceToEvChargers.toFixed(2)
        }

    }
}