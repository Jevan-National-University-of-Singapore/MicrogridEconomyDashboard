import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    visible: row === 2 && column !== 0
    
    text: visible? (Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.hourlySolarPowerGeneration.percentageOfDailyKwh[column - 1] * 100).toFixed(2): ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter
}