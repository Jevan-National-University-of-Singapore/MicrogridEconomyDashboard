import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    property int currentYear: 0

    visible: row === 1 && column !== 0

    text: visible? Scenario.years[Scenario.currentYearIndex].financial.summary.discountedCashFlowsSection.presentValueOfCashFlow.toFixed(2) : ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter
}