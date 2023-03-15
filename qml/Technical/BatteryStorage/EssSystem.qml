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

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.installedCapacity = parseFloat(installedCapacity.inputText)

            inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.installedCapacity.toFixed(2)
        }

        Templates.LabelledText {
            id: chargeRate

            labelText: "Charge Rate"
            units: "C-rate"

            text: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.chargeRate.toFixed(2)
        }

        Templates.LabelledText {
            id: maximumPower

            labelText: "Maximum Power"
            units: "kW"

            text: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.maximumPower.toFixed(2)
        }

        Templates.LabelledInput {
            id: operationalTime

            label: "Operational Time"
            units: "%"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.operationalTime = parseFloat(operationalTime.inputText)/100

            inputText: (Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.operationalTime*100).toFixed(2)
        }

        Templates.LabelledInput {
            id: socUpperLimit

            label: "SoC upper limit"
            units: "%"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.stateOfChargeUpperLimit = parseFloat(socUpperLimit.inputText)/100
            
            inputText: (Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.stateOfChargeUpperLimit*100).toFixed(2)
        }

        Templates.LabelledInput {
            id: socLowerLimit

            label: "SoC lower limit"
            units: "%"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.stateOfChargeLowerLimit = parseFloat(socLowerLimit.inputText)/100

            inputText: (Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.stateOfChargeLowerLimit*100).toFixed(2)
        }

        Templates.LabelledText {
            id: depthOfDischarge

            labelText: "Depth of Discharge"
            units: "%"

            text: (Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.depthOfDischargePercentage*100).toFixed(2)
        }

        Templates.LabelledInput {
            id: eolCapacity

            label: "EoL capacity"
            units: "%"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.endOfLifeCapacity = parseFloat(eolCapacity.inputText)/100

            inputText: (Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.endOfLifeCapacity*100).toFixed(2)
        }

        Templates.LabelledInput {
            id: essNameplateLifeCycle

            label: "ESS Nameplate Lifecycle"
            units: "Cycles"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.essNameplateLifeCycle = parseFloat(essNameplateLifeCycle.inputText)

            inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.essSystem.essNameplateLifecycle.toFixed(2)
        }


    }
}