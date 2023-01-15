import QtQuick
import "../../Templates" as Templates


Templates.Page{
    id: root
        
    Templates.SubSection {
        id: subsectionItems

        subsection: "Grid Charging"

        anchors{
            left: parent.left
            leftMargin: Qt.application.font.pixelSize
            
            top: parent.top
            topMargin: Qt.application.font.pixelSize
        }        

        Templates.LabelledInput {
            id: offPeakElectricityRequired

            label: "Off-peak electricity required / day"
            units: "kWh"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.offPeakElectricityRequired = offPeakElectricityRequired.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.offPeakElectricityRequired
        }

        Templates.LabelledInput {
            id: peakElectricityChargedFromGrid

            label: "Peak electricity charged from grid / day"
            units: "kWh"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.peakElectricityChargedFromGrid = peakElectricityChargedFromGrid.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.peakElectricityChargedFromGrid
        }

        Templates.LabelledText {
            id: gridElectricityRequired

            labelText: "Grid electricity required / day"
            units: "kWh"

            text: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.gridElectricityRequired
        }

        Templates.LabelledInput {
            id: gridDrawLimit

            label: "Grid draw limit / day"
            units: "kWh"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.gridDrawLimit = gridDrawLimit.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.gridDrawLimit
        }

    }
}