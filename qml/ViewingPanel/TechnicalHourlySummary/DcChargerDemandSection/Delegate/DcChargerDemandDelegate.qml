import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    property int currentYear: 0

    visible: row === 0 && column !== 0


    text: visible? Scenario.years[Scenario.currentYearIndex].technical.hourlyBreakdown.dcChargerDemandSection.dcChargerDemand[column -1].toFixed(2) : ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter

}