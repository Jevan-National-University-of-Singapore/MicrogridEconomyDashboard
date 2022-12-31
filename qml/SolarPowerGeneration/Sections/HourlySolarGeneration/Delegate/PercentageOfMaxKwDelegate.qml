import QtQuick
import QtQuick.Controls.Material

TextField {
    id: root

    visible: row === 1 && column !== 0
    
    text: visible? Scenario.solarPowerGeneration.percentageOfMaxKw[column - 1] : ""

    // onEditingFinished: Scenario.solarPowerGeneration.percentageOfMaxKw[column - 1] = parseFloat(root.text)

    onEditingFinished: {
        Scenario.solarPowerGeneration.setPercentageOfMaxKwElement(column - 1, parseFloat(root.text))
    }

}