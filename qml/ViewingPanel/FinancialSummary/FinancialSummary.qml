import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts

import "../../Templates" as Templates

// import "OperationalYearSection"
import "EbitdaSection"
import "EbitSection"
import "NetIncomeSection"
import "FreeCashFlowSection"
import "DiscountedCashFlowsSection"

import "InternalRateOfReturnSection"

Templates.Page{
    id: root

    Column {
        id: cashFlow

        EbitdaSection {
            id: ebitdaSection

            height: contentHeight
            width: root.width/3
            // width: root.width// - label.font.pixelSize
        }

        EbitSection {
            id: ebitSection

            height: contentHeight
            width: ebitdaSection.width

            syncView: ebitdaSection
            syncDirection: Qt.Horizontal
        }

        NetIncomeSection {
            id: netIncomeSection

            height: contentHeight
            width: ebitdaSection.width

            syncView: ebitdaSection
            syncDirection: Qt.Horizontal
        }

        FreeCashFlowSection {
            id: freeCashFlowSection

            height: contentHeight
            width: ebitdaSection.width

            syncView: ebitdaSection
            syncDirection: Qt.Horizontal
        }

        DiscountedCashFlowsSection {
            id: discountedCashFlowsSection

            height: contentHeight
            width: ebitdaSection.width

            syncView: ebitdaSection
            syncDirection: Qt.Horizontal
        }


    }

    GroupBox {
        id: summary

        title: qsTr("Summary")
        height: internalRateOfReturnSection.height + Qt.application.font.pointSize * 6
        width: internalRateOfReturnSection.width
        InternalRateOfReturnSection {
            id: internalRateOfReturnSection
            height: contentHeight
            implicitWidth: root.width/3.4
        }

        anchors.left: cashFlow.right
    }


}