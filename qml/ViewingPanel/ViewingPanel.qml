import QtQuick
import QtQuick.Controls.Material

import "TechnicalHourlySummary"
import "FinancialSummary"


Page {
    id: root

    function goToTechnicalHourlySummary(){
        swipeview.currentIndex = 0
    }
    function goToFinancialSummary(){
        swipeview.currentIndex = 1
    }

    SwipeView{
        id: swipeview

        anchors.fill: parent

        contentHeight: Math.max(technicalHourlySummary.height, financialSummary.height)

        TechnicalHourlySummary {
            id: technicalHourlySummary

            // height: 500
            // width: root.width

        }

        FinancialSummary {
            id: financialSummary
        }
    }
}