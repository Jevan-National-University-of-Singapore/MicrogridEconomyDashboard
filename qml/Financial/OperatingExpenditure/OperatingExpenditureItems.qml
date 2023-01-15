import QtQuick
import "../../Templates" as Templates

Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "Operating Expenditure Items"

        Templates.LabelledText {
            id: solarPvOAndM

            labelText: "Solar PV O&M"
            units: "RM/year"

            text: Scenario.years[Scenario.currentYearIndex].financial.operatingExpenditure.operatingExpenditureItems.solarPvOAndM
        }

        Templates.LabelledText {
            id: dcChargesOAndM

            labelText: "DC Chargers O&M"
            units: "RM/year"

            text: Scenario.years[Scenario.currentYearIndex].financial.operatingExpenditure.operatingExpenditureItems.dcChargesOAndM
        }

        Templates.LabelledText {
            id: essOAndM

            labelText: "ESS O&M"
            units: "RM/year"

            text: Scenario.years[Scenario.currentYearIndex].financial.operatingExpenditure.operatingExpenditureItems.essOAndM
        }

        Templates.LabelledText {
            id: gridElectricity

            labelText: "Grid electricity"
            units: "RM/year"

            text: Scenario.years[Scenario.currentYearIndex].financial.operatingExpenditure.operatingExpenditureItems.gridElectricity
        }

        Templates.LabelledText {
            id: totalOpex

            labelText: "Total Opex"
            units: "RM/year"

            text: Scenario.years[Scenario.currentYearIndex].financial.operatingExpenditure.operatingExpenditureItems.totalOpex
        }

    

    }
}