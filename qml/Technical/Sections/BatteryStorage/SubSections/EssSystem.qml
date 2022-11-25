import QtQuick
import "../../../../Templates"


SubSection {
    id: root

    subsection: "ESS System"

    LabelledInput {
        id: installedCapacity

        label: "Installed Capacity"

        input.onEditingFinished: Scenario.batteryStorage.essSystem.installedCapacity = installedCapacity.inputText
    }

    LabelledText {
        id: chargeRate

        labelText: "Charge Rate"

        text: Scenario.batteryStorage.essSystem.chargeRate
    }

    LabelledText {
        id: maximumPower

        labelText: "Maximum Power"

        text: Scenario.batteryStorage.essSystem.maximumPower
    }

    LabelledInput {
        id: operationalTime

        label: "Operational Time"

        input.onEditingFinished: Scenario.batteryStorage.essSystem.operationalTime = operationalTime.inputText
    }

    LabelledInput {
        id: socUpperLimit

        label: "SoC upper limit"

        input.onEditingFinished: Scenario.batteryStorage.essSystem.stateOfChargeUpperLimit = socUpperLimit.inputText
    }

    LabelledInput {
        id: socLowerLimit

        label: "SoC lower limit"

        input.onEditingFinished: Scenario.batteryStorage.essSystem.stateOfChargeLowerLimit = socLowerLimit.inputText
    }

    LabelledText {
        id: depthOfDischarge

        labelText: "Depth of Discharge"

        text: Scenario.batteryStorage.essSystem.depthOfDischargePercentage
    }

    LabelledInput {
        id: eolCapacity

        label: "EoL capacity"

        input.onEditingFinished: Scenario.batteryStorage.essSystem.endOfLifeCapacity = eolCapacity.inputText
    }

    LabelledInput {
        id: essNameplateLifeCycle

        label: "ESS Nameplate Lifecycle"

        input.onEditingFinished: Scenario.batteryStorage.essSystem.essNameplateLifeCycle = essNameplateLifeCycle.inputText
    }

    Component.onCompleted: {
        installedCapacity.inputText = Scenario.batteryStorage.essSystem.installedCapacity
        operationalTime.inputText = Scenario.batteryStorage.essSystem.operationalTime
        socLowerLimit.inputText = Scenario.batteryStorage.essSystem.stateOfChargeLowerLimit
        socUpperLimit.inputText = Scenario.batteryStorage.essSystem.stateOfChargeUpperLimit
        eolCapacity.inputText = Scenario.batteryStorage.essSystem.endOfLifeCapacity
        essNameplateLifeCycle.inputText = Scenario.batteryStorage.essSystem.essNameplateLifecycle
    }



}