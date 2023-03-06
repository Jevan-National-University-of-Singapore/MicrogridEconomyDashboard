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

    OperatingCashFlowDelegate {
        id: operatingCashFlowDelegate

        anchors.fill: parent
    }  

    CapexDelegate {
        id: capexDelegate

        anchors.fill: parent
    }   

    ChangeInNetWorkingCapitalDelegate {
        id: changeInNetWorkingCapitalDelegate

        anchors.fill: parent
    }  

    FreeCashFlowDelegate {
        id: freeCashFlowDelegate

        anchors.fill: parent
    }   


}