import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Grid Charging"


    LabelledText {
        id: actualEssLifecycle

        labelText: "Actual ESS Lifecycle"
        units: "Cycles"

        text: Scenario.financial.capitalExpenditure.depreciation.actualEssLifecycle
    }

    LabelledText {
        id: essCapexPerKwh

        labelText: "ESS Capex/kWh"
        units: "RM/kWh"

        text: Scenario.financial.capitalExpenditure.depreciation.essCapexPerKwh
    }

    LabelledText {
        id: essDepreciation

        labelText: "ESS Depreciation"
        units: "RM/kWh"

        text: Scenario.financial.capitalExpenditure.depreciation.essDepreciation
    }    

    LabelledText {
        id: chargerLifecycleCapacity

        labelText: "Charger Lifecycle Capacity"
        units: "kWh"

        text: Scenario.financial.capitalExpenditure.depreciation.chargerLifecycleCapacity
    }

    LabelledText {
        id: chargerCapexPerKw

        labelText: "Charger Capex/kW"
        units: "RM/kW"

        text: Scenario.financial.capitalExpenditure.depreciation.chargerCapexPerKw
    }

    LabelledText {
        id: chargerDepreciation

        labelText: "Charger Depreciation"
        units: "RM/kWh"

        text: Scenario.financial.capitalExpenditure.depreciation.chargerDepreciation
    }       



}