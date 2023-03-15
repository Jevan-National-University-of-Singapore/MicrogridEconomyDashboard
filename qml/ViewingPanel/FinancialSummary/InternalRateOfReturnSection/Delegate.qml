import QtQuick
import QtQuick.Controls.Material

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

    InitialInvestment {
        id: initialInvestment
        
        anchors.fill: parent
    }

    NetProfitsFairValue {
        id: netProfitsFairValue

        anchors.fill: parent
    }   

    NetPresentValue {
        id: netPresentValue

        anchors.fill: parent
    }  

    InternalRateOfReturn {
        id: internalRateOfReturn

        anchors.fill: parent
    }  


}