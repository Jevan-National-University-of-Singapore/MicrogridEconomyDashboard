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

            text: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.depreciation.actualEssLifecycle.toFixed(2)
        }

        Templates.LabelledText {
            id: essCapexPerKwh

            labelText: "ESS Capex/kWh"
            units: "RM/kWh"

            text: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.depreciation.essCapexPerKwh.toFixed(2)
        }

        Templates.LabelledText {
            id: essDepreciation

            labelText: "ESS Depreciation"
            units: "RM/kWh"

            text: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.depreciation.essDepreciation.toFixed(2)
        }    

        Templates.LabelledText {
            id: chargerLifecycleCapacity

            labelText: "Charger Lifecycle Capacity"
            units: "kWh"

            text: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.depreciation.chargerLifecycleCapacity.toFixed(2)
        }

        Templates.LabelledText {
            id: chargerCapexPerKw

            labelText: "Charger Capex/kW"
            units: "RM/kW"

            text: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.depreciation.chargerCapexPerKw.toFixed(2)
        }

        Templates.LabelledText {
            id: chargerDepreciation

            labelText: "Charger Depreciation"
            units: "RM/kWh"

            text: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.depreciation.chargerDepreciation.toFixed(2)
        }       



    }
}