import QtQuick
import "../../Templates" as Templates

Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "5-year Lifetime"

        Templates.LabelledText {
            id: requiredFromChargers

            labelText: "Required from chargers"
            units: "RM"

            text: Scenario.years[Scenario.currentYearIndex].financial.revenue.fiveYearLifetime.requiredFromChargers

        }

        Templates.LabelledText {
            id: retailToFacility

            labelText: "Retail to facility"
            units: "RM"

            text: Scenario.years[Scenario.currentYearIndex].financial.revenue.fiveYearLifetime.retailToFacility

        }

        Templates.LabelledText {
            id: revenueRequiredToBreakEven

            labelText: "Revenue required to break-even"
            units: "RM"

            text: Scenario.years[Scenario.currentYearIndex].financial.revenue.fiveYearLifetime.revenueRequiredToBreakEven

        }



    }
}