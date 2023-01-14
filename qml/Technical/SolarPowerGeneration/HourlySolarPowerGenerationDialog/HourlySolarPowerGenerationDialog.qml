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

    visible: opacity


    Behavior on opacity { SmoothedAnimation { velocity: 2.5 } }

    defaultData: MouseArea{
        id: touchHandler

        visible: root.opacity
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