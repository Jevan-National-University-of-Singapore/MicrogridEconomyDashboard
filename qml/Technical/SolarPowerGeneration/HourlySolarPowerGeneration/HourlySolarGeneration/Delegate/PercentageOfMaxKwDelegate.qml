import QtQuick
import QtQuick.Controls.Material

TextField {
    id: root

    visible: row === 1 && column !== 0
    
    text: visible? (Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.hourlySolarPowerGeneration.percentageOfMaxKw[column - 1]*100).toFixed(2) : ""

    // onEditingFinished: Scenario.solarPowerGeneration.percentageOfMaxKw[column - 1] = parseFloat(root.text)

    onEditingFinished: {
        Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.hourlySolarPowerGeneration.setPercentageOfMaxKwElement(column - 1, parseFloat(root.text)/100)
    }

}