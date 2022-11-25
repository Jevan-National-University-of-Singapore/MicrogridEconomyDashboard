import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Grid Charging"

    LabelledInput {
        id: offPeakElectricityRequired

        label: "Off-peak electricity required"

        input.onEditingFinished: Scenario.batteryStorage.gridCharging.offPeakElectricityRequired = offPeakElectricityRequired.inputText
    }

    LabelledInput {
        id: peakElectricityChargedFromGrid

        label: "Peak electricity charged from grid"

        input.onEditingFinished: Scenario.batteryStorage.gridCharging.peakElectricityChargedFromGrid = peakElectricityChargedFromGrid.inputText
    }

    LabelledText {
        id: gridElectricityRequired

        labelText: "Grid electricity required / day"

        text: Scenario.batteryStorage.gridCharging.gridElectricityRequired
    }

    LabelledInput {
        id: gridDrawLimit

        label: "Grid draw limit"

        input.onEditingFinished: Scenario.batteryStorage.gridCharging.gridDrawLimit = gridDrawLimit.inputText
    }


    Component.onCompleted: {
        offPeakElectricityRequired.inputText = Scenario.batteryStorage.gridCharging.offPeakElectricityRequired
        peakElectricityChargedFromGrid.inputText = Scenario.batteryStorage.gridCharging.peakElectricityChargedFromGrid
        gridDrawLimit.inputText = Scenario.batteryStorage.gridCharging.gridDrawLimit
    }


}