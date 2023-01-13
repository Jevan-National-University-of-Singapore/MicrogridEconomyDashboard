import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Solar Energy Production"

    LabelledText {
        id: specificYield

        labelText: "Specific Yield"
        units: "kWh/kWp"

        text: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.solarEnergyProduction.specificYield
    }

    LabelledInput {
        id: boostInverterEfficiency

        label: "Boost Inverter Efficiency"
        units: "%"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.solarEnergyProduction.boostInverterEfficiency = boostInverterEfficiency.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.solarEnergyProduction.boostInverterEfficiency
    }


    LabelledText {
        id: estimatedGenerationPerDay

        labelText: "Estimated Generation / day"
        units: "kWh"

        text: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.solarEnergyProduction.estimatedGenerationPerDay
    }

    LabelledText {
        id: estimatedGenerationPerYear

        labelText: "Estimated Generation / year"
        units: "kWh"

        text: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.solarEnergyProduction.estimatedGenerationPerYear
    }    

}