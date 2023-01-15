import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "5-year Lifetime"

    LabelledText {
        id: requiredFromChargers

        labelText: "Required from chargers"
        units: "RM"

        text: Scenario.financial.revenue.fiveYearLifetime.requiredFromChargers

    }

    LabelledText {
        id: retailToFacility

        labelText: "Retail to facility"
        units: "RM"

        text: Scenario.financial.revenue.fiveYearLifetime.retailToFacility

    }

    LabelledText {
        id: revenueRequiredToBreakEven

        labelText: "Revenue required to break-even"
        units: "RM"

        text: Scenario.financial.revenue.fiveYearLifetime.revenueRequiredToBreakEven

    }



}