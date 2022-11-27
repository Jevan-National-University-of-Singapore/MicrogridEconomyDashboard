import QtQuick
import QtQuick.Controls.Material

import "Sections/CapitalExpenditure"
import "Sections/OperatingExpenditure"
import "Sections/Revenue"

Item {
    id: root

    CapitalExpenditure{
        id: capitalExpenditure

        anchors {
            top: root.top
            topMargin: root.height/40

            left: root.left
            leftMargin: root.width/40
        }

        height: root.height/1.6
        width: root.width/2.8
    }

    OperatingExpenditure {
        id: operatingExpenditure

        anchors {
            top: root.top
            topMargin: root.height/40

            left: capitalExpenditure.right
            leftMargin: root.width/40
        }

        width: root.width/2.5
        height: root.height/2.5
    }

    Revenue {
        id: revenue

        anchors {
            top: operatingExpenditure.bottom
            topMargin: operatingExpenditure.anchors.topMargin

            left: operatingExpenditure.left

            bottom: root.bottom
            bottomMargin: operatingExpenditure.anchors.topMargin*2.5
        }

        width: operatingExpenditure.width * 1.1

    }

}