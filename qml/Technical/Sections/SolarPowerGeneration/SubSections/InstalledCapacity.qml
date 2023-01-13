import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Installed Capacity"

    LabelledInput {
        id: installedCapacity

        label: "Installed Capacity"
        units: "kWp"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.installedCapacity.installedCapacity = installedCapacity.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.installedCapacity.installedCapacity
    }

}