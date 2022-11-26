import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Discharge"

    LabelledText {
        id: powerContinuous

        labelText: "Power (Continuous, 0.75C)"
        units: "kW"

        text: Scenario.technical.batteryStorage.discharge.powerContinuous
    }

    LabelledText {
        id: powerMax

        labelText: "Power (max, 1C)"
        units: "kW"

        text: Scenario.technical.batteryStorage.discharge.powerMax
    }

}