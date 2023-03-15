import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    visible: row === 3 && column !== 0

    text: visible? Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.hourlySolarPowerGeneration.estimatedKwhGenerated[column - 1].toFixed(2) : ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter
}