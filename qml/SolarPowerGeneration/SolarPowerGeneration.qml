import QtQuick
import QtQuick.Controls.Material

import "Sections/HourlySolarGeneration"
import "Sections/DailySolarGeneration"


ScrollView {
    id: root

    HourlySolarGeneration{
        id: hourlySolarGeneration

        anchors.centerIn: parent
    }

    DailySolarGeneration {
        id: dailySolarGeneration

        anchors {
            top: hourlySolarGeneration.bottom
            topMargin: dailySolarGeneration.dailyGeneration.spacing

            left: hourlySolarGeneration.left
        }
    }
    
}