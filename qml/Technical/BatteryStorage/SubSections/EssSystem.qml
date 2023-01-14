import QtQuick
import "../../../../Templates"


SubSection {
    id: root

    subsection: "ESS System"

    LabelledInput {
        id: installedCapacity

        label: "Installed Capacity"
        units: "kWh"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.installedCapacity = installedCapacity.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.installedCapacity
    }

    LabelledText {
        id: chargeRate

        labelText: "Charge Rate"
        units: "C-rate"

        text: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.chargeRate
    }

    LabelledText {
        id: maximumPower

        labelText: "Maximum Power"
        units: "kW"

        text: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.maximumPower
    }

    LabelledInput {
        id: operationalTime

        label: "Operational Time"
        units: "%"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.operationalTime = operationalTime.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.operationalTime
    }

    LabelledInput {
        id: socUpperLimit

        label: "SoC upper limit"
        units: "%"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.stateOfChargeUpperLimit = socUpperLimit.inputText
        
        inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.stateOfChargeUpperLimit
    }

    LabelledInput {
        id: socLowerLimit

        label: "SoC lower limit"
        units: "%"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.stateOfChargeLowerLimit = socLowerLimit.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.stateOfChargeLowerLimit
    }

    LabelledText {
        id: depthOfDischarge

        labelText: "Depth of Discharge"
        units: "%"

        text: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.depthOfDischargePercentage
    }

    LabelledInput {
        id: eolCapacity

        label: "EoL capacity"
        units: "%"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.endOfLifeCapacity = eolCapacity.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.endOfLifeCapacity
    }

    LabelledInput {
        id: essNameplateLifeCycle

        label: "ESS Nameplate Lifecycle"
        units: "Cycles"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.essNameplateLifeCycle = essNameplateLifeCycle.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.essNameplateLifecycle
    }

    // Component.onCompleted: {
    //     installedCapacity.inputText = Scenario.batteryStorage.essSystem.installedCapacity
    //     operationalTime.inputText = Scenario.batteryStorage.essSystem.operationalTime
    //     socLowerLimit.inputText = Scenario.batteryStorage.essSystem.stateOfChargeLowerLimit
    //     socUpperLimit.inputText = Scenario.batteryStorage.essSystem.stateOfChargeUpperLimit
    //     eolCapacity.inputText = Scenario.batteryStorage.essSystem.endOfLifeCapacity
    //     essNameplateLifeCycle.inputText = Scenario.batteryStorage.essSystem.essNameplateLifecycle
    // }



}