import QtQuick
import QtQuick.Window
import QtQuick.Controls.Material

import "../../../Templates"


Item {
    id: root

    height: dataColumn.height
    width: dataColumn.width

    property alias totalPercentageOfMaxKw: totalPercentageOfMaxKw
    property alias dailyGeneration: dailyGeneration

    Column {
        id: dataColumn

        LabelledText {
            id: totalPercentageOfMaxKw

            labelText: "Total percentage of max kW"

            text: (Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.hourlySolarPowerGeneration.totalPercentageOfMaxKw * 100).toFixed(2)

        }

        LabelledText {
            id: dailyGeneration

            labelText: "Daily generation (kWh)"

            text: Scenario.years[Scenario.currentYearIndex].technical.solarPowerGeneration.hourlySolarPowerGeneration.dailyGeneration.toFixed(2)

        }

    }


    
    
    

}