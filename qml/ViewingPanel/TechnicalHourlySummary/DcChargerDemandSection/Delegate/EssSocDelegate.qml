import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    visible: row === 3 && column !== 0

    property int currentYear: 0

    text: visible? (Scenario.years[Scenario.currentYearIndex].technical.hourlyBreakdown.dcChargerDemandSection.essStateOfCharge[column -1]*100).toFixed(2) : ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter

}