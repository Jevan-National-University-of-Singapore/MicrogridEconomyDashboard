import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Installed Capacity"

    LabelledInput {
        id: installedCapacity

        label: "Installed Capacity"
        units: "kWp"

        input.onEditingFinished: Scenario.technical.solarPowerGeneration.installedCapacity.installedCapacity = installedCapacity.inputText

        inputText: Scenario.technical.solarPowerGeneration.installedCapacity.installedCapacity
    }

}