import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts

import "../../Templates" as Templates

// import "OperationalYearSection"
import "EbitdaSection"
import "EbitSection"
import "NetIncomeSection"
import "FreeCashFlowSection"
import "PresentValueOfCashFlowSection"


Templates.Page{
    id: root

    Column {

        id: tables
        EbitdaSection {
            id: ebitdaSection

            height: contentHeight
            width: root.width// - label.font.pixelSize
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

        PresentValueOfCashFlowSection {
            id: presentValueOfCashFlowSection

            height: contentHeight
            width: ebitdaSection.width

            syncView: ebitdaSection
            syncDirection: Qt.Horizontal
        }


    }


}