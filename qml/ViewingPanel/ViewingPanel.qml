import QtQuick
import QtQuick.Controls.Material

import "TechnicalHourlySummary"


Page {
    id: root

    SwipeView{
        id: swipeview

        anchors.fill: parent

        contentHeight: technicalHourlySummary.height

        TechnicalHourlySummary {
            id: technicalHourlySummary

            // height: 500
            // width: root.width

        }
    }
}