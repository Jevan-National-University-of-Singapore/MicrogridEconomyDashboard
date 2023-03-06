import QtQuick
import QtQuick.Controls.Material

Item {
    id: delegate

    property int currentYear: 0

    implicitWidth: column === 0? 200:100

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

    DiscountedCashFlowsDelegate {
        id: discountedCashFlowsDelegate

        anchors.fill: parent
    }  

    PresentValueOfCashFlowDelegate {
        id: presentValueOfCashFlowDelegate

        anchors.fill: parent
    }   

}