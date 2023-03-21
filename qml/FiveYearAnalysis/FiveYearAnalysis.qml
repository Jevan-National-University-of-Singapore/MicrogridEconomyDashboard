import QtQuick
import QtQuick.Controls.Material

import "../Templates" as Templates


Page {
    id: root

    // function goToCapitalExpenditureItems(){swipeView.currentIndex = 0}
    // function goToExchangeRate(){swipeView.currentIndex = 1}
    // function goToDepreciation(){swipeView.currentIndex = 2}

    // function goToOperatingExpenditureItems(){swipeView.currentIndex = 3}
    // function goToFixedOAndM(){swipeView.currentIndex = 4}

    // function goToFiveYearLifetime(){swipeView.currentIndex = 5}
    // function goToPerAnnum(){swipeView.currentIndex = 6}
    // function goToTariffAssumption(){swipeView.currentIndex = 7}

    // SwipeView {
    //     id: swipeView

    //     anchors.fill: parent

    //     orientation: Qt.Vertical

    //     clip: true
    //     interactive: false

    //     CapitalExpenditureItems{id: capitalExpenditureItems}
    //     ExchangeRate{id: exchangeRate}
    //     Depreciation{id: depreciation}

    //     OperatingExpenditureItems{id: operatingExpenditureItems }
    //     FixedOAndM{id: fixedOAndM }

    //     FiveYearLifetime{id: fiveYearLifetime }
    //     PerAnnum{id: perAnnum }
    //     TariffAssumption{id: tariffAssumption }

    // }
    Templates.SubSection {
            id: subsectionItems

            subsection: "Breakeven analysis"

            Templates.LabelledText {
                id: revenueRequiredFromChargers

                labelText: "Revenue required from chargers"
                units: "RM"

                text: Scenario.fiveYearAnalysis.breakeven.revenueRequiredFromChargers.toFixed(2)

            }

            Templates.LabelledText {
                id: revenueFromRetailToFacility

                labelText: "Revenue from retail to facility"
                units: "RM"

                text: Scenario.fiveYearAnalysis.breakeven.revenueFromRetailToFacility.toFixed(2)

            }

            Templates.LabelledText {
                id: totalRevenueRequired

                labelText: "Total revenue required"
                units: "RM"

                text: Scenario.fiveYearAnalysis.breakeven.totalRevenueRequired.toFixed(2)

            }
        }

        Templates.LabelledText {
            id: evChargingPriceToBreakeven

            anchors {
                top: subsectionItems.bottom
                topMargin: Qt.application.font.pixelSize

                left: subsectionItems.left
                leftMargin: Qt.application.font.pixelSize
            }

            labelText: "EV charging price to breakeven"
            units: "RM"

            text: Scenario.fiveYearAnalysis.breakeven.evChargingPriceToBreakeven.toFixed(2)

        }

        Frame {
            anchors.centerIn: evChargingPriceToBreakeven

            height: evChargingPriceToBreakeven.height + Qt.application.font.pixelSize
            width: evChargingPriceToBreakeven.width + (Qt.application.font.pixelSize * 2)
        }
}