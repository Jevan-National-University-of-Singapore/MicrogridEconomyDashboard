import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    property int currentYear: 0

    visible: row === 0 && column !== 0
    
    text: visible? Scenario.years[Scenario.currentYearIndex].technical.hourlyBreakdown.totalChargeSupplySection.solarPowerGeneration[column -1] : ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter

}