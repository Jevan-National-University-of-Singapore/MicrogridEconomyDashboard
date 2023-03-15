import QtQuick
import QtQuick.Controls.Material

import "Depreciation" as Depreciation

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

    Depreciation.TotalDelegate {
        id: totalDelegate

        anchors.fill: parent
    }

    Depreciation.ChargersDelegate {
        id: chargersDelegate

        anchors.fill: parent
    }    

    Depreciation.EssDelegate {
        id: essDelegate

        anchors.fill: parent
    }    

    EbitDelegate {
        id: ebitDelegate

        anchors.fill: parent
    }   
}