import QtQuick
import QtQuick.Controls.Material

import "CapitalExpenditure"
import "OperatingExpenditure"
import "Revenue"

import "../Templates" as Templates


Page {
    id: root

    function goToCapitalExpenditureItems(){swipeView.currentIndex = 0}
    function goToExchangeRate(){swipeView.currentIndex = 1}
    function goToDepreciation(){swipeView.currentIndex = 2}

    function goToOperatingExpenditureItems(){swipeView.currentIndex = 3}
    function goToFixedOAndM(){swipeView.currentIndex = 4}

    function goToRevenueItems(){swipeView.currentIndex = 5}
    function goToPricing(){swipeView.currentIndex = 6}
    function goToTariffAssumption(){swipeView.currentIndex = 7}

    SwipeView {
        id: swipeView

        anchors.fill: parent

        orientation: Qt.Vertical

        clip: true
        interactive: false

        CapitalExpenditureItems{id: capitalExpenditureItems}
        ExchangeRate{id: exchangeRate}
        Depreciation{id: depreciation}

        OperatingExpenditureItems{id: operatingExpenditureItems }
        FixedOAndM{id: fixedOAndM }

        RevenueItems{id: revenueItems }
        Pricing{id: pricing }
        TariffAssumption{id: tariffAssumption }

    }

}