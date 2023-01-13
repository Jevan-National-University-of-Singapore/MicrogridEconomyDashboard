import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Grid Charging"

    LabelledInput {
        id: offPeakElectricityRequired

        label: "Off-peak electricity required / day"
        units: "kWh"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.offPeakElectricityRequired = offPeakElectricityRequired.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.offPeakElectricityRequired
    }

    LabelledInput {
        id: peakElectricityChargedFromGrid

        label: "Peak electricity charged from grid / day"
        units: "kWh"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.peakElectricityChargedFromGrid = peakElectricityChargedFromGrid.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.peakElectricityChargedFromGrid
    }

    LabelledText {
        id: gridElectricityRequired

        labelText: "Grid electricity required / day"
        units: "kWh"

        text: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.gridElectricityRequired
    }

    LabelledInput {
        id: gridDrawLimit

        label: "Grid draw limit / day"
        units: "kWh"

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.gridDrawLimit = gridDrawLimit.inputText

        inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.gridDrawLimit
    }


    // Component.onCompleted: {
    //     offPeakElectricityRequired.inputText = Scenario.batteryStorage.gridCharging.offPeakElectricityRequired
    //     peakElectricityChargedFromGrid.inputText = Scenario.batteryStorage.gridCharging.peakElectricityChargedFromGrid
    //     gridDrawLimit.inputText = Scenario.batteryStorage.gridCharging.gridDrawLimit
    // }


}