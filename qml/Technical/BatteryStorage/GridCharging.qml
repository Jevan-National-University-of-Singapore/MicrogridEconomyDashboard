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

        Templates.LabelledText {
            id: offPeakElectricityRequired

            labelText: "Off-peak electricity required / day"
            units: "kWh"

            text: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.offPeakElectricityRequired.toFixed(2)
        }

        Templates.LabelledText {
            id: peakElectricityChargedFromGrid

            labelText: "Peak electricity charged from grid / day"
            units: "kWh"

            text: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.peakElectricityChargedFromGrid.toFixed(2)
        }

        Templates.LabelledText {
            id: gridElectricityRequired

            labelText: "Grid electricity required / day"
            units: "kWh"

            text: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.gridElectricityRequired.toFixed(2)
        }

        Templates.LabelledInput {
            id: gridDrawLimit

            label: "Grid draw limit / day"
            units: "kWh"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.gridDrawLimit = parseFloat(gridDrawLimit.inputText)

            inputText: Scenario.years[Scenario.currentYearIndex].technical.batteryStorage.gridCharging.gridDrawLimit.toFixed(2)
        }

    }
}