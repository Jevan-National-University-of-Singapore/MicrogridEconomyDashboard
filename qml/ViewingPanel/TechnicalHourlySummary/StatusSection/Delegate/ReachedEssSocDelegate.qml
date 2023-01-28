import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    visible: row === 3 && column !== 0

    property int currentYear: 0

    text: visible? Scenario.years[Scenario.currentYearIndex].technical.hourlyBreakdown.statusSection.reachedEssStateOfCharge[column -1] : ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter
}