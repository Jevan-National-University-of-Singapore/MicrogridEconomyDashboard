import QtQuick
import QtQuick.Controls.Material

import "TechnicalTreeView"

ScrollView {
    id: root

    contentHeight: surface.height; contentWidth: surface.width

    property alias technical: technical


    Pane {
        id: surface
        // anchors.fill: parent
        height: root.height; width: root.width


        TechnicalTreeView{
            id: technical

            anchors.fill: parent

            height: surface.height; width: surface.width
        }

    }

}