import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "ChargingPorts"

    LabelledInput {
        id: dcCharger1Rating

        label: "DC Charger 1 rating"
        units: "kW"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.dcCharger1Rating = dcCharger1Rating.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.dcCharger1Rating

    }

    LabelledInput {
        id: numOfDcCharger1

        label: "Number of DC Charger 1"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.numOfDcCharger1 = numOfDcCharger1.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.numOfDcCharger1

    }

    LabelledText {
        id: dc1ChargingTime

        labelText: "DC 1 Charging Time / user"
        units: "hr"

        text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.dc1ChargingTimePerUser

    }

    LabelledInput {
        id: dcCharger2Rating

        label: "DC Charger 2 rating"
        units: "kW"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.dcCharger2Rating = dcCharger2Rating.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.dcCharger2Rating

    }

    LabelledInput {
        id: numOfDcCharger2

        label: "Number of DC Charger 2"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.numOfDcCharger2 = numOfDcCharger2.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.numOfDcCharger2

    }

    LabelledText {
        id: dc2ChargingTime

        labelText: "DC 2 Charging Time / user"
        units: "hr"

        text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.chargingPorts.dc2ChargingTimePerUser

    }

    // Component.onCompleted: {
    //     dcCharger1Rating.inputText = Scenario.chargingAndDemand.chargingPorts.dcCharger1Rating
    //     numOfDcCharger1.inputText = Scenario.chargingAndDemand.chargingPorts.numOfDcCharger1
    //     dcCharger2Rating.inputText = Scenario.chargingAndDemand.chargingPorts.dcCharger2Rating
    //     numOfDcCharger2.inputText = Scenario.chargingAndDemand.chargingPorts.numOfDcCharger2
    // }


}