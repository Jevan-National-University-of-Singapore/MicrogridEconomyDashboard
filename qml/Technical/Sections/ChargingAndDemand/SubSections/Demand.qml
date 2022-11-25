import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Demand"

    LabelledInput {
        id: numberOfUsersPerDay

        label: "Number of Users / day"

        input.onEditingFinished: Scenario.chargingAndDemand.demand.numOfUsersPerDay = numberOfUsersPerDay.inputText
    }

    LabelledText {
        id: numberOfUsersPerYear

        labelText: "Number of Users / year"

        text: Scenario.chargingAndDemand.demand.numOfUsersPerYear
    }

    LabelledInput {
        id: socAtEntry

        label: "SoC at entry"

        input.onEditingFinished: Scenario.chargingAndDemand.demand.stateOfChargeAtEntry = socAtEntry.inputText

    }

    LabelledInput {
        id: socLimit

        label: "SoC limit"

        input.onEditingFinished: Scenario.chargingAndDemand.demand.stateOfChargeLimit = socLimit.inputText

    }

    LabelledText {
        id: socToBeCharged

        labelText: "SoC to be charged"

        text: Scenario.chargingAndDemand.demand.stateOfChargeToBeCharged
    }

    LabelledInput {
        id: totalWaitingTime

        label: "Total waiting time"

        input.onEditingFinished: Scenario.chargingAndDemand.demand.totalWaitingTime = totalWaitingTime.inputText

    }

    LabelledInput {
        id: actualUsersServed

        label: "Actual Users served  / day"

        input.onEditingFinished: Scenario.chargingAndDemand.demand.actualUsersServedPerDay = actualUsersServed.inputText

    }

    LabelledText {
        id: actualEnergyServed

        labelText: "Actual energy served / day"

        text: Scenario.chargingAndDemand.demand.actualEnergyServedPerDay
    }

    Component.onCompleted: {
        numberOfUsersPerDay.inputText = Scenario.chargingAndDemand.demand.numOfUsersPerDay
        socAtEntry.inputText = Scenario.chargingAndDemand.demand.stateOfChargeAtEntry
        socLimit.inputText = Scenario.chargingAndDemand.demand.stateOfChargeLimit
        totalWaitingTime.inputText = Scenario.chargingAndDemand.demand.totalWaitingTime
        actualUsersServed.inputText = Scenario.chargingAndDemand.demand.actualUsersServedPerDay
    }

}
