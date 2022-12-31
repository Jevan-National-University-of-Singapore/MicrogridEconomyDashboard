import QtQuick
import QtQuick.Controls.Material

import "ReadOnlyDelegates"

Item {
    id: delegate

    // property int row
    // property int column

    implicitWidth: column === 0? headerDelegate.implicitWidth:
        row===0? headerDelegate.header.font.pixelSize * 5://hourDelegate.implicitWidth+hourDelegate.font.pixelSize :
        row === 1? headerDelegate.header.font.pixelSize * 5 : 10
    

    // implicitHeight: column === 0? headerDelegate.implicitHeight:
    //     row===0? hourDelegate.implicitHeight*1.2 :
    //     row === 1? percentageOfMaxKwDelegate.implicitHeight : 10

    implicitHeight: percentageOfMaxKwDelegate.implicitHeight 


    Frame {
        id: surface

        visible : !headerDelegate.visible
        
        anchors.fill: parent

    }

    HeaderDelegate {
        id: headerDelegate

        anchors.fill: parent

        backgroundColor : surface.Material.foreground
        foregroundColor : surface.Material.background
    }

    HourDelegate {
        id: hourDelegate

        anchors.fill: parent
    }

    PercentageOfMaxKwDelegate {
        id: percentageOfMaxKwDelegate

        anchors.centerIn: parent

        width: headerDelegate.header.font.pixelSize * 4
        height: parent.height
    }


    PercentageOfDailyKwhDelegate {
        id: percentageOfDailyKwhDelegate
        
        anchors.fill: parent
    }

    EstimatedKwhGeneratedDelegate {
        id: estimatedKwhGeneratedDelegate
        
        anchors.fill: parent
    }


    
}