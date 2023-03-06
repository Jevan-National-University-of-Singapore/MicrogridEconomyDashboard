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

            subsection: "Financial"

            Templates.LabelledText {
                id: netPresentValue

                labelText: "Net Present Value"
                units: "RM"

                text: Scenario.fiveYearAnalysis.netPresentValue

            }

            Templates.LabelledText {
                id: internalRateOfReturn

                labelText: "Internal Rate Of Return"
                units: "RM"

                text: Scenario.fiveYearAnalysis.internalRateOfReturn

            }

            Templates.LabelledText {
                id: netProfits

                labelText: "Net Profits"
                units: "RM"

                text: Scenario.fiveYearAnalysis.netProfits

            }

            Templates.LabelledText {
                id: initialInvestment

                labelText: "Initial Investment"
                units: "RM"

                text: Scenario.fiveYearAnalysis.initialInvestment

            }


        }
}