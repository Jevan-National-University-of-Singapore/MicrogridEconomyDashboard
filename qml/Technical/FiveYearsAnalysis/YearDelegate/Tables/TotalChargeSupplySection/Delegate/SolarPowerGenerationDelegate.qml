import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    property int currentYear: 0

    visible: row === 0 && column !== 0
    
    text: visible? Scenario.technical.fiveYearsAnalysis.years[currentYear].totalChargeSupplySection.solarPowerGeneration[column -1] : ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter

}