import "../../../../Templates"


SubSection {
    id: root

    subsection: "Discharge"

    LabelledInput {
        id: installedCapacity

        label: "Power (Continuous, 0.75C)"
    }

    LabelledInput {
        id: chargeRate

        label: "Power (max, 1C)"
    }

}