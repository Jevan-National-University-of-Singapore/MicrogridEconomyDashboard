import QtQuick
import "../../Templates" as Templates

Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "Revenue Items"

        Templates.LabelledText {
            id: requiredFromChargers

            labelText: "Chargers"
            units: "RM"

            text: Scenario.years[Scenario.currentYearIndex].financial.revenue.revenueItems.chargers.toFixed(2)

        }

        Templates.LabelledText {
            id: retailToFacility

            labelText: "Retail to facility"
            units: "RM"

            text: Scenario.years[Scenario.currentYearIndex].financial.revenue.revenueItems.retailToFacility.toFixed(2)

        }

        Templates.LabelledText {
            id: totalRevenue

            labelText: "Total Revenue"
            units: "RM"

            text: Scenario.years[Scenario.currentYearIndex].financial.revenue.revenueItems.totalRevenue.toFixed(2)

        }



    }
}