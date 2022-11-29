import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Solar Energy Production"

    LabelledText {
        id: specificYield

        labelText: "Specific Yield"
        units: "kWh/kWp"

        text: Scenario.solarPowerGeneration.solarEnergyProduction.specificYield
    }

    LabelledInput {
        id: boostInverterEfficiency

        label: "Boost Inverter Efficiency"
        units: "%"

        input.onEditingFinished: Scenario.solarPowerGeneration.solarEnergyProduction.boostInverterEfficiency = boostInverterEfficiency.inputText

        inputText: Scenario.solarPowerGeneration.solarEnergyProduction.boostInverterEfficiency
    }


    LabelledText {
        id: estimatedGenerationPerDay

        labelText: "Estimated Generation / day"
        units: "kWh"

        text: Scenario.solarPowerGeneration.solarEnergyProduction.estimatedGenerationPerDay
    }

    LabelledText {
        id: estimatedGenerationPerYear

        labelText: "Estimated Generation / year"
        units: "kWh"

        text: Scenario.solarPowerGeneration.solarEnergyProduction.estimatedGenerationPerYear
    }    

}