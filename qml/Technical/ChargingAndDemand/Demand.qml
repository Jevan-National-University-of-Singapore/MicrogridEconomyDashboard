import QtQuick
import "../../Templates" as Templates

Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "Demand"

        anchors{
            left: parent.left
            leftMargin: Qt.application.font.pixelSize
            
            top: parent.top
            topMargin: Qt.application.font.pixelSize
        }



        Templates.LabelledInput {
            id: numberOfUsersPerDay

            label: "Number of Users / day"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.numberOfUsersPerDay = parseInt(numberOfUsersPerDay.inputText)

            inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.numberOfUsersPerDay
        }

        Templates.LabelledText {
            id: numberOfUsersPerYear

            labelText: "Number of Users / year"

            text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.numberOfUsersPerYear
        }

        Templates.LabelledInput {
            id: socAtEntry

            label: "SoC at entry"
            units: "%"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.stateOfChargeAtEntry = parseFloat(socAtEntry.inputText)/100

            inputText: (Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.stateOfChargeAtEntry*100).toFixed(2)

        }

        Templates.LabelledInput {
            id: socLimit

            label: "SoC limit"
            units: "%"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.stateOfChargeLimit = parseFloat(socLimit.inputText)/100

            inputText: (Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.stateOfChargeLimit*100).toFixed(2)

        }

        Templates.LabelledText {
            id: socToBeCharged

            labelText: "SoC to be charged"
            units: "%"

            text: (Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.stateOfChargeToBeCharged*100).toFixed(2)
        }

        Templates.LabelledText {
            id: totalWaitingTime

            labelText: "Total waiting time"
            units: "hr"

            text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.totalWaitingTime.toFixed(2)

        }

        Templates.LabelledText {
            id: actualUsersServed

            labelText: "Actual users served / day"

            text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.actualUsersServedPerDay

        }

        Templates.LabelledText {
            id: actualEnergyServed

            labelText: "Actual energy served / day"
            units: "kWh"

            text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.actualEnergyServedPerDay.toFixed(2)
        }

    }
}
