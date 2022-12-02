import QtQuick
import QtQuick.Controls.Material

import "Sections/CapitalExpenditure"
import "Sections/OperatingExpenditure"
import "Sections/Revenue"

ScrollView {
    id: root

    CapitalExpenditure{
        id: capitalExpenditure

        anchors {
            top: parent.top
            topMargin: capitalExpenditure.label.height

            left: parent.left
        }

    }

    OperatingExpenditure {
        id: operatingExpenditure

        anchors {
            top: capitalExpenditure.top

            left: capitalExpenditure.right
            leftMargin: operatingExpenditure.label.height
        }

    }

    Revenue {
        id: revenue

        anchors {
            top: operatingExpenditure.bottom
            topMargin: revenue.label.height

            left: operatingExpenditure.left

        }

    }

}