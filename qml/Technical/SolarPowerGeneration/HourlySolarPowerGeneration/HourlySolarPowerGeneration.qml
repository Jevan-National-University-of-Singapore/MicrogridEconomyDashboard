import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts

import "HourlySolarGeneration"

import "../../../Templates" as Templates


Templates.Page{
    id: root
    
    Templates.SubSection {
        id: subsectionItems

        subsection: "Hourly Solar Power Generation"

        anchors{
            left: parent.left
            leftMargin: Qt.application.font.pixelSize
            
            top: parent.top
            topMargin: Qt.application.font.pixelSize
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
}

