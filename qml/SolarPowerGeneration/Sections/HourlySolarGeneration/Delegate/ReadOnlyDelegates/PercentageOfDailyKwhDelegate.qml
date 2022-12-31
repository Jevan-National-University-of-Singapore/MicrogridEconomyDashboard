import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    visible: row === 2 && column !== 0
    
    text: visible? Scenario.solarPowerGeneration.percentageOfDailyKwh[column - 1] : ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter
}