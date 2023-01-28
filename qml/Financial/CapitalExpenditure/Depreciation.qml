import QtQuick
import "../../Templates" as Templates



Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "Depreciation"


        Templates.LabelledText {
            id: actualEssLifecycle

            labelText: "Actual ESS Lifecycle"
            units: "Cycles"

            text: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.depreciation.actualEssLifecycle
        }

        Templates.LabelledText {
            id: essCapexPerKwh

            labelText: "ESS Capex/kWh"
            units: "RM/kWh"

            text: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.depreciation.essCapexPerKwh
        }

        Templates.LabelledText {
            id: essDepreciation

            labelText: "ESS Depreciation"
            units: "RM/kWh"

            text: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.depreciation.essDepreciation
        }    

        Templates.LabelledText {
            id: chargerLifecycleCapacity

            labelText: "Charger Lifecycle Capacity"
            units: "kWh"

            text: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.depreciation.chargerLifecycleCapacity
        }

        Templates.LabelledText {
            id: chargerCapexPerKw

            labelText: "Charger Capex/kW"
            units: "RM/kW"

            text: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.depreciation.chargerCapexPerKw
        }

        Templates.LabelledText {
            id: chargerDepreciation

            labelText: "Charger Depreciation"
            units: "RM/kWh"

            text: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.depreciation.chargerDepreciation
        }       



    }
}