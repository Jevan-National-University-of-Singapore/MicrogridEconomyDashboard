import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Material

import "../Delegates"

Item {
    id: root

    property alias capitalExpenditure: capitalExpenditure
    property alias operatingExpenditure: operatingExpenditure
    property alias revenue: revenue

    visible: opacity

    function collapse() {
        capitalExpenditure.collapse()
        operatingExpenditure.collapse()
        revenue.collapse()
        opacityAnimation.velocity = 5
        opacity = 0
    }    

    function show() {
        capitalExpenditure.show()
        operatingExpenditure.show()
        revenue.show()
        opacityAnimation.velocity = 2.5
        opacity = 1
    }        

    Behavior on opacity { 
        SmoothedAnimation { 
            id: opacityAnimation
            velocity: 5 
        } 
    }

    Column{
        id: subTreeViews

        clip: true

        height: childrenRect.implicitHeight; width: contentWidth

        CapitalExpenditureTreeView {
            id: capitalExpenditure

            onCapitalExpenditureItemsSelected: {
                operatingExpenditure.deselectAll()
                revenue.deselectAll()
            }
            onExchangeRateSelected: {
                operatingExpenditure.deselectAll()
                revenue.deselectAll()
            }
            onDepreciationSelected: {
                operatingExpenditure.deselectAll()
                revenue.deselectAll()
            }
        }

        OperatingExpenditureTreeView {
            id: operatingExpenditure

            onOperatingExpenditureItemsSelected:{
                revenue.deselectAll()
                capitalExpenditure.deselectAll()
            }

            onFixedOAndMSelected:{
                revenue.deselectAll()
                capitalExpenditure.deselectAll()
            }


        }

        RevenueTreeView {
            id: revenue           

            onFiveYearsLifetimeSelected: {
                capitalExpenditure.deselectAll()
                operatingExpenditure.deselectAll()
            }
            onPerAnnumSelected: {
                capitalExpenditure.deselectAll()
                operatingExpenditure.deselectAll()
            }
            onTariffAssumptionSelected: {
                capitalExpenditure.deselectAll()
                operatingExpenditure.deselectAll()
            }
        }

    }
}