import QtQuick
import "../../../../Templates"


SubSection {
    id: root

    subsection: "Ayer Keroh Site Conditions"

    LabelledInput {
        id: specificPvPowerOutputPerDay

        label: "RM/USD"
        units: "RM"

        input.onEditingFinished: Scenario.solarPowerGeneration.ayerKerohSiteConditions.specificPvPowerOutputPerDay = specificPvPowerOutputPerDay.inputText

        inputText: Scenario.solarPowerGeneration.ayerKerohSiteConditions.specificPvPowerOutputPerDay
    }

    LabelledText {
        id: specificPvPowerOutputPerYear

        labelText: "Actual ESS Lifecycle"
        units: "Cycles"

        text: Scenario.solarPowerGeneration.ayerKerohSiteConditions.specificPvPowerOutputPerYear
    }
}