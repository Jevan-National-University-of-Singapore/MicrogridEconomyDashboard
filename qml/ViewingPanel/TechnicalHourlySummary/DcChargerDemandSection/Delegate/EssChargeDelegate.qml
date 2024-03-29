import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    visible: row === 2 && column !== 0

    property int currentYear: 0

    text: visible? Scenario.years[Scenario.currentYearIndex].technical.hourlyBreakdown.dcChargerDemandSection.essCharge[column -1].toFixed(2) : ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter
}