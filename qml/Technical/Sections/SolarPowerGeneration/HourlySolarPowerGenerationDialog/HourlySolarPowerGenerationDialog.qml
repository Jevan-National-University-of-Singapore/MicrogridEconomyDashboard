import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts

import "Sections/HourlySolarGeneration"
import "Sections/DailySolarGeneration"

import "../../../../Templates"



Section {
    id: root

    section: "Hourly Solar Power Generation"

    function show(){
        opacity = 1
    }

    function close(){
        opacity = 0
    }


    Behavior on opacity { SmoothedAnimation { velocity: 2.5 } }
    defaultData: MouseArea{
        enabled: opacity
        anchors.fill: parent
    }

    HourlySolarGeneration{
        id: hourlySolarGeneration

    }

    DailySolarGeneration {
        id: dailySolarGeneration

        anchors {
            top: hourlySolarGeneration.bottom
        }
    }
    



    
}