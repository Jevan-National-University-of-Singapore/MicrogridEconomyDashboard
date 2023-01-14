import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Demand"


    LabelledInput {
        id: numberOfUsersPerDay

        label: "Number of Users / day"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.numOfUsersPerDay = numberOfUsersPerDay.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.numOfUsersPerDay
    }

    LabelledText {
        id: numberOfUsersPerYear

        labelText: "Number of Users / year"

        text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.numOfUsersPerYear
    }

    LabelledInput {
        id: socAtEntry

        label: "SoC at entry"
        units: "%"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.stateOfChargeAtEntry = socAtEntry.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.stateOfChargeAtEntry

    }

    LabelledInput {
        id: socLimit

        label: "SoC limit"
        units: "%"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.stateOfChargeLimit = socLimit.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.stateOfChargeLimit

    }

    LabelledText {
        id: socToBeCharged

        labelText: "SoC to be charged"
        units: "%"

        text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.stateOfChargeToBeCharged
    }

    LabelledInput {
        id: totalWaitingTime

        label: "Total waiting time"
        units: "hr"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.totalWaitingTime = totalWaitingTime.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.totalWaitingTime

    }

    LabelledInput {
        id: actualUsersServed

        label: "Actual users served / day"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.actualUsersServedPerDay = actualUsersServed.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.actualUsersServedPerDay

    }

    LabelledText {
        id: actualEnergyServed

        labelText: "Actual energy served / day"
        units: "kWh"

        text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.actualEnergyServedPerDay
    }

    // Component.onCompleted: {
    //     numberOfUsersPerDay.inputText = Scenario.chargingAndDemand.demand.numOfUsersPerDay
    //     socAtEntry.inputText = Scenario.chargingAndDemand.demand.stateOfChargeAtEntry
    //     socLimit.inputText = Scenario.chargingAndDemand.demand.stateOfChargeLimit
    //     totalWaitingTime.inputText = Scenario.chargingAndDemand.demand.totalWaitingTime
    //     actualUsersServed.inputText = Scenario.chargingAndDemand.demand.actualUsersServedPerDay
    // }

}
