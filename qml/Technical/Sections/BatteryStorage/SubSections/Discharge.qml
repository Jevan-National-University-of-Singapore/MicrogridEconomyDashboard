import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Discharge"

    LabelledText {
        id: powerContinuous

        labelText: "Power (Continuous, 0.75C)"

        text: Scenario.batteryStorage.discharge.powerContinuous
    }

    LabelledText {
        id: powerMax

        labelText: "Power (max, 1C)"

        text: Scenario.batteryStorage.discharge.powerMax
    }

}