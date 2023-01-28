import QtQuick

import "../../Templates" as Templates


Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "Solar Energy Production"

        anchors{
            left: parent.left
            leftMargin: Qt.application.font.pixelSize
            
            top: parent.top
            topMargin: Qt.application.font.pixelSize
        }

        Templates.LabelledText {
            id: specificYield

            labelText: "Specific Yield"
            units: "kWh/kWp"

            text: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.solarEnergyProduction.specificYield
        }

        Templates.LabelledInput {
            id: boostInverterEfficiency

            label: "Boost Inverter Efficiency"
            units: "%"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.solarEnergyProduction.boostInverterEfficiency = boostInverterEfficiency.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.solarEnergyProduction.boostInverterEfficiency
        }


        Templates.LabelledText {
            id: estimatedGenerationPerDay

            labelText: "Estimated Generation / day"
            units: "kWh"

            text: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.solarEnergyProduction.estimatedGenerationPerDay
        }

        Templates.LabelledText {
            id: estimatedGenerationPerYear

            labelText: "Estimated Generation / year"
            units: "kWh"

            text: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.solarEnergyProduction.estimatedGenerationPerYear
        }    
    }

}