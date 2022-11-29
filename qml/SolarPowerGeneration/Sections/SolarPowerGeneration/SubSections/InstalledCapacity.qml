import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Installed Capacity"

    LabelledInput {
        id: installedCapacity

        label: "Installed Capacity"
        units: "kWp"

        input.onEditingFinished: Scenario.solarPowerGeneration.installedCapacity.installedCapacity = installedCapacity.inputText

        inputText: Scenario.solarPowerGeneration.installedCapacity.installedCapacity
    }

}