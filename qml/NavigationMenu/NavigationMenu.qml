import QtQuick
import QtQuick.Controls.Material

import "TechnicalTreeView"
import "FinancialTreeView"

ScrollView {
    id: root

    contentHeight: surface.height; contentWidth: surface.width

    property alias technical: technical
    property alias financial: financial


    Pane {
        id: surface
        height: root.height; width: root.width


        TechnicalTreeView{
            id: technical

            anchors.fill: parent

            height: surface.height; width: surface.width
        }

        FinancialTreeView{
            id: financial

            anchors.fill: parent

            height: surface.height; width: surface.width
        }

    }

}