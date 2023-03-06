import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    property int currentYear: 0

    visible: row === 4 && column !== 0

    text: visible? Scenario.years[Scenario.currentYearIndex].financial.summary.ebitdaSection.ebitda : ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter
}