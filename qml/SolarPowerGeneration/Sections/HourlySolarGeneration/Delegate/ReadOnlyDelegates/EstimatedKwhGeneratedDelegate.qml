import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    visible: row === 3 && column !== 0

    text: visible? Scenario.solarPowerGeneration.estimatedKwhGenerated[column - 1] : ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter
}