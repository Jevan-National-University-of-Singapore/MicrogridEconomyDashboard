import QtQuick
import QtQuick.Controls.Material

import "Revenue" as Revenue

Item {
    id: delegate

    property int currentYear: 0

    implicitWidth: column === 0? 250:100

    implicitHeight: 30

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

    Revenue.TotalDelegate {
        id: totalDelegate

        anchors.fill: parent
    }

    Revenue.ChargersDelegate {
        id: chargersDelegate

        anchors.fill: parent
    }    

    Revenue.RetailToFacilityDelegate {
        id: retailToFacilityDelegate

        anchors.fill: parent
    }    
    OpexDelegate {
        id: opexDelegate

        anchors.fill: parent
    }    
    EbitdaDelegate {
        id: ebitdaDelegate

        anchors.fill: parent
    }   
}