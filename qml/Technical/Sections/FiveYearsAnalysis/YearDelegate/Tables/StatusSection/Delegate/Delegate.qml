import QtQuick
import QtQuick.Controls.Material

Item {
    id: delegate

    property int currentYear: 0

    // implicitWidth: column === 0? headerDelegate.implicitWidth:
    //     row===0? headerDelegate.header.font.pixelSize * 5:
    //     row === 1? headerDelegate.header.font.pixelSize * 5 : 10
    

    // implicitHeight: percentageOfMaxKwDelegate.implicitHeight 

    implicitWidth: column === 0? 200:60
    

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

    ChargeSufficiencyDelegate {
        id: chargeSufficiencyDelegate

        anchors.fill: parent
    }

    ChargeStatusDelegate {
        id: chargeStatusDelegate

        anchors.fill: parent
    }

    ChargerNeededDelegate {
        id: chargerNeededDelegate

        anchors.fill: parent

    }

    ReachedEssSocDelegate {
        id: reachedEssSocDelegate

        anchors.fill: parent
    }

    AvailabilityDelegate {
        id: availabilityDelegate

        anchors.fill: parent
    }    

    
}