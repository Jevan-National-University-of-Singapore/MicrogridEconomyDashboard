import QtQuick
import "../../../../Templates"


SubSection {
    id: root

    subsection: "Ayer Keroh Site Conditions"

    LabelledInput {
        id: specificPvPowerOutputPerDay

        label: "RM/USD"
        units: "RM"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.ayerKerohSiteConditions.specificPvPowerOutputPerDay = specificPvPowerOutputPerDay.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.ayerKerohSiteConditions.specificPvPowerOutputPerDay
    }

    LabelledText {
        id: specificPvPowerOutputPerYear

        labelText: "Actual ESS Lifecycle"
        units: "Cycles"

        text: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.ayerKerohSiteConditions.specificPvPowerOutputPerYear
    }
}