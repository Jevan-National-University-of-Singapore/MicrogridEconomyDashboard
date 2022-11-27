import "../../../Templates"
import "../../../Templates/Separators"

import "SubSections"


Section {
    id: root

    section: "Capital Expenditure"

    CapitalExpenditureItems {
        id: capitalExpenditureItems

        anchors.verticalCenter: capitalExpenditureItemsSeparator.verticalCenter
    }

    VerticalSeparator {
        id: capitalExpenditureItemsSeparator

        anchors {
            left: capitalExpenditureItems.right
            leftMargin: capitalExpenditureItems.width/8
            verticalCenter: root.verticalCenter
        }

        length: root.height/1.2
    }

    ExchangeRate {
        id: exchangeRate

        anchors {
            left: capitalExpenditureItemsSeparator.right
            leftMargin: exchangeRate.width/8
        }
    }

    
    HorizontalSeparator {
        id: exchangeRateSeparator

        anchors {
            top: exchangeRate.bottom
            topMargin: exchangeRate.height/5
            horizontalCenter: exchangeRate.horizontalCenter
        }

        length: exchangeRate.width/1.2
    }

    Depreciation {
        id: depreciation

        anchors {
            top: exchangeRateSeparator.bottom
            topMargin: exchangeRate.height/8

            left: exchangeRate.left
        }
    }

}