import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Operating Expenditure Items"

    LabelledText {
        id: solarPvOAndM

        labelText: "Solar PV O&M"
        units: "RM/year"

        text: Scenario.financial.operatingExpenditure.operatingExpenditureItems.solarPvOAndM
    }

    LabelledText {
        id: dcChargesOAndM

        labelText: "DC Chargers O&M"
        units: "RM/year"

        text: Scenario.financial.operatingExpenditure.operatingExpenditureItems.dcChargesOAndM
    }

    LabelledText {
        id: essOAndM

        labelText: "ESS O&M"
        units: "RM/year"

        text: Scenario.financial.operatingExpenditure.operatingExpenditureItems.essOAndM
    }

    LabelledText {
        id: gridElectricity

        labelText: "Grid electricity"
        units: "RM/year"

        text: Scenario.financial.operatingExpenditure.operatingExpenditureItems.gridElectricity
    }

    LabelledText {
        id: totalOpex

        labelText: "Total Opex"
        units: "RM/year"

        text: Scenario.financial.operatingExpenditure.operatingExpenditureItems.totalOpex
    }

   

}