import QtQuick.Layouts

import "../../../Templates"
import "../../../Templates/Separators"

import "SubSections"

import QtQuick
Section {
    id: root

    section: "Capital Expenditure"

    ColumnLayout {
        id: rightColumn

        spacing: exchangeRate.label.font.pixelSize

        anchors {
            top: parent.top

            left: parent.left
            leftMargin: capitalExpenditureItems.width + capitalExpenditureItems.anchors.rightMargin
                        + rightColumnSeparator.anchors.rightMargin

        }

        ExchangeRate {
            id: exchangeRate

        }

    
        HorizontalSeparator {
            id: exchangeRateSeparator
            Layout.alignment: Qt.AlignCenter

            length: exchangeRate.width - rightColumn.spacing
        }

        Depreciation {
            id: depreciation

        }
    }

    VerticalSeparator {
        id: rightColumnSeparator

        anchors {
            right: rightColumn.left
            rightMargin: rightColumn.spacing
        }

        length: rightColumn.height - rightColumn.spacing
    }


    CapitalExpenditureItems {
        id: capitalExpenditureItems

        anchors{
            right: rightColumnSeparator.right
            rightMargin: rightColumn.spacing

            verticalCenter: rightColumn.verticalCenter
        }
    }




}