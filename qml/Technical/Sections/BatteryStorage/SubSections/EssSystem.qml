import "../../../../Templates"


SubSection {
    id: root

    subsection: "ESS System"

    LabelledInput {
        id: installedCapacity

        label: "Installed Capacity"
    }

    LabelledInput {
        id: chargeRate

        label: "Charge Rate"
    }

    LabelledInput {
        id: maximumPower

        label: "Maximum Power"
    }

    LabelledInput {
        id: operationalTime

        label: "Operational Time"
    }

    LabelledInput {
        id: socUpperLimit

        label: "SoC upper limit"
    }

    LabelledInput {
        id: socLowerLimit

        label: "SoC lower limit"
    }

    LabelledInput {
        id: depthOfDischarge

        label: "Depth of Discharge"
    }

    LabelledInput {
        id: eolCapacity

        label: "EoL capacity"
    }

    LabelledInput {
        id: essNameplateLifeCycle

        label: "ESS Nameplate Lifecycle"
    }



}