import QtQuick
import "../../Templates" as Templates

Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "ESS System"

        anchors{
            left: parent.left
            leftMargin: Qt.application.font.pixelSize
            
            top: parent.top
            topMargin: Qt.application.font.pixelSize
        }        

        Templates.LabelledInput {
            id: installedCapacity

            label: "Installed Capacity"
            units: "kWh"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.installedCapacity = installedCapacity.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.installedCapacity
        }

        Templates.LabelledText {
            id: chargeRate

            labelText: "Charge Rate"
            units: "C-rate"

            text: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.chargeRate
        }

        Templates.LabelledText {
            id: maximumPower

            labelText: "Maximum Power"
            units: "kW"

            text: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.maximumPower
        }

        Templates.LabelledInput {
            id: operationalTime

            label: "Operational Time"
            units: "%"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.operationalTime = operationalTime.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.operationalTime
        }

        Templates.LabelledInput {
            id: socUpperLimit

            label: "SoC upper limit"
            units: "%"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.stateOfChargeUpperLimit = socUpperLimit.inputText
            
            inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.stateOfChargeUpperLimit
        }

        Templates.LabelledInput {
            id: socLowerLimit

            label: "SoC lower limit"
            units: "%"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.stateOfChargeLowerLimit = socLowerLimit.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.stateOfChargeLowerLimit
        }

        Templates.LabelledText {
            id: depthOfDischarge

            labelText: "Depth of Discharge"
            units: "%"

            text: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.depthOfDischargePercentage
        }

        Templates.LabelledInput {
            id: eolCapacity

            label: "EoL capacity"
            units: "%"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.endOfLifeCapacity = eolCapacity.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.endOfLifeCapacity
        }

        Templates.LabelledInput {
            id: essNameplateLifeCycle

            label: "ESS Nameplate Lifecycle"
            units: "Cycles"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.essNameplateLifeCycle = essNameplateLifeCycle.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.essNameplateLifecycle
        }


    }
}