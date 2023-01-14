import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    visible: row === 1 && column !== 0

    property int currentYear: 0

    text: visible? Scenario.technical.fiveYearsAnalysis.years[currentYear].dcChargerDemandSection.loadOnEss[column -1] : ""

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter
}