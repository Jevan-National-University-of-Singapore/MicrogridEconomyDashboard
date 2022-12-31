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

            text: Scenario.solarPowerGeneration.totalPercentageOfMaxKw

        }

        LabelledText {
            id: dailyGeneration

            labelText: "Daily generation (kWh)"

            text: Scenario.solarPowerGeneration.dailyGeneration

        }

    }


    
    
    

}